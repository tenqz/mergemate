"""Mentra CLI entry point module.

This module provides the entry class for the command-line interface (CLI).
It handles argument parsing and emits domain events.
"""

import sys

from mentra.cli.application.interfaces.cli_interface import CLIInterface
from mentra.cli.infrastructure.cli_event_store import CLIEventStore


class CLIApp(CLIInterface):
    """CLI application wrapper for Mentra commands."""

    def __init__(
        self,
        argv: list[str] | None = None,
        event_store: CLIEventStore | None = None,
    ) -> None:
        """Initialize CLIApp.

        Args:
            argv (list[str] | None): Optional list of arguments to parse.
            event_store (CLIEventStore | None): Optional event sourcing store.

        """
        self.argv = argv or sys.argv[1:]
        self.event_store = event_store or CLIEventStore()

    def run(self) -> int:
        """Run the CLI application.

        Parses arguments and emits an event for the received command.
        """
        if not self.argv:
            print("No command provided.")
            return 1

        command = self.argv[0]
        args = self.argv[1:]

        # Record domain event
        self.event_store.record_command(command, args)

        return 0

if __name__ == "__main__":
    app = CLIApp()
    app.run()