# Backend Architecture

## Purpose

The Calculus Visualizer backend is a local computation and rendering service for a future frontend application. It receives JSON requests, validates them, coordinates future calculus processing, prepares future visualization data, and returns JSON responses with result fields and generated file paths.

This version is an architecture skeleton only. It defines the project boundaries and contracts but does not implement real calculus computation or Manim rendering.

## Layer Architecture

### API Layer

Location: `app/api`

Responsible for:

- HTTP endpoints.
- Request validation through Pydantic schemas.
- Response formatting.
- Routing requests to services.

The API layer should stay thin. It should not contain symbolic math, sampling, file generation, or Manim execution logic.

### Service Layer

Location: `app/services`

Responsible for:

- Coordinating math computation and rendering.
- Routing tasks by `task_type`.
- Calling `math_engine` and `render_engine` modules.
- Keeping API routes clean.

Future compute flow will likely enter `ComputeService`, call parser and calculus modules, request sampling if needed, and optionally pass render instructions to `RenderService`.

### Math Engine Layer

Location: `app/math_engine`

Responsible for future symbolic and numerical computation:

- Expression parsing.
- Derivative computation.
- Integral computation.
- Gradient computation.
- Divergence computation.
- Curl computation.
- Vector field processing.
- Numerical sampling.

SymPy and NumPy work belongs here, not in API routes. This separation keeps math logic testable and prevents HTTP concerns from leaking into calculation code.

### Render Engine Layer

Location: `app/render_engine`

Responsible for future animation rendering:

- Manim scene management.
- Render task preparation.
- Output video and image path generation.
- Render quality settings.

Manim integration belongs behind this layer so future rendering behavior can evolve without changing the API contract.

### Output Layer

Location: `app/output`

Responsible for:

- Output directory management.
- File naming.
- Caching strategy.
- Generated video, image, and data paths.

The output layer should provide predictable paths to services while keeping filesystem details away from math and API modules.

### Utils Layer

Location: `app/utils`

Responsible for small shared helpers such as LaTeX formatting, domain validation, and task ID helpers. Larger behavior should stay in services or engines.

## Request Flow

```text
Frontend
  -> FastAPI route
  -> Pydantic schema validation
  -> Service layer
  -> Future math_engine and/or render_engine calls
  -> Output path preparation
  -> Pydantic response model
  -> Frontend
```

Current skeleton flow:

```text
Frontend
  -> FastAPI route
  -> Pydantic schema validation
  -> Service placeholder response
  -> Frontend
```

## Future Frontend-Backend Interaction

The frontend will send JSON payloads to `/api/compute` and `/api/render`. The backend will respond with:

- `success` status.
- The original `task_id`.
- Placeholder or real math results.
- Optional output paths for videos, images, or data files.
- A structured `error` object when a task fails.

Keeping request and response shapes stable early lets frontend development begin before the math and rendering internals are complete.

## Why FastAPI

FastAPI is a good fit because it provides:

- Typed endpoint definitions.
- Pydantic-based validation.
- Built-in OpenAPI documentation at `/docs`.
- A simple local development workflow with Uvicorn.
- Clean separation between route handlers and service logic.

## Why Separate SymPy, NumPy, And Manim

SymPy, NumPy, and Manim each solve different problems:

- SymPy handles symbolic expressions and calculus.
- NumPy handles numerical sampling for plots and vector fields.
- Manim handles animation rendering.

Keeping them in separate layers makes the backend easier to test, easier to explain, and easier to change. It also lets the frontend consume stable JSON contracts while backend internals are built incrementally.
