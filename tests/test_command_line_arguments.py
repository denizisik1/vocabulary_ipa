"""Tests for command-line argument parsing."""

import sys
import pytest

sys.path.insert(0, "src")

from command_line_arguments import ArgumentParsing


class TestArgumentParsing:
    """Tests for the ArgumentParsing class."""

    def test_argument_parsing_initialization(self):
        """Test that ArgumentParsing initializes correctly."""
        arg_parser = ArgumentParsing()
        assert arg_parser.parser is not None
        assert arg_parser.parser.prog == "LanguagePronunciationScraper"

    def test_parse_random_arguments(self):
        """Test parsing of --random, --language, and --number arguments."""
        arg_parser = ArgumentParsing()
        # Simulate command line arguments
        sys.argv = ["prog", "-r", "-l", "german", "-n", "5"]
        args = arg_parser.parse_arguments()
        assert args.random is True
        assert args.language == "german"
        assert args.number == 5

    def test_parse_analyze_argument(self):
        """Test parsing of --analyze argument."""
        arg_parser = ArgumentParsing()
        sys.argv = ["prog", "-a", "-l", "german"]
        args = arg_parser.parse_arguments()
        assert args.analyze is True
        assert args.language == "german"

    def test_parse_version_argument(self):
        """Test parsing of --version argument."""
        arg_parser = ArgumentParsing()
        sys.argv = ["prog", "-v"]
        args = arg_parser.parse_arguments()
        assert args.version is True

    def test_parse_list_languages_argument(self):
        """Test parsing of --list-languages argument."""
        arg_parser = ArgumentParsing()
        sys.argv = ["prog", "-e"]
        args = arg_parser.parse_arguments()
        assert args.list_languages is True

    def test_parse_debug_argument(self):
        """Test parsing of --debug argument."""
        arg_parser = ArgumentParsing()
        sys.argv = ["prog", "-d"]
        args = arg_parser.parse_arguments()
        assert args.debug is True

    def test_parse_scrape_argument(self):
        """Test parsing of --scrape argument."""
        arg_parser = ArgumentParsing()
        sys.argv = ["prog", "-s", "-l", "german"]
        args = arg_parser.parse_arguments()
        assert args.scrape is True
        assert args.language == "german"

    def test_parse_backup_argument(self):
        """Test parsing of --backup argument."""
        arg_parser = ArgumentParsing()
        sys.argv = ["prog", "-b"]
        args = arg_parser.parse_arguments()
        assert args.backup is True

    def test_parse_quiet_argument(self):
        """Test parsing of --quiet argument."""
        arg_parser = ArgumentParsing()
        sys.argv = ["prog", "-q"]
        args = arg_parser.parse_arguments()
        assert args.quiet is True
        assert args.verbose is False

    def test_parse_verbose_argument(self):
        """Test parsing of --verbose argument."""
        arg_parser = ArgumentParsing()
        sys.argv = ["prog", "--verbose"]
        args = arg_parser.parse_arguments()
        assert args.verbose is True
        assert args.quiet is False

    def test_parse_clean_argument(self):
        """Test parsing of --clean argument."""
        arg_parser = ArgumentParsing()
        sys.argv = ["prog", "-C", "-l", "german"]
        args = arg_parser.parse_arguments()
        assert args.clean is True

    def test_parse_revert_argument(self):
        """Test parsing of --revert argument."""
        arg_parser = ArgumentParsing()
        sys.argv = ["prog", "-R", "-l", "german"]
        args = arg_parser.parse_arguments()
        assert args.revert is True

    def test_parse_good_argument(self):
        """Test parsing of --good argument."""
        arg_parser = ArgumentParsing()
        sys.argv = ["prog", "-g", "-l", "german"]
        args = arg_parser.parse_arguments()
        assert args.good is True

    def test_parse_set_language_argument(self):
        """Test parsing of --set-language argument."""
        arg_parser = ArgumentParsing()
        sys.argv = ["prog", "-k", "spanish"]
        args = arg_parser.parse_arguments()
        assert args.set_language == "spanish"

    def test_parse_set_number_argument(self):
        """Test parsing of --set-number argument."""
        arg_parser = ArgumentParsing()
        sys.argv = ["prog", "-m", "10"]
        args = arg_parser.parse_arguments()
        assert args.set_number == 10

    def test_parse_input_output_arguments(self):
        """Test parsing of --input and --output arguments."""
        arg_parser = ArgumentParsing()
        sys.argv = ["prog", "-f", "input.txt", "-o", "output.txt", "-l", "german"]
        args = arg_parser.parse_arguments()
        assert args.input == "input.txt"
        assert args.output == "output.txt"

    def test_parse_ipa_wikipedia_argument(self):
        """Test parsing of --ipa-wikipedia argument."""
        arg_parser = ArgumentParsing()
        sys.argv = ["prog", "-i"]
        args = arg_parser.parse_arguments()
        assert args.ipa_wikipedia is True

    def test_parse_confirm_clean_argument(self):
        """Test parsing of --confirm-clean argument."""
        arg_parser = ArgumentParsing()
        sys.argv = ["prog", "-c", "-l", "german"]
        args = arg_parser.parse_arguments()
        assert args.confirm_clean is True

    def test_empty_arguments(self):
        """Test parsing with no arguments."""
        arg_parser = ArgumentParsing()
        sys.argv = ["prog"]
        args = arg_parser.parse_arguments()
        assert args.random is False
        assert args.analyze is False
        assert args.version is False
