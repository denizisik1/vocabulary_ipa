"""Tests for the environment module."""

import sys
import pytest

sys.path.insert(0, "src")


class TestSelectEnvFile:
    """Tests for the select_env_file function."""

    def test_select_env_file_main_branch(self, mocker):
        """Test selecting env file on main branch."""
        mock_repo = mocker.MagicMock()
        mock_repo.head.shorthand = "main"
        mocker.patch("environment.Repository", return_value=mock_repo)

        import environment

        # Patch the module-level branch_name
        mocker.patch.object(environment, "branch_name", "main")
        result = environment.select_env_file()
        assert result == ".env.production"

    def test_select_env_file_testing_branch(self, mocker):
        """Test selecting env file on testing branch."""
        mock_repo = mocker.MagicMock()
        mock_repo.head.shorthand = "testing"
        mocker.patch("environment.Repository", return_value=mock_repo)

        import environment

        mocker.patch.object(environment, "branch_name", "testing")
        result = environment.select_env_file()
        assert result == ".env.testing"

    def test_select_env_file_development_branch(self, mocker):
        """Test selecting env file on development branch."""
        mock_repo = mocker.MagicMock()
        mock_repo.head.shorthand = "development"
        mocker.patch("environment.Repository", return_value=mock_repo)

        import environment

        mocker.patch.object(environment, "branch_name", "development")
        result = environment.select_env_file()
        assert result == ".env.development"

    def test_select_env_file_unrecognized_branch(self, mocker):
        """Test selecting env file on an unrecognized branch exits."""
        mock_repo = mocker.MagicMock()
        mock_repo.head.shorthand = "feature-xyz"
        mocker.patch("environment.Repository", return_value=mock_repo)

        import environment

        mocker.patch.object(environment, "branch_name", "feature-xyz")
        with pytest.raises(SystemExit):
            environment.select_env_file()
