"""Typer command-line application for Interop Trace.

The CLI adapter translates command-line input into calls to reusable project
services. Command modules stay small so they are easy to test separately from
terminal formatting.
"""

import typer

from interop_trace.adapters.cli.commands import process

# The Typer app is the command registry. Add new commands by importing their
# modules and registering them below.
app = typer.Typer(
    help="Tracing interoperability across bioinformatics databases and workflows."
)


@app.callback()
def callback() -> None:
    """Provide the parent command for the CLI subcommands."""


app.command(name="process")(process.command)


def main() -> None:
    """Run the command-line application."""
    app()
