"""Task service placeholder.

Future rendering may need task status tracking for queued, running, completed,
or failed jobs. Keep this file minimal until actual asynchronous rendering is
introduced.
"""


class TaskService:
    """Placeholder for future task lifecycle management."""

    def register_task(self, task_id: str, task_type: str) -> None:
        """Register a future compute or render task.

        TODO: Store task metadata when task tracking is implemented.
        """

        raise NotImplementedError("Task tracking is not implemented yet.")
