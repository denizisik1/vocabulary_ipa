"""Tests for the environment module."""

import sys
import pytest
from unittest.mock import patch, MagicMock

sys.path.insert(0, "src")


class TestSelectEnvFile:
    """Tests for the select_env_file function."""

    @patch("environment.Repository")
    def test_select_env_file_main_branch(self, mock_repo_class):
        """Test selecting env file on main branch."""
        mock_repo = MagicMock()
        mock_repo.head.shorthand = "main"
        mock_repo_class.return_value = mock_repo

        # Need to reimport to pick up the mock
        import importlib
        import environment

        # Patch the module-level branch_name
        with patch.object(environment, "branch_name", "main"):
            result = environment.select_env_file()
            assert result == ".env.production"

    @patch("environment.Repository")
    def test_select_env_file_testing_branch(self, mock_repo_class):
        """Test selecting env file on testing branch."""
        mock_repo = MagicMock()
        mock_repo.head.shorthand = "testing"
        mock_repo_class.return_value = mock_repo

        import environment

        with patch.object(environment, "branch_name", "testing"):
            result = environment.select_env_file()
            assert result == ".env.testing"

    @patch("environment.Repository")
    def test_select_env_file_development_branch(self, mock_repo_class):
        """Test selecting env file on development branch."""
        mock_repo = MagicMock()
        mock_repo.head.shorthand = "development"
        mock_repo_class.return_value = mock_repo

        import environment

        with patch.object(environment, "branch_name", "development"):
            result = environment.select_env_file()
            assert result == ".env.development"

    @patch("environment.Repository")
    def test_select_env_file_unrecognized_branch(self, mock_repo_class):
        """Test selecting env file on an unrecognized branch exits."""
        mock_repo = MagicMock()
        mock_repo.head.shorthand = "feature-xyz"
        mock_repo_class.return_value = mock_repo

        import environment

        with patch.object(environment, "branch_name", "feature-xyz"):
            with pytest.raises(SystemExit):
                environment.select_env_file()
