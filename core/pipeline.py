"""
Public portfolio edition.

Core orchestration implementation is intentionally omitted from the public release.
See docs/public/IMPLEMENTATION_PATTERNS_EN_JA.md for architecture and method details.
"""

from typing import Any, AsyncIterator, Dict


class AgentPipeline:
    """Public stub for portfolio distribution."""

    def run(
        self,
        query: str,
        session_id: str,
        language: str = "中文",
        enable_deep_thinking: bool = False,
        enable_web_search: bool = False,
    ) -> Dict[str, Any]:
        raise NotImplementedError(
            "Core orchestration is private in the public portfolio edition."
        )

    async def run_streaming(
        self,
        query: str,
        session_id: str,
        language: str = "中文",
        enable_deep_thinking: bool = False,
        enable_web_search: bool = False,
    ) -> AsyncIterator[Dict[str, Any]]:
        raise NotImplementedError(
            "Core orchestration is private in the public portfolio edition."
        )


pipeline = AgentPipeline()

