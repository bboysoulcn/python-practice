import redis

# 普通直接连接
# r = redis.Redis(host="vultr.bboysoul.com",port=6379,decode_responses=True)
# r.set("name","bboysoul")
# print(r.get("name"))

# 连接池连接
pool=redis.ConnectionPool(host="vultr.bboysoul.com",port=6379,decode_response=True)

r = redis.Redis(connection_pool=pool)
print(r.get('name'))