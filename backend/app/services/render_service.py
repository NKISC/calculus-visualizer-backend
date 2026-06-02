"""Render service skeleton.

This module will eventually prepare and submit Manim rendering tasks. The
current implementation intentionally avoids invoking Manim.
"""

from app.schemas.common import OutputPaths
from app.schemas.render import RenderRequest, RenderResponse


class RenderService:
    """Coordinates future Manim render task preparation."""

    def create_placeholder_response(self, request: RenderRequest) -> RenderResponse:
        """Return placeholder render queue status without rendering media."""

        # TODO: Validate render_options against supported Manim output presets.
        # TODO: Ask render_engine.render_manager to prepare the correct scene.
        # TODO: Return generated output paths after actual rendering exists.
        return RenderResponse(
            success=True,
            task_id=request.task_id,
            status="queued",
            outputs=OutputPaths(),
            error=None,
        )
