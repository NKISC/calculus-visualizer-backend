"""Compute service skeleton.

The service layer will eventually route validated compute requests to the
appropriate math engine module. For now it only returns a documented placeholder
response so the API contract can be exercised by the frontend.
"""

from app.schemas.common import MathResult, OutputPaths
from app.schemas.compute import ComputeInput, ComputeRequest, ComputeResponse


class ComputeService:
    """Coordinates future symbolic computation and visualization data creation."""

    def create_placeholder_response(self, request: ComputeRequest) -> ComputeResponse:
        """Return the current skeleton response without performing math."""

        # TODO: Route request.task_type to math_engine modules.
        # TODO: Populate MathResult with SymPy and NumPy outputs.
        # TODO: Trigger render service when request.render_options.render is true.
        return ComputeResponse(
            success=True,
            task_id=request.task_id,
            task_type=request.task_type,
            input=ComputeInput(
                expression=request.expression,
                vector_field=request.vector_field,
                variables=request.variables,
            ),
            math_result=MathResult(),
            outputs=OutputPaths(),
            error=None,
        )
