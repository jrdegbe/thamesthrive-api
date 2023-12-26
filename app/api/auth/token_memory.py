from ThamesThrive.service.singleton import Singleton
from ThamesThrive.service.storage.redis.collections import Collection
from ThamesThrive.service.storage.redis_client import RedisClient
from ThamesThrive.config import ThamesThrive
from hashlib import sha1


class TokenMemory(metaclass=Singleton):

    def __init__(self):
        self._redis = RedisClient()
        self.ttl = 30 * 60
        self.instance_hash = sha1(f"{Collection.token}{ThamesThrive.version.version}.{ThamesThrive.version.name}"
                                  .encode("utf-8")).hexdigest()

    def __setitem__(self, token, value):
        self._redis.set(f"{self.instance_hash}-{token}", value, ex=self.ttl)

    def __getitem__(self, token):
        return self._redis.get(f"{self.instance_hash}-{token}")

    def __delitem__(self, token):
        self._redis.delete(f"{self.instance_hash}-{token}")

    def refresh(self, token):
        self._redis.expire(f"{self.instance_hash}-{token}", self.ttl)

