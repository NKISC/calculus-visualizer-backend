"""Render endpoint skeleton.

This route accepts future render requests and delegates placeholder task status
creation to the render service. It does not run Manim yet.
"""

from fastapi import APIRouter

from app.schemas.render import RenderRequest, RenderResponse
from app.services.render_service import RenderService


router = APIRouter(tags=["render"])
render_service = RenderService()


@router.post("/render", response_model=RenderResponse)
async def render(request: RenderRequest) -> RenderResponse:
    """Receive a future render task and return placeholder queue status."""

    return render_service.create_placeholder_response(request)
