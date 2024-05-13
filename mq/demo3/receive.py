import redis

redis_conn = redis.StrictRedis(host='172.29.44.161', port=6379, db=0)

pubsub = redis_conn.pubsub()
pubsub.subscribe('queue')

print("[*] Waiting for messages. To exit press CTRL+C")

try:
    for message in pubsub.listen():
        if message['type'] == 'message':
            print("Received message:", message['data'].decode('utf-8'))
except KeyboardInterrupt:
    print("Stopped receiving messages")
