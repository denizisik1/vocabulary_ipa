import sys
import pytest

sys.path.insert(0, "src")

from random_word import RandomWord


class TestRandomWord:
    def test_random_word_initialization(self):
        rw = RandomWord("german", 5)
        assert rw.language == "german"
        assert rw.number == 5
        assert rw.db is not None

    def test_get_random_word_with_invalid_language(self):
        rw = RandomWord("nonexistent_language_xyz", 1)
        with pytest.raises(ValueError) as excinfo:
            rw.get_random_word()
        assert "not found in the database" in str(excinfo.value)

    def test_get_random_word_with_valid_language_mocked(self, mocker):
        mock_db = mocker.Mock()
        mock_db.check_for_language.return_value = True
        mock_db.retrieve_random_word.return_value = [
            ("der", "Hund", "dog", "[hʊnt]"),
        ]
        mocker.patch("random_word.PronunciationDatabase", return_value=mock_db)

        rw = RandomWord("german", 1)
        # Should not raise an exception
        rw.get_random_word()

        mock_db.check_for_language.assert_called_once_with("german")
        mock_db.retrieve_random_word.assert_called_once_with("german", 1)

    def test_get_random_word_language_not_found_mocked(self, mocker):
        mock_db = mocker.Mock()
        mock_db.check_for_language.return_value = False
        mocker.patch("random_word.PronunciationDatabase", return_value=mock_db)

        rw = RandomWord("spanish", 3)
        with pytest.raises(ValueError) as excinfo:
            rw.get_random_word()
        assert "spanish" in str(excinfo.value)
        assert "not found in the database" in str(excinfo.value)

    def test_get_random_word_no_data_returned(self, mocker):
        mock_db = mocker.Mock()
        mock_db.check_for_language.return_value = True
        mock_db.retrieve_random_word.return_value = None
        mocker.patch("random_word.PronunciationDatabase", return_value=mock_db)

        rw = RandomWord("german", 1)
        # Should handle None gracefully
        rw.get_random_word()

    def test_get_random_word_multiple_rows(self, mocker):
        mock_db = mocker.Mock()
        mock_db.check_for_language.return_value = True
        mock_db.retrieve_random_word.return_value = [
            ("der", "Hund", "dog", "[hʊnt]"),
            ("die", "Katze", "cat", "[katsə]"),
            ("das", "Auto", "car", "[aʊto]"),
        ]
        mocker.patch("random_word.PronunciationDatabase", return_value=mock_db)

        rw = RandomWord("german", 3)
        rw.get_random_word()

        mock_db.retrieve_random_word.assert_called_once_with("german", 3)

    def test_get_random_word_with_none_values_in_row(self, mocker):
        mock_db = mocker.Mock()
        mock_db.check_for_language.return_value = True
        mock_db.retrieve_random_word.return_value = [
            (None, "Hund", None, "[hʊnt]"),
        ]
        mocker.patch("random_word.PronunciationDatabase", return_value=mock_db)

        rw = RandomWord("german", 1)
        # Should handle None values in row gracefully
        rw.get_random_word()

    def test_get_random_word_single_tuple_normalization(self, mocker):
        mock_db = mocker.Mock()
        mock_db.check_for_language.return_value = True
        # Return a single tuple (not a list of tuples)
        mock_db.retrieve_random_word.return_value = ("der", "Hund", "dog", "[hʊnt]")
        mocker.patch("random_word.PronunciationDatabase", return_value=mock_db)

        rw = RandomWord("german", 1)
        # Should normalize the single tuple to a list
        rw.get_random_word()
