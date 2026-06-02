"""Output file naming placeholder.

Future responsibility:
- Produce stable filenames from task_id, task_type, format, and timestamp.
- Avoid leaking raw expressions into filenames.
"""


def build_output_filename(task_id: str, task_type: str, extension: str) -> str:
    """Build a future generated output filename."""

    # TODO: Add safe file naming once output generation exists.
    raise NotImplementedError("Output file naming is not implemented yet.")
