"""Infrastructure service wrapping the eventsourcing Application."""

from eventsourcing.application import Application

from mentra.cli.domain.cli_aggregate import CLICommand


class CLIEventStore(Application):
    """Event sourcing application for storing CLI command events."""

    def record_command(self, command: str, args: list[str]):
        """Save an incoming CLI command to the event store."""
        cli_command = self.save_new(command, args)
        return cli_command

    def save_new(self, command: str, args: list[str]):
        """Create and persist a new aggregate instance."""
        cli_cmd = CLICommand(command=command, args=args)
        self.save(cli_cmd)
        return cli_cmd
