import random
import redisConnect
import json

random.seed(444)
hats = {f"hat:{random.getrandbits(32)}": i for i in (
    {
        "color": "black",
        "price": 49.99,
        "style": "fitted",
        "quantity": 1000,
        "npurchased": 0,
    },
    {
        "color": "maroon",
        "price": 59.99,
        "style": "hipster",
        "quantity": 500,
        "npurchased": 0,
    },
    {
        "color": "green",
        "price": 99.99,
        "style": "baseball",
        "quantity": 200,
        "npurchased": 0,
    })
}
hats_json = json.dumps(hats)
rc = redisConnect.connect()
# with rc.pipeline() as pipe:
#    for h_id, hat in hats.items():
#        pipe.zadd(h_id, hat)
#    pipe.execute()

with rc.pipeline() as pipe:
    for h_id, hat in hats.items():
        rc.set(h_id, json.dumps(hat))
    pipe.execute()

print(rc.get(h_id))
