import sys
import pytest

sys.path.insert(0, "src")

from data_analyzer import DataAnalyzer


class TestDataAnalyzer:
    def test_data_analyzer_initialization(self):
        analyzer = DataAnalyzer("german")
        assert analyzer.language == "german"
        assert analyzer.db is not None

    def test_analyze_data_with_valid_language(self):
        analyzer = DataAnalyzer("german")
        try:
            count = analyzer.analyze_data()
            assert isinstance(count, int)
            assert count >= 0
        except ValueError:
            pass

    def test_analyze_data_with_invalid_language(self):
        analyzer = DataAnalyzer("nonexistent_language_xyz")
        with pytest.raises(ValueError) as excinfo:
            analyzer.analyze_data()
        assert "not found in the database" in str(excinfo.value)

    def test_analyze_data_mocked(self, mocker):
        mock_db = mocker.Mock()
        mock_db.check_for_language.return_value = True
        mock_db.analyze_data.return_value = 42
        mocker.patch("data_analyzer.PronunciationDatabase", return_value=mock_db)

        analyzer = DataAnalyzer("german")
        result = analyzer.analyze_data()

        assert result == 42
        mock_db.check_for_language.assert_called_once_with("german")
        mock_db.analyze_data.assert_called_with("german")

    def test_analyze_data_language_not_found_mocked(self, mocker):
        mock_db = mocker.Mock()
        mock_db.check_for_language.return_value = False
        mocker.patch("data_analyzer.PronunciationDatabase", return_value=mock_db)

        analyzer = DataAnalyzer("spanish")
        with pytest.raises(ValueError) as excinfo:
            analyzer.analyze_data()
        assert "spanish" in str(excinfo.value)
        assert "not found in the database" in str(excinfo.value)
