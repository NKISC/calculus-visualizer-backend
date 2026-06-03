"""Schema tests for compute request and response contracts."""

from app.schemas.compute import ComputeRequest


def test_compute_request_accepts_gradient_example() -> None:
    """The gradient example shape should validate through Pydantic."""

    request = ComputeRequest(
        task_id="task_001",
        task_type="gradient",
        expression="x**2 + y**2",
        vector_field=None,
        variables=["x", "y"],
        parameters={
            "x_range": [-3, 3],
            "y_range": [-3, 3],
            "sample_density": 15,
            "lower_bound": None,
            "upper_bound": None,
        },
        render_options={
            "render": False,
            "quality": "low",
            "format": "mp4",
        },
    )

    assert request.task_type == "gradient"
    assert request.expression == "x**2 + y**2"
