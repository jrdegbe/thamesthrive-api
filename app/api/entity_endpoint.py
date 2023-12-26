from elasticsearch.exceptions import NotFoundError
from fastapi import APIRouter, Depends, HTTPException

from ThamesThrive.domain.entity_index_mapping import EntityIndexMapping
from ThamesThrive.service.storage.driver.elastic import raw as raw_db
from ThamesThrive.service.storage.driver.elastic import entity as entity_db
from .auth.permissions import Permissions
from ..config import server

router = APIRouter(
    dependencies=[Depends(Permissions(roles=["admin", "developer", "maintainer"]))]
)


@router.post("/entity/{index}", tags=["entity"], include_in_schema=server.expose_gui_api)
async def create_entity_index(index: str, mapping: EntityIndexMapping):
    index = f"entity-{index}"
    return await raw_db.create_index(index, mapping.dict(by_alias=True))


@router.get("/entity/{index}/mapping", tags=["entity"], include_in_schema=server.expose_gui_api)
async def get_entity_index_mapping(index: str):
    try:
        index = f"entity-{index}"
        return await raw_db.get_mapping(index)
    except NotFoundError as e:
        return HTTPException(status_code=404, detail=str(e))


@router.get("/entity/count", tags=["entity"], include_in_schema=server.expose_gui_api)
async def entity_count(query: dict = None):
    return await entity_db.count(query)
