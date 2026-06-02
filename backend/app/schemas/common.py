"""Shared Pydantic models for API contracts."""

from typing import Any, Literal

from pydantic import BaseModel, Field


TaskType = Literal["derivative", "integral", "gradient", "divergence", "curl"]
RenderQuality = Literal["low", "medium", "high"]
RenderFormat = Literal["mp4", "png", "gif"]


class ErrorDetail(BaseModel):
    """Structured error payload returned by future failed operations."""

    code: str | None = Field(default=None, description="Optional machine-readable code.")
    message: str = Field(description="Human-readable error message.")
    details: dict[str, Any] | None = Field(
        default=None,
        description="Optional context for debugging or frontend display.",
    )


class HealthResponse(BaseModel):
    """Response returned by GET /api/health."""

    success: bool
    message: str
    version: str


class RenderOptions(BaseModel):
    """Options that control future rendering behavior."""

    render: bool = Field(
        default=False,
        description="Whether the frontend is requesting rendered media.",
    )
    quality: RenderQuality = Field(
        default="low",
        description="Future Manim quality preset.",
    )
    format: RenderFormat = Field(
        default="mp4",
        description="Desired output format for future rendered media.",
    )


class OutputPaths(BaseModel):
    """Paths to generated artifacts.

    Values are null during the skeleton phase because no files are generated.
    """

    video_path: str | None = None
    image_path: str | None = None
    data_path: str | None = None


class MathResult(BaseModel):
    """Container for future symbolic and numerical computation outputs."""

    latex: str | None = Field(
        default=None,
        description="LaTeX representation of the input expression or field.",
    )
    result_text: str | None = Field(
        default=None,
        description="Plain-text result for future calculus computation.",
    )
    result_latex: str | None = Field(
        default=None,
        description="LaTeX result for future calculus computation.",
    )
    numeric_data: dict[str, Any] | list[Any] | None = Field(
        default=None,
        description="Future sampled data for visualization.",
    )
