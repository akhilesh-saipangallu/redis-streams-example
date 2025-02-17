import redis
import time

# Connect to Redis
redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

stream_name = 'stream_demo'
group_name = 'email_consumer_group'
consumer_name = 'email_consumer'


def setup_consumer_group():
    try:
        redis_client.xgroup_create(stream_name, group_name, id='0', mkstream=True)
        print(f'Consumer group "{group_name}" created.')
    except redis.exceptions.ResponseError as e:
        if 'BUSYGROUP' in str(e):
            print(f'Consumer group "{group_name}" already exists.')
        else:
            raise


def consume_messages():
    while True:
        try:
            messages = redis_client.xreadgroup(
                group_name, 
                consumer_name, 
                {stream_name: '>'},  # Fetch only new messages
                count=10,
                block=5000  # Wait for 5 seconds if no messages
            )
            if messages:
                for stream, message_list in messages:
                    for message_id, message_data in message_list:
                        print(f'email consumer: {consumer_name} consumed: {message_data}')
                        # Acknowledge the message
                        redis_client.xack(stream_name, group_name, message_id)
        except Exception as e:
            print(f'Error: {e}')


if __name__ == '__main__':
    setup_consumer_group()
    consume_messages()
