import json
from kafka import KafkaConsumer

IDENTIFIER = "serhii_mishovych"

TOPICS = [
    f"temperature_alerts_{IDENTIFIER}",
    f"humidity_alerts_{IDENTIFIER}"
]

consumer = KafkaConsumer(
    *TOPICS,
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="alert-listener"
)

print("📡 Listening to alerts...")

for message in consumer:
    topic = message.topic
    data = message.value

    if "temperature" in topic:
        print(f"🔥 Temp Alert Received: {data}")
    elif "humidity" in topic:
        print(f"💧 Humidity Alert Received: {data}")
