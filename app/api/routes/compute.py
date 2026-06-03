"""Compute endpoint skeleton.

This route validates request shape and delegates placeholder response creation
to the service layer. It does not perform calculus yet.
"""

from fastapi import APIRouter

from app.schemas.compute import ComputeRequest, ComputeResponse
from app.services.compute_service import ComputeService


router = APIRouter(tags=["compute"])
compute_service = ComputeService()


@router.post("/compute", response_model=ComputeResponse)
async def compute(request: ComputeRequest) -> ComputeResponse:
    """Receive a future calculus task and return a placeholder response."""

    return compute_service.create_placeholder_response(request)
