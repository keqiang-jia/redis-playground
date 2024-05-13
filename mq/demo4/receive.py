import redis
import time

r = redis.Redis(host='172.29.44.161', port=6379, db=0)

try:
    r.xgroup_destroy('mystream', 'mygroup')
except:
    pass

stream_name = 'mystream'
group_name = 'mygroup'

r.xgroup_create(stream_name, group_name, mkstream=True)


def receive_messages():
    while True:
        messages = r.xreadgroup(
            group_name,
            'consumer',
            streams={stream_name: '>'},
            count=1,
            block=0
        )

        if messages:
            for message in messages[0][1]:
                print(f"Received message: {message[1]}")
                r.xack(stream_name, group_name, message[0])


try:
    receive_messages()
except KeyboardInterrupt:
    print("Exiting...")
