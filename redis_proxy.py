

import redis

r = redis.StrictRedis(host='106.54.68.249', port=9379, db=0, password='AeCqegjNMpKn5u4e')

print(r.zrange("proxies:universal", start=0, end=-1))