# Redis Streams Example

## Steps to Run the Project
### 1. Setup a Virtual Environment:
```sh
python -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies:
```sh
pip install -r requirements.txt
```

### 3. Run the Publisher:
```sh
python publisher.py
```
This will publish a message every second to the Redis stream.

### 4. Run the Consumers Separately:
Open two separate terminal windows and run:

```sh
python consumer_1.py

python consumer_2.py
```

Each consumer will independently consume messages from the stream.


## Notes

- Ensure that Redis is running before executing the scripts.
- The consumers will receive the same messages separately.

