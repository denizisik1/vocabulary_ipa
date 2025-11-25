"""Tests for the VersionInfo class."""

import sys

sys.path.insert(0, "src")


class TestVersionInfo:
    """Tests for the VersionInfo class."""

    def test_version_info_initialization(self, mocker):
        """Test that VersionInfo initializes correctly."""
        mock_select_env = mocker.patch("version_info.select_env_file", return_value=".env.testing")
        mock_load_dotenv = mocker.patch("version_info.load_dotenv")
        mocker.patch("version_info.os.getenv", return_value="1.0.0")

        from version_info import VersionInfo

        vi = VersionInfo()
        assert vi.version == "1.0.0"
        mock_select_env.assert_called_once()
        mock_load_dotenv.assert_called_once_with(".env.testing")

    def test_version_info_display(self, mocker):
        """Test that VersionInfo displays the version correctly."""
        mocker.patch("version_info.select_env_file", return_value=".env.testing")
        mocker.patch("version_info.load_dotenv")
        mocker.patch("version_info.os.getenv", return_value="2.1.3")

        from version_info import VersionInfo

        vi = VersionInfo()
        # display() logs the version, we just test it doesn't raise
        vi.display()

    def test_version_info_none_version(self, mocker):
        """Test VersionInfo when VERSION env var is not set."""
        mocker.patch("version_info.select_env_file", return_value=".env.testing")
        mocker.patch("version_info.load_dotenv")
        mocker.patch("version_info.os.getenv", return_value=None)

        from version_info import VersionInfo

        vi = VersionInfo()
        assert vi.version is None

    def test_version_info_production_env(self, mocker):
        """Test VersionInfo with production environment."""
        mocker.patch("version_info.select_env_file", return_value=".env.production")
        mock_load_dotenv = mocker.patch("version_info.load_dotenv")
        mocker.patch("version_info.os.getenv", return_value="3.0.0")

        from version_info import VersionInfo

        vi = VersionInfo()
        assert vi.version == "3.0.0"
        mock_load_dotenv.assert_called_once_with(".env.production")
