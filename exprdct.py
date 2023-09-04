

from time import sleep
from expiring_dict import ExpiringDict

cache = ExpiringDict(1)  # Keys will exist for 1 second

cache["key"] = "value"
print(cache.get("key"))
sleep(2)
print(cache.get("key"))


cache = ExpiringDict()  # No TTL set, keys set via [] will not expire

cache["permanent_key"] = "persistent value"
cache.ttl("expiring_key", "expiring value", 1)  # This will expire after 1 second
print(cache.get("permanent_key"))
print(cache.get("expiring_key"))
sleep(2)
print(cache.get("permanent_key"))
print(cache.get("expiring_key"))
