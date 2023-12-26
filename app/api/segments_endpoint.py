from collections import defaultdict
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException

from ThamesThrive.domain.named_entity import NamedEntity
from ThamesThrive.domain.segment import Segment
from ThamesThrive.domain.value_object.bulk_insert_result import BulkInsertResult
from ThamesThrive.service.storage.driver.elastic import segment as segment_db
from app.service.grouper import search
from .auth.permissions import Permissions
from ..config import server

router = APIRouter(dependencies=[Depends(Permissions(roles=["admin", "developer", "marketer"]))])

async def _load_record(id: str) -> Optional[Segment]:
    """Fetch a record by its ID."""
    return Segment.create(await segment_db.load_by_id(id))

@router.get("/segment/{id}", tags=["segment"], include_in_schema=server.expose_gui_api)
async def get_segment(id: str):
    """Return a segment with the given ID."""
    return await _load_record(id)

@router.delete("/segment/{id}", tags=["segment"], include_in_schema=server.expose_gui_api)
async def delete_segment(id: str):
    """Delete a segment with the given ID."""
    try:
        result = await segment_db.delete_by_id(id)
        await segment_db.refresh()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/segments/refresh", tags=["segment"], include_in_schema=server.expose_gui_api)
async def refresh_segments():
    """Refresh the segments index."""
    return await segment_db.refresh()

@router.get("/segments", tags=["segment"], include_in_schema=server.expose_gui_api)
async def get_segments(query: str = None):
    """
    Return segments matching the given query on name or event type.
    """
    # Fetch and process results...
    # [code for fetching and processing results]

@router.get("/segments/metadata", tags=["segment"], include_in_schema=server.expose_gui_api)
async def get_segment_metadata(name: str = ""):
    """Return segments matching the given name."""
    # Fetch and process metadata...
    # [code for fetching and processing metadata]

@router.post("/segment", tags=["segment"], response_model=BulkInsertResult, include_in_schema=server.expose_gui_api)
async def upsert_segment(segment: Segment):
    """Add or update a segment in the database."""
    try:
        result = await segment_db.save(segment.dict())
        await segment_db.refresh()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))