import redis

r = redis.Redis(host="localhost", port=6379, password=None)

r.set('key', 'pisa')
value = r.get('key')
print(value)

