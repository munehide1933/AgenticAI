from .models import *  # noqa: F401,F403

__all__ = ["pipeline"]


def __getattr__(name: str):
    if name == "pipeline":
        from .pipeline import pipeline

        return pipeline
    raise AttributeError(f"module 'core' has no attribute '{name}'")
