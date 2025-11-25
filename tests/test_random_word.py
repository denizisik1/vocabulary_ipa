"""Tests for the RandomWord class."""

import sys
import pytest
from unittest.mock import Mock, patch
from io import StringIO

sys.path.insert(0, "src")

from random_word import RandomWord


class TestRandomWord:
    """Tests for the RandomWord class."""

    def test_random_word_initialization(self):
        """Test that RandomWord initializes correctly."""
        rw = RandomWord("german", 5)
        assert rw.language == "german"
        assert rw.number == 5
        assert rw.db is not None

    def test_get_random_word_with_invalid_language(self):
        """Test that getting random word with invalid language raises ValueError."""
        rw = RandomWord("nonexistent_language_xyz", 1)
        with pytest.raises(ValueError) as excinfo:
            rw.get_random_word()
        assert "not found in the database" in str(excinfo.value)

    @patch("random_word.PronunciationDatabase")
    def test_get_random_word_with_valid_language_mocked(self, mock_db_class):
        """Test getting random word with a mocked database."""
        mock_db = Mock()
        mock_db.check_for_language.return_value = True
        mock_db.retrieve_random_word.return_value = [
            ("der", "Hund", "dog", "[hʊnt]"),
        ]
        mock_db_class.return_value = mock_db

        rw = RandomWord("german", 1)
        # Should not raise an exception
        rw.get_random_word()

        mock_db.check_for_language.assert_called_once_with("german")
        mock_db.retrieve_random_word.assert_called_once_with("german", 1)

    @patch("random_word.PronunciationDatabase")
    def test_get_random_word_language_not_found_mocked(self, mock_db_class):
        """Test that ValueError is raised when language is not found."""
        mock_db = Mock()
        mock_db.check_for_language.return_value = False
        mock_db_class.return_value = mock_db

        rw = RandomWord("spanish", 3)
        with pytest.raises(ValueError) as excinfo:
            rw.get_random_word()
        assert "spanish" in str(excinfo.value)
        assert "not found in the database" in str(excinfo.value)

    @patch("random_word.PronunciationDatabase")
    def test_get_random_word_no_data_returned(self, mock_db_class):
        """Test handling when no data is returned from the database."""
        mock_db = Mock()
        mock_db.check_for_language.return_value = True
        mock_db.retrieve_random_word.return_value = None
        mock_db_class.return_value = mock_db

        rw = RandomWord("german", 1)
        # Should handle None gracefully
        rw.get_random_word()

    @patch("random_word.PronunciationDatabase")
    def test_get_random_word_multiple_rows(self, mock_db_class):
        """Test getting multiple random words."""
        mock_db = Mock()
        mock_db.check_for_language.return_value = True
        mock_db.retrieve_random_word.return_value = [
            ("der", "Hund", "dog", "[hʊnt]"),
            ("die", "Katze", "cat", "[katsə]"),
            ("das", "Auto", "car", "[aʊto]"),
        ]
        mock_db_class.return_value = mock_db

        rw = RandomWord("german", 3)
        rw.get_random_word()

        mock_db.retrieve_random_word.assert_called_once_with("german", 3)

    @patch("random_word.PronunciationDatabase")
    def test_get_random_word_with_none_values_in_row(self, mock_db_class):
        """Test handling rows with None values."""
        mock_db = Mock()
        mock_db.check_for_language.return_value = True
        mock_db.retrieve_random_word.return_value = [
            (None, "Hund", None, "[hʊnt]"),
        ]
        mock_db_class.return_value = mock_db

        rw = RandomWord("german", 1)
        # Should handle None values in row gracefully
        rw.get_random_word()

    @patch("random_word.PronunciationDatabase")
    def test_get_random_word_single_tuple_normalization(self, mock_db_class):
        """Test that a single tuple is normalized to a list of rows."""
        mock_db = Mock()
        mock_db.check_for_language.return_value = True
        # Return a single tuple (not a list of tuples)
        mock_db.retrieve_random_word.return_value = ("der", "Hund", "dog", "[hʊnt]")
        mock_db_class.return_value = mock_db

        rw = RandomWord("german", 1)
        # Should normalize the single tuple to a list
        rw.get_random_word()
