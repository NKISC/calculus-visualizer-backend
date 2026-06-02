# Calculus Visualizer Backend

Local FastAPI backend for the Calculus Visualizer project.

This backend will eventually coordinate symbolic calculus computation, numerical sampling, visualization data generation, and Manim render task management. The frontend will be built separately and will call this backend through JSON APIs.

## Current Status

This project is currently an architecture skeleton only.

- FastAPI app structure is prepared.
- Pydantic request and response schemas are defined.
- API endpoints return placeholder responses.
- Math engine and render engine files contain TODO stubs only.
- No real derivative, integral, gradient, divergence, curl, sampling, or Manim rendering logic has been implemented yet.

## Backend Responsibility

The backend is responsible for:

- Receiving computation and render requests from the frontend.
- Validating request payloads with Pydantic.
- Routing future calculus tasks to the correct service and engine modules.
- Returning JSON responses and generated output file paths.
- Managing local output folders for future videos, images, data files, and logs.

The backend is not responsible for frontend UI code, authentication, user accounts, database storage, or cloud deployment at this stage.

## Setup

From the `backend` folder:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run The Development Server

```bash
uvicorn main:app --reload
```

After the server starts, the interactive API docs should be available at:

```text
http://127.0.0.1:8000/docs
```

The health endpoint is available at:

```text
http://127.0.0.1:8000/api/health
```

## Run Tests

```bash
pytest
```

The current tests are lightweight schema and skeleton checks. They are placeholders for future behavior tests.

## Folder Structure

```text
backend/
├── main.py
├── app/
│   ├── api/              # FastAPI routers and HTTP endpoints
│   ├── core/             # Configuration, errors, and logging setup
│   ├── schemas/          # Pydantic API contracts
│   ├── services/         # Coordination between API, math engine, rendering, and outputs
│   ├── math_engine/      # Future SymPy and NumPy calculus logic
│   ├── render_engine/    # Future Manim render task management
│   ├── output/           # Future output path, cache, and file naming helpers
│   └── utils/            # Shared utility helpers
├── outputs/              # Future generated videos, images, data, and logs
├── examples/             # Example request payloads
├── docs/                 # Architecture and API documentation
└── tests/                # Future pytest suite
```

## API Overview

- `GET /api/health`
- `POST /api/compute`
- `POST /api/render`

See `docs/api-contract.md` for request and response examples.
