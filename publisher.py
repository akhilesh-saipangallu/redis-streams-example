import redis
import time
import random

# Connect to Redis
redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

stream_name = 'stream_demo'

def produce_messages():
    i = 1
    while True:
        message = {
            'data': f'event_{i}',
            'timestamp': str(time.time())
        }
        redis_client.xadd(stream_name, message)
        print(f'Produced: {message}')
        i += 1
        time.sleep(5)  # Produces a message every second

if __name__ == '__main__':
    produce_messages()
1