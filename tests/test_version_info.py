"""Tests for the VersionInfo class."""

import sys
import os
import pytest
from unittest.mock import patch, MagicMock

sys.path.insert(0, "src")


class TestVersionInfo:
    """Tests for the VersionInfo class."""

    @patch("version_info.load_dotenv")
    @patch("version_info.select_env_file")
    @patch("version_info.os.getenv")
    def test_version_info_initialization(self, mock_getenv, mock_select_env, mock_load_dotenv):
        """Test that VersionInfo initializes correctly."""
        mock_select_env.return_value = ".env.testing"
        mock_getenv.return_value = "1.0.0"

        from version_info import VersionInfo

        vi = VersionInfo()
        assert vi.version == "1.0.0"
        mock_select_env.assert_called_once()
        mock_load_dotenv.assert_called_once_with(".env.testing")

    @patch("version_info.load_dotenv")
    @patch("version_info.select_env_file")
    @patch("version_info.os.getenv")
    def test_version_info_display(self, mock_getenv, mock_select_env, mock_load_dotenv):
        """Test that VersionInfo displays the version correctly."""
        mock_select_env.return_value = ".env.testing"
        mock_getenv.return_value = "2.1.3"

        from version_info import VersionInfo

        vi = VersionInfo()
        # display() logs the version, we just test it doesn't raise
        vi.display()

    @patch("version_info.load_dotenv")
    @patch("version_info.select_env_file")
    @patch("version_info.os.getenv")
    def test_version_info_none_version(self, mock_getenv, mock_select_env, mock_load_dotenv):
        """Test VersionInfo when VERSION env var is not set."""
        mock_select_env.return_value = ".env.testing"
        mock_getenv.return_value = None

        from version_info import VersionInfo

        vi = VersionInfo()
        assert vi.version is None

    @patch("version_info.load_dotenv")
    @patch("version_info.select_env_file")
    @patch("version_info.os.getenv")
    def test_version_info_production_env(self, mock_getenv, mock_select_env, mock_load_dotenv):
        """Test VersionInfo with production environment."""
        mock_select_env.return_value = ".env.production"
        mock_getenv.return_value = "3.0.0"

        from version_info import VersionInfo

        vi = VersionInfo()
        assert vi.version == "3.0.0"
        mock_load_dotenv.assert_called_once_with(".env.production")
