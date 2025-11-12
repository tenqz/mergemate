"""Unit tests for the CLI interface contract."""

import pytest

from mentra.cli.application.interfaces.cli_interface import CLIInterface

# === ARRANGE HELPERS ===

class _InvalidCLI(CLIInterface):
    """CLI missing required `run` implementation."""

    pass


class _ValidCLI(CLIInterface):
    """CLI implementing `run` contract correctly."""

    def __init__(self, exit_code: int) -> None:
        self._exit_code = exit_code

    def run(self) -> int:
        return self._exit_code


# === TESTS ===

def test_cli_interface_run_is_marked_abstract() -> None:
    """Ensure `run` is abstract at the interface level."""
    # Arrange
    method = getattr(CLIInterface, "run", None)

    # Act
    is_abstract = getattr(method, "__isabstractmethod__", False)

    # Assert
    assert is_abstract is True


def test_cli_interface_requires_run_implementation() -> None:
    """Ensure subclasses without `run` cannot be instantiated."""
    # Arrange / Act / Assert
    with pytest.raises(TypeError) as error:
        _InvalidCLI()

    assert "run" in str(error.value)


def test_cli_interface_run_contract_with_implementation() -> None:
    """Ensure valid CLI implementations return expected exit code."""
    # Arrange
    expected_exit_code = 0
    cli = _ValidCLI(exit_code=expected_exit_code)

    # Act
    result = cli.run()

    # Assert
    assert result == expected_exit_code