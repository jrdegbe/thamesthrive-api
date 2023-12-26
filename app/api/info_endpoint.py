from datetime import datetime

from fastapi import APIRouter

from ThamesThrive.domain.api_instance import ApiInstance
from ThamesThrive.service.license import License

from app.config import server
from ThamesThrive.config import ThamesThrive

router = APIRouter()


@router.get("/info/version", tags=["info"], include_in_schema=server.expose_gui_api, response_model=str)
async def get_version():
    """
    Returns info about ThamesThrive API version
    """
    return ThamesThrive.version.version


@router.get("/info/version/details", tags=["info"])
async def get_current_backend_version():

    """
    Returns current backend version with previous versions.
    """

    version = ThamesThrive.version.dict()
    version['instance'] = ApiInstance().id

    if License.has_license():
        license = License.check()
        version['owner'] = license.owner
        version['expires'] = datetime.fromtimestamp(license.expires)
        version['licenses'] = list(license.get_service_ids())
    else:
        version['owner'] = "ThamesThrive"
        version['expires'] = "Never"
        version['licenses'] = ["MIT + Common Clause"]
    return version
