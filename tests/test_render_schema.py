"""Schema tests for render request contracts."""

from app.schemas.render import RenderRequest


def test_render_request_accepts_placeholder_math_result() -> None:
    """The render request example shape should validate through Pydantic."""

    request = RenderRequest(
        task_id="task_001",
        task_type="gradient",
        math_result={
            "latex": "x^{2} + y^{2}",
            "result_text": "<2*x, 2*y>",
            "result_latex": "\\langle 2x, 2y \\rangle",
            "numeric_data": None,
        },
        render_options={
            "render": True,
            "quality": "low",
            "format": "mp4",
        },
    )

    assert request.task_id == "task_001"
    assert request.render_options.render is True
