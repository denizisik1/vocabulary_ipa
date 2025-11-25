"""Tests for the PronunciationDatabase class."""

import sys
import sqlite3
import os
import pytest

sys.path.insert(0, "src")

from database import PronunciationDatabase


class TestPronunciationDatabase:
    """Tests for the PronunciationDatabase class."""

    def test_database_initialization(self):
        """Test that the database initializes correctly."""
        db = PronunciationDatabase()
        assert db.connection is not None
        assert db.cursor is not None

    def test_check_for_language_existing(self):
        """Test checking for an existing language table."""
        db = PronunciationDatabase()
        # German is expected to exist based on test_database_connection.py
        result = db.check_for_language("german")
        assert result is True

    def test_check_for_language_nonexistent(self):
        """Test checking for a non-existent language table."""
        db = PronunciationDatabase()
        result = db.check_for_language("nonexistent_language_xyz")
        assert result is False

    def test_list_available_languages(self):
        """Test listing available language tables."""
        db = PronunciationDatabase()
        languages = db.list_available_languages()
        assert isinstance(languages, list)
        # At least german should exist
        assert "german" in languages

    def test_retrieve_random_word_single(self):
        """Test retrieving a single random word."""
        db = PronunciationDatabase()
        if db.check_for_language("german"):
            result = db.retrieve_random_word("german", 1)
            if result:
                assert isinstance(result, list)
                assert len(result) <= 1

    def test_retrieve_random_word_multiple(self):
        """Test retrieving multiple random words."""
        db = PronunciationDatabase()
        if db.check_for_language("german"):
            result = db.retrieve_random_word("german", 3)
            if result:
                assert isinstance(result, list)
                assert len(result) <= 3

    def test_analyze_data(self):
        """Test analyzing data for rows without pronunciation."""
        db = PronunciationDatabase()
        if db.check_for_language("german"):
            count = db.analyze_data("german")
            assert isinstance(count, int)
            assert count >= 0

    def test_check_for_language_sql_injection_prevention(self):
        """Test that SQL injection attempts are handled safely."""
        db = PronunciationDatabase()
        # This should not cause any issues due to parameterized query
        result = db.check_for_language("german'; DROP TABLE german; --")
        assert result is False

    def test_list_available_languages_returns_only_alpha(self):
        """Test that list_available_languages only returns alphabetic table names."""
        db = PronunciationDatabase()
        languages = db.list_available_languages()
        for lang in languages:
            assert lang.isalpha(), f"Language '{lang}' should only contain alphabetic characters"
