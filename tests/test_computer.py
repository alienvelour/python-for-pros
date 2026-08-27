import pytest
from pydantic import ValidationError

from lesson_03_testing.computer import Computer


def test_computer_valid() -> None:
    computer = Computer(brand="apple", ram_gb=16, hard_drive_gb=512)
    assert computer.brand == "apple"
    assert computer.ram_gb == 16
    assert computer.hard_drive_gb == 512


def test_computer_rejects_string_ram() -> None:
    with pytest.raises(ValidationError):
        Computer(brand="apple", ram_gb="sixteen", hard_drive_gb=512)  # type: ignore[arg-type]


def test_computer_requires_brand() -> None:
    with pytest.raises(ValidationError):
        Computer(ram_gb=16, hard_drive_gb=512)  # type: ignore[call-arg]
