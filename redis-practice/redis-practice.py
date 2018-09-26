import redis

# 普通直接连接
# r = redis.Redis(host="vultr.bboysoul.com",port=6379,decode_responses=True)
# r.set("name","bboysoul")
# print(r.get("name"))

# 连接池连接
# pool=redis.ConnectionPool(host="vultr.bboysoul.com",port=6379,decode_responses=True)
#
# r = redis.Redis(connection_pool=pool)
# r.set("age","21")
# print(r.get("age"))

# mset mget 批量设置值 批量获取值
pool = redis.ConnectionPool(host="vultr.bboysoul.com",port=6379,decode_responses=True,db=1)
r = redis.Redis(connection_pool=pool)
# r.mset(name1="张三",name2="李四")
# print(r.mget("name1","name2"))

# 循环打印redis中所有的数据


# for key in list_keys:
#     print(r.get(key))

# 循环删除redis中所有的数据

r.mset(name1="a",name2="b",name3="c",name4="d")
print(r.mget("name1"))
print(r.strlen("name1"))




# 设置值的过期时间
# ex 过期时间秒
# px 过期时间毫秒
# nx 当key不存在，set才可以操作
# xx 当key存在，set才可以操作
import time

# r.set("object","linux",px=1)
# print("下面应该打印none因为时间太短，已经过期了")
# print(r.get("object"))
# r.set("object2","linux2",ex=3)
# print("下面应该会打印")
# print(r.get("object2"))
# time.sleep(3)
# print("下面应该不会打印")
# print(r.get("object2"))
# print("下面应该打印linux3")
# r.set("object","linux3")
# r.set("object","linux4",nx=True)
# print(r.get("object"))
# print("下面应该打印linux5")
# r.set("object","linux5",xx=True)
# print(r.get("object"))

