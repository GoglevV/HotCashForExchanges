import redis, config

def connect():
    r = redis.Redis(host=config.redis_server, port=6379, password=config.redis_password, username=config.redis_user)
    return r
