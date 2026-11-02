"""Tests for the main module."""
from main import main


def test_main_prints_greeting(capsys):
    """Test that the main function prints the correct greeting."""
    main()

    captured = capsys.readouterr()
    assert captured.out == "Hello from fde!\n"
    assert captured.err == ""
