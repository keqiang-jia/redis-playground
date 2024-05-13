import redis

r = redis.StrictRedis(host='172.29.44.161', port=6379, db=0)

print("[*] Waiting for messages. To exit press CTRL+C")

try:
    while True:
        message = r.zpopmin('message_queue', 1)
        if message:
            print(message[0][0].decode('utf-8'))
except KeyboardInterrupt:
    print("Ctrl+C pressed. Exiting...")
