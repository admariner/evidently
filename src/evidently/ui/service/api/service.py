import os
from typing import Optional

from litestar import Router
from litestar import get

import evidently
from evidently.legacy.ui.api.models import Version

EVIDENTLY_APPLICATION_NAME = "Evidently UI"


@get("/version")
async def version() -> Version:
    return Version(
        application=EVIDENTLY_APPLICATION_NAME,
        version=evidently.__version__,
        commit=get_git_revision_short_hash(os.path.dirname(evidently.__file__)) or "-",
    )


def get_git_revision_short_hash(path: str) -> Optional[str]:
    from_env = os.environ.get("GIT_COMMIT")
    if from_env is not None:
        return from_env
    import subprocess

    try:
        return subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=path).decode("ascii").strip()
    except Exception:
        return None


def service_api():
    return Router("", route_handlers=[version])
