"""Tests for command-line argument parsing."""

import sys

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
        args = arg_parser.parser.parse_args(["-r", "-l", "german", "-n", "5"])
        assert args.random is True
        assert args.language == "german"
        assert args.number == 5

    def test_parse_analyze_argument(self):
        """Test parsing of --analyze argument."""
        arg_parser = ArgumentParsing()
        args = arg_parser.parser.parse_args(["-a", "-l", "german"])
        assert args.analyze is True
        assert args.language == "german"

    def test_parse_version_argument(self):
        """Test parsing of --version argument."""
        arg_parser = ArgumentParsing()
        args = arg_parser.parser.parse_args(["-v"])
        assert args.version is True

    def test_parse_list_languages_argument(self):
        """Test parsing of --list-languages argument."""
        arg_parser = ArgumentParsing()
        args = arg_parser.parser.parse_args(["-e"])
        assert args.list_languages is True

    def test_parse_debug_argument(self):
        """Test parsing of --debug argument."""
        arg_parser = ArgumentParsing()
        args = arg_parser.parser.parse_args(["-d"])
        assert args.debug is True

    def test_parse_scrape_argument(self):
        """Test parsing of --scrape argument."""
        arg_parser = ArgumentParsing()
        args = arg_parser.parser.parse_args(["-s", "-l", "german"])
        assert args.scrape is True
        assert args.language == "german"

    def test_parse_backup_argument(self):
        """Test parsing of --backup argument."""
        arg_parser = ArgumentParsing()
        args = arg_parser.parser.parse_args(["-b"])
        assert args.backup is True

    def test_parse_quiet_argument(self):
        """Test parsing of --quiet argument."""
        arg_parser = ArgumentParsing()
        args = arg_parser.parser.parse_args(["-q"])
        assert args.quiet is True
        assert args.verbose is False

    def test_parse_verbose_argument(self):
        """Test parsing of --verbose argument."""
        arg_parser = ArgumentParsing()
        args = arg_parser.parser.parse_args(["--verbose"])
        assert args.verbose is True
        assert args.quiet is False

    def test_parse_clean_argument(self):
        """Test parsing of --clean argument."""
        arg_parser = ArgumentParsing()
        args = arg_parser.parser.parse_args(["-C", "-l", "german"])
        assert args.clean is True

    def test_parse_revert_argument(self):
        """Test parsing of --revert argument."""
        arg_parser = ArgumentParsing()
        args = arg_parser.parser.parse_args(["-R", "-l", "german"])
        assert args.revert is True

    def test_parse_good_argument(self):
        """Test parsing of --good argument."""
        arg_parser = ArgumentParsing()
        args = arg_parser.parser.parse_args(["-g", "-l", "german"])
        assert args.good is True

    def test_parse_set_language_argument(self):
        """Test parsing of --set-language argument."""
        arg_parser = ArgumentParsing()
        args = arg_parser.parser.parse_args(["-k", "spanish"])
        assert args.set_language == "spanish"

    def test_parse_set_number_argument(self):
        """Test parsing of --set-number argument."""
        arg_parser = ArgumentParsing()
        args = arg_parser.parser.parse_args(["-m", "10"])
        assert args.set_number == 10

    def test_parse_input_output_arguments(self):
        """Test parsing of --input and --output arguments."""
        arg_parser = ArgumentParsing()
        args = arg_parser.parser.parse_args(["-f", "input.txt", "-o", "output.txt", "-l", "german"])
        assert args.input == "input.txt"
        assert args.output == "output.txt"

    def test_parse_ipa_wikipedia_argument(self):
        """Test parsing of --ipa-wikipedia argument."""
        arg_parser = ArgumentParsing()
        args = arg_parser.parser.parse_args(["-i"])
        assert args.ipa_wikipedia is True

    def test_parse_confirm_clean_argument(self):
        """Test parsing of --confirm-clean argument."""
        arg_parser = ArgumentParsing()
        args = arg_parser.parser.parse_args(["-c", "-l", "german"])
        assert args.confirm_clean is True

    def test_empty_arguments(self):
        """Test parsing with no arguments."""
        arg_parser = ArgumentParsing()
        args = arg_parser.parser.parse_args([])
        assert args.random is False
        assert args.analyze is False
        assert args.version is False
