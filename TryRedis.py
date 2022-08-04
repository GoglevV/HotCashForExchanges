import redis
import config
import telnetlib
# r = redis.StrictRedis(host=config.redis_server, password=config.redis_password)
# tn = telnetlib.Telnet(host=config.redis_server)
# print(tn)
r = redis.Redis(host=config.redis_server, port=6379, password=config.redis_password, username="default")
print(r.connection)
r.set("England", "Manchester")
# r.set("England": "London")
# r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
# print(r.get("Bahamas"))




