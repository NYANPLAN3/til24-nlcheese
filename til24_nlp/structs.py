"""Types."""

from typing import TypedDict

__all__ = ["CommandJSON"]


class CommandJSON(TypedDict):
    """Actual competition schema."""

    heading: str
    tool: str
    target: str
