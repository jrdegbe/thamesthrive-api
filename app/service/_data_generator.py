# import random
# from datetime import timedelta, datetime
# from random import randint
# from uuid import uuid4
#
# from ThamesThrive.domain.event_metadata import EventMetadata
# from ThamesThrive.domain.time import EventTime
#
# from ThamesThrive.domain.event import Event
# from ThamesThrive.domain.entity import Entity
# from ThamesThrive.domain.session import Session, SessionMetadata
# from ThamesThrive.domain.time import ProfileTime, ProfileVisit
# from ThamesThrive.domain.metadata import ProfileMetadata
# from ThamesThrive.domain.profile_stats import ProfileStats
# from ThamesThrive.domain.profile import Profile
# from ThamesThrive.domain.event_source import EventSource


# def generate_events_for_profile(profiles, sessions, sources):
#     for profile in profiles:
#         for _ in range(randint(1, 50)):
#             yield Event(
#                 id=str(uuid4()),
#                 type=random.choice(['page-view', 'identify', 'purchase-order', 'log-in']),
#                 metadata=EventMetadata(
#                     time=EventTime(
#                         insert=generate_random_date(),
#                         process_time=randint(0, 10) / 100
#                     )
#                 ),
#                 profile=Entity(id=profile.id),
#                 session=random.choice(sessions),
#                 source=random.choice(sources),
#                 properties={
#                     "name": profile.data.pii.firstname,
#                     "surname": profile.data.pii.lastname,
#                 }
#             )


# def generate_profile():
#     date = generate_random_date()
#     return Profile(
#         id=str(uuid4()),
#         metadata=ProfileMetadata(time=ProfileTime(insert=date, visit=ProfileVisit(last=date, current=date))),
#         stats=ProfileStats(views=randint(0, 300)),
#         traits={},
#         segments=[random.choice(['frequent-user', 'customer', 'first-timer', 'vip'])],
#         active=True
#     )


# def generate_sessions_for_profiles(profiles):
#     for profile in profiles:
#         for _ in range(randint(1, 5)):
#             yield Session(metadata=SessionMetadata(),
#                 id=str(uuid4()),
#                 profile=Entity(id=profile.id),
#                 context={},
#                 properties={}
#             )


# def generate_random_date():
#     start = datetime.now() - timedelta(days=30)
#     end = datetime.now()
#     return start + (end - start) * random.random()


# def generate_fake_data(profiles=20):
#     profiles = [generate_profile() for _ in range(profiles)]
#     sessions = list(generate_sessions_for_profiles(profiles))
#     sources = [
#             EventSource(
#                 id="@test-resource",
#                 type=["web-page"],
#                 name="Test event source",
#                 description="This source is created for test purposes.",
#                 tags=['test']
#             ),
#             EventSource(
#                 id="@test-resource-1",
#                 type=["web-page"],
#                 name="Test event source 1",
#                 description="This source is created for test purposes.",
#                 tags=['test']
#             ),
#             EventSource(
#                 id="@test-resource-2",
#                 type=["web-page"],
#                 name="Test event source 1",
#                 description="This source is created for test purposes.",
#                 tags=['test']
#             )
#         ]
#     events=list(generate_events_for_profile(profiles, sessions=sessions, sources=sources))
#
#     data = {
#         "event-source": sources,
#         'profile': profiles,
#         'session': sessions,
#         'event': events
#     }
#
#     return data
