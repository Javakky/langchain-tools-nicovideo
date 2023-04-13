"""Tool for the Nicovideo Snapshot Search API."""

from langchain.tools.base import BaseTool

from langchain_tools_nicovideo.utilities.nicovideo_snapshot_api import (
    NicovideoSnapshotApiWrapper,
)


class NicovideoQueryRun(BaseTool):
    """Tool that adds the capability to search using the Nicovideo Snapshot Search API."""

    name = "NicoVideo"
    description = (
        "A wrapper around Nicovideo. "
        "The site is deeply involved in otaku culture. "
        "and can retrieve video titles (title), descriptions (description), and play counts (viewCounter). "
        "Be sure to use the prefix 'Search query: '. Search results are returned in Json format."
    )
    api_wrapper: NicovideoSnapshotApiWrapper

    def _run(self, query: str) -> str:
        """Use the Nicovideo tool."""
        return self.api_wrapper.run(query)

    async def _arun(self, query: str) -> str:
        """Use the Nicovideo tool asynchronously."""
        # TODO
        raise NotImplementedError("NicovideoQueryRun")
