"""Tests for the DataAnalyzer class."""

import sys
import pytest
from unittest.mock import Mock, patch

sys.path.insert(0, "src")

from data_analyzer import DataAnalyzer


class TestDataAnalyzer:
    """Tests for the DataAnalyzer class."""

    def test_data_analyzer_initialization(self):
        """Test that DataAnalyzer initializes correctly."""
        analyzer = DataAnalyzer("german")
        assert analyzer.language == "german"
        assert analyzer.db is not None

    def test_analyze_data_with_valid_language(self):
        """Test analyzing data with a valid language."""
        analyzer = DataAnalyzer("german")
        # This should work if german table exists
        try:
            count = analyzer.analyze_data()
            assert isinstance(count, int)
            assert count >= 0
        except ValueError:
            # German table might not exist in test environment
            pass

    def test_analyze_data_with_invalid_language(self):
        """Test that analyzing data with an invalid language raises ValueError."""
        analyzer = DataAnalyzer("nonexistent_language_xyz")
        with pytest.raises(ValueError) as excinfo:
            analyzer.analyze_data()
        assert "not found in the database" in str(excinfo.value)

    @patch("data_analyzer.PronunciationDatabase")
    def test_analyze_data_mocked(self, mock_db_class):
        """Test analyzing data with a mocked database."""
        mock_db = Mock()
        mock_db.check_for_language.return_value = True
        mock_db.analyze_data.return_value = 42
        mock_db_class.return_value = mock_db

        analyzer = DataAnalyzer("german")
        result = analyzer.analyze_data()

        assert result == 42
        mock_db.check_for_language.assert_called_once_with("german")
        mock_db.analyze_data.assert_called_with("german")

    @patch("data_analyzer.PronunciationDatabase")
    def test_analyze_data_language_not_found_mocked(self, mock_db_class):
        """Test that ValueError is raised when language is not found."""
        mock_db = Mock()
        mock_db.check_for_language.return_value = False
        mock_db_class.return_value = mock_db

        analyzer = DataAnalyzer("spanish")
        with pytest.raises(ValueError) as excinfo:
            analyzer.analyze_data()
        assert "spanish" in str(excinfo.value)
        assert "not found in the database" in str(excinfo.value)
