"""Tests for the environment module."""

import sys

sys.path.insert(0, "src")


class TestSelectEnvFile:
    """Tests for the select_env_file function."""

    def test_select_env_file_returns_dot_env(self):
        """Test selecting env file always returns .env."""
        from environment import select_env_file

        result = select_env_file()
        assert result == ".env"
