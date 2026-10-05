"""Runtime entry point for ``python -m interop_trace``.

This module provides a tiny package-level command for quick smoke tests. Keep
larger runtime interfaces in dedicated modules.
"""

from interop_trace.services.processing import process_text


def main(text: str = "Interop Trace") -> None:
    """Run the package entry point.

    Parameters
    ----------
    text : str, default="Interop Trace"
        Text to process.
    """
    # Delegate to the service layer so the entry point stays small and
    # testable.
    result = process_text(text)
    print(result.output_text)


if __name__ == "__main__":
    main()
