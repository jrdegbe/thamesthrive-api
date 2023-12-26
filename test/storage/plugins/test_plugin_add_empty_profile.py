from  ThamesThrive .domain.entity import Entity
from  ThamesThrive .domain.event_metadata import EventMetadata
from  ThamesThrive .domain.time import EventTime
from  ThamesThrive .domain.session import Session, SessionMetadata
from  ThamesThrive .domain.event import Event, EventSession
from  ThamesThrive .process_engine.action.v1.internal.add_empty_profile.plugin import AddEmptyProfileAction
from  ThamesThrive .service.plugin.service.plugin_runner import run_plugin


def test_plugin_add_empty_profile():
    payload = {}
    event = Event(
        id='1',
        type='text',
        metadata=EventMetadata(time=EventTime(), profile_less=True),
        session=EventSession(id='1'),
        source=Entity(id='1')
    )
    session = Session(
        id='1',
        metadata=SessionMetadata()
    )
    result = run_plugin(AddEmptyProfileAction, {}, payload=payload, event=event, session=session, profile=None)
    assert result.event.metadata.profile_less is False
    assert result.event.profile is not None

