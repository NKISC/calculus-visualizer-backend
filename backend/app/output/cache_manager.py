"""Cache management placeholder.

Future responsibility:
- Decide whether previously generated outputs can be reused.
- Clear stale generated files when needed.
- Keep cache policy separate from math and render logic.
"""


class CacheManager:
    """Placeholder for future cache strategy."""

    def lookup(self, cache_key: str) -> str | None:
        """Return a future cached output path for cache_key."""

        # TODO: Implement cache lookup after output file naming is stable.
        raise NotImplementedError("Cache lookup is not implemented yet.")
