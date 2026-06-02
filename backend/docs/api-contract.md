# API Contract

Base path:

```text
/api
```

This API contract is prepared for frontend integration. The current backend returns placeholder responses only.

## Endpoints

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/api/health` | Check whether the backend server is running. |
| POST | `/api/compute` | Validate and route a future calculus computation request. |
| POST | `/api/render` | Validate and queue a future Manim render request. |

## GET /api/health

Example response:

```json
{
  "success": true,
  "message": "Calculus Visualizer backend is running.",
  "version": "0.1.0"
}
```

## POST /api/compute

Purpose:

- Receive a mathematical task.
- Validate request format.
- Route the task to the correct future math engine.
- Return placeholder response for now.

Example request:

```json
{
  "task_id": "task_001",
  "task_type": "gradient",
  "expression": "x**2 + y**2",
  "vector_field": null,
  "variables": ["x", "y"],
  "parameters": {
    "x_range": [-3, 3],
    "y_range": [-3, 3],
    "sample_density": 15,
    "lower_bound": null,
    "upper_bound": null
  },
  "render_options": {
    "render": false,
    "quality": "low",
    "format": "mp4"
  }
}
```

Example placeholder response:

```json
{
  "success": true,
  "task_id": "task_001",
  "task_type": "gradient",
  "input": {
    "expression": "x**2 + y**2",
    "vector_field": null,
    "variables": ["x", "y"]
  },
  "math_result": {
    "latex": null,
    "result_text": null,
    "result_latex": null,
    "numeric_data": null
  },
  "outputs": {
    "video_path": null,
    "image_path": null,
    "data_path": null
  },
  "error": null
}
```

## POST /api/render

Purpose:

- Receive a render request.
- Prepare a future Manim rendering task.
- Return placeholder status or output path.
- Avoid actual Manim rendering until the render engine is implemented.

Example request:

```json
{
  "task_id": "task_001",
  "task_type": "gradient",
  "math_result": {
    "latex": "x^{2} + y^{2}",
    "result_text": "<2*x, 2*y>",
    "result_latex": "\\langle 2x, 2y \\rangle",
    "numeric_data": null
  },
  "render_options": {
    "render": true,
    "quality": "low",
    "format": "mp4"
  }
}
```

Example placeholder response:

```json
{
  "success": true,
  "task_id": "task_001",
  "status": "queued",
  "outputs": {
    "video_path": null,
    "image_path": null,
    "data_path": null
  },
  "error": null
}
```

## task_type Definitions

| task_type | Future meaning |
| --- | --- |
| `derivative` | Differentiate a scalar expression with respect to one variable. |
| `integral` | Integrate a scalar expression, optionally with bounds. |
| `gradient` | Compute the gradient vector of a scalar field. |
| `divergence` | Compute divergence of a vector field. |
| `curl` | Compute curl of a vector field. |

## Expression Format Rules

Planned expression rules:

- Expressions should be strings.
- Use Python-style operators compatible with future SymPy parsing.
- Use `**` for powers, for example `x**2`.
- Variables must be listed in the `variables` array.
- Frontend should avoid sending raw user input that has not been reviewed or sanitized.

Examples:

```text
x**2 + y**2
sin(x)
x**3 + 2*x
```

## Vector Field Format Rules

Planned vector field rules:

- Vector fields should be arrays of component strings.
- Each component should follow the expression format rules.
- The number of components should match the intended dimension.
- Variables should be listed in the `variables` array.

Examples:

```json
["x", "y"]
["-y", "x", "0"]
```

## Error Response Format

Future failed operations should return an `error` object:

```json
{
  "success": false,
  "error": {
    "code": "unsupported_task_type",
    "message": "The requested task type is not supported.",
    "details": {
      "task_type": "laplacian"
    }
  }
}
```

FastAPI validation errors may use FastAPI's default validation response shape unless a custom exception handler is added later.

## Frontend Integration Notes

- Treat `task_id` as the stable identifier for a frontend request.
- Expect placeholder `math_result` values to be `null` until computation is implemented.
- Expect output paths to be `null` until rendering and data generation are implemented.
- Use `/api/health` before making compute or render requests during local development.
- Use `/docs` to inspect the generated OpenAPI schema while contracts evolve.
