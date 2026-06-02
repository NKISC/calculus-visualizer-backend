"""Pydantic schemas for the render endpoint."""

from typing import Literal

from pydantic import BaseModel, Field

from app.schemas.common import ErrorDetail, MathResult, OutputPaths, RenderOptions, TaskType


RenderStatus = Literal["queued", "running", "completed", "failed"]


class RenderRequest(BaseModel):
    """Request contract for POST /api/render."""

    task_id: str = Field(description="Frontend-provided task identifier.")
    task_type: TaskType = Field(description="Type of visualization to render.")
    math_result: MathResult = Field(
        description="Future computation result used to prepare a Manim scene.",
    )
    render_options: RenderOptions = Field(
        default_factory=RenderOptions,
        description="Requested render quality and format.",
    )


class RenderResponse(BaseModel):
    """Response contract for POST /api/render."""

    success: bool
    task_id: str
    status: RenderStatus
    outputs: OutputPaths
    error: ErrorDetail | None = None
