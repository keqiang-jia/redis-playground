import redis


r = redis.Redis(host='172.29.44.161', port=6379, db=0)

print("[*] Waiting for messages. To exit press CTRL+C")

try:
    while True:
        print('Received message:', r.brpop(
            'message_queue')[1].decode('utf-8'))
except KeyboardInterrupt:
    print("Stopped receiving messages")
