"""Integration tests for generated interface adapters."""

import pytest

from interop_trace.services.processing import process_text


def test_service_integration_path_processes_text():
    """Ensure the reusable service path behaves consistently."""
    assert process_text("abc").output_text == "ABC"


def test_cli_application_processes_a_command():
    """Ensure the installed CLI surface reaches the service layer."""
    pytest.importorskip("typer")
    from typer.testing import CliRunner

    from interop_trace.adapters.cli.app import app

    result = CliRunner().invoke(app, ["process", "abc"])

    assert result.exit_code == 0
    assert result.stdout.strip() == "ABC"


