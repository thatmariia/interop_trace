"""Regression tests for stable starter behavior."""

from interop_trace.services.processing import process_text


def test_processing_regression_uppercase_output():
    """Ensure starter processing keeps its documented output."""
    result = process_text("Research Software")

    assert result.output_text == "RESEARCH SOFTWARE"
