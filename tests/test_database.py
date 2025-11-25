import sys
import sqlite3
import os
import pytest

sys.path.insert(0, "src")

from database import PronunciationDatabase


class TestPronunciationDatabase:
    def test_database_initialization(self):
        db = PronunciationDatabase()
        assert db.connection is not None
        assert db.cursor is not None

    def test_check_for_language_existing(self):
        db = PronunciationDatabase()
        result = db.check_for_language("german")
        assert result is True

    def test_check_for_language_nonexistent(self):
        db = PronunciationDatabase()
        result = db.check_for_language("nonexistent_language_xyz")
        assert result is False

    def test_list_available_languages(self):
        db = PronunciationDatabase()
        languages = db.list_available_languages()
        assert isinstance(languages, list)
        # At least german should exist
        assert "german" in languages

    def test_retrieve_random_word_single(self):
        db = PronunciationDatabase()
        if db.check_for_language("german"):
            result = db.retrieve_random_word("german", 1)
            if result:
                assert isinstance(result, list)
                assert len(result) <= 1

    def test_retrieve_random_word_multiple(self):
        db = PronunciationDatabase()
        if db.check_for_language("german"):
            result = db.retrieve_random_word("german", 3)
            if result:
                assert isinstance(result, list)
                assert len(result) <= 3

    def test_analyze_data(self):
        db = PronunciationDatabase()
        if db.check_for_language("german"):
            count = db.analyze_data("german")
            assert isinstance(count, int)
            assert count >= 0

    def test_check_for_language_sql_injection_prevention(self):
        db = PronunciationDatabase()
        result = db.check_for_language("german'; DROP TABLE german; --")
        assert result is False

    def test_list_available_languages_returns_only_alpha(self):
        db = PronunciationDatabase()
        languages = db.list_available_languages()
        for lang in languages:
            assert lang.isalpha(), f"Language '{lang}' should only contain alphabetic characters"
