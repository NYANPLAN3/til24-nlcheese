"""NLP Manager."""

import logging

from .cheese import cheese_heading, cheese_target, cheese_tool
from .structs import CommandJSON

__all__ = ["NLPManager"]

log = logging.getLogger(__name__)


class NLPManager:
    """NLP Manager."""

    def __init__(self):
        """Init."""
        pass

    def extract(self, transcript: str) -> CommandJSON:
        """Extract JSON command."""
        # Pre-processing.
        # transcript = cheese_filter_transcript(transcript)
        heading = cheese_heading(transcript)
        tool = cheese_tool(transcript)
        target = cheese_target(tool, transcript)
        return {"heading": heading, "tool": tool, "target": target}
