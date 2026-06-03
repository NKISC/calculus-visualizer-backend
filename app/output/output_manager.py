"""Output directory management placeholder.

Future responsibility:
- Ensure output directories exist.
- Return normalized paths for generated videos, images, data, and logs.
"""

from pathlib import Path


class OutputManager:
    """Placeholder for future output directory coordination."""

    def __init__(self, base_dir: Path) -> None:
        self.base_dir = base_dir

    def prepare_output_directories(self) -> None:
        """Prepare output folders for future generated artifacts."""

        # TODO: Create and validate output folders when generation is added.
        raise NotImplementedError("Output directory management is not implemented yet.")
