import sys

sys.path.insert(0, "src")

from list_languages import ListLanguages


class TestListLanguages:
    def test_list_languages_initialization(self):
        ll = ListLanguages()
        assert ll.db is not None

    def test_list_languages_with_available_languages(self, mocker):
        mock_db = mocker.Mock()
        mock_db.list_available_languages.return_value = ["german", "spanish", "french"]
        mocker.patch("list_languages.PronunciationDatabase", return_value=mock_db)

        ll = ListLanguages()
        result = ll.list_languages()

        assert result == ["german", "spanish", "french"]
        mock_db.list_available_languages.assert_called_once()

    def test_list_languages_with_no_languages(self, mocker, capsys):
        mock_db = mocker.Mock()
        mock_db.list_available_languages.return_value = []
        mocker.patch("list_languages.PronunciationDatabase", return_value=mock_db)

        ll = ListLanguages()
        result = ll.list_languages()

        assert result is None
        captured = capsys.readouterr()
        assert "No languages found" in captured.out

    def test_list_languages_with_real_database(self):
        ll = ListLanguages()
        result = ll.list_languages()
        if result:
            assert "german" in result

    def test_list_languages_prints_each_language(self, mocker, capsys):
        mock_db = mocker.Mock()
        mock_db.list_available_languages.return_value = ["german", "spanish"]
        mocker.patch("list_languages.PronunciationDatabase", return_value=mock_db)

        ll = ListLanguages()
        ll.list_languages()

        captured = capsys.readouterr()
        assert "german" in captured.out
        assert "spanish" in captured.out
