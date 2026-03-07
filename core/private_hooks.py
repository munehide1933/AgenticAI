import importlib
import logging
import os
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


class DefaultPrivateHooks:
    """No-op hooks used by the public edition."""

    def enrich_initial_state(self, state: Dict[str, Any]) -> Dict[str, Any]:
        return state

    def after_workflow(self, state: Dict[str, Any]) -> Dict[str, Any]:
        return state

    def mutate_response(
        self, response: Dict[str, Any], *, state: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return response


def load_private_hooks() -> DefaultPrivateHooks:
    """
    Load proprietary hooks from a private package if configured.

    Set AGENTICAI_PRIVATE_HOOKS_MODULE to a module path that exports
    either `get_private_hooks()` or `PrivateHooks`.
    """
    module_path = os.getenv("AGENTICAI_PRIVATE_HOOKS_MODULE", "").strip()
    if not module_path:
        return DefaultPrivateHooks()

    try:
        module = importlib.import_module(module_path)
    except Exception as exc:
        logger.warning("Private hooks module load failed (%s): %s", module_path, exc)
        return DefaultPrivateHooks()

    # Pattern 1: factory function
    factory = getattr(module, "get_private_hooks", None)
    if callable(factory):
        try:
            hooks = factory()
            if hooks is not None:
                logger.info("Private hooks loaded from %s via get_private_hooks()", module_path)
                return hooks
        except Exception as exc:
            logger.warning("get_private_hooks() failed for %s: %s", module_path, exc)

    # Pattern 2: class with default constructor
    hooks_cls = getattr(module, "PrivateHooks", None)
    if hooks_cls is not None:
        try:
            hooks = hooks_cls()
            logger.info("Private hooks loaded from %s via PrivateHooks", module_path)
            return hooks
        except Exception as exc:
            logger.warning("PrivateHooks init failed for %s: %s", module_path, exc)

    logger.warning(
        "Private hooks module %s found but no compatible export was detected",
        module_path,
    )
    return DefaultPrivateHooks()

