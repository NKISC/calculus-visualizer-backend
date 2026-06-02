"""Pydantic schemas for the compute endpoint."""

from typing import Any

from pydantic import BaseModel, Field

from app.schemas.common import ErrorDetail, MathResult, OutputPaths, RenderOptions, TaskType


class ComputationParameters(BaseModel):
    """Optional parameters for future symbolic and numerical computation."""

    x_range: list[float] | None = Field(
        default=None,
        description="Optional x-domain for future sampling or plotting.",
    )
    y_range: list[float] | None = Field(
        default=None,
        description="Optional y-domain for future multivariable sampling.",
    )
    z_range: list[float] | None = Field(
        default=None,
        description="Optional z-domain for future 3D vector field work.",
    )
    sample_density: int | None = Field(
        default=None,
        description="Future number of samples per axis.",
    )
    lower_bound: float | None = Field(
        default=None,
        description="Future lower integration bound.",
    )
    upper_bound: float | None = Field(
        default=None,
        description="Future upper integration bound.",
    )
    extra: dict[str, Any] | None = Field(
        default=None,
        description="Reserved for future task-specific options.",
    )


class ComputeInput(BaseModel):
    """Echo of the input fields most relevant to frontend display."""

    expression: str | None
    vector_field: list[str] | None
    variables: list[str]


class ComputeRequest(BaseModel):
    """Request contract for POST /api/compute."""

    task_id: str = Field(description="Frontend-provided task identifier.")
    task_type: TaskType = Field(description="Future calculus task to perform.")
    expression: str | None = Field(
        default=None,
        description="Expression string for scalar calculus tasks.",
    )
    vector_field: list[str] | None = Field(
        default=None,
        description="Vector field components for vector calculus tasks.",
    )
    variables: list[str] = Field(
        default_factory=list,
        description="Variables used by the expression or vector field.",
    )
    parameters: ComputationParameters = Field(
        default_factory=ComputationParameters,
        description="Optional computation settings.",
    )
    render_options: RenderOptions = Field(
        default_factory=RenderOptions,
        description="Optional render request hints.",
    )


class ComputeResponse(BaseModel):
    """Response contract for POST /api/compute."""

    success: bool
    task_id: str
    task_type: TaskType
    input: ComputeInput
    math_result: MathResult
    outputs: OutputPaths
    error: ErrorDetail | None = None
