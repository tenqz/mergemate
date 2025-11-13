"""Domain aggregate describing CLI command events."""

from eventsourcing.domain import Aggregate, event


class CLICommand(Aggregate):
    """Aggregate root representing a CLI command event source."""

    @event("Received")
    def __init__(self, command: str, args: list[str]):
        """Persist the incoming CLI command payload."""
        self.command = command
        self.args = args
