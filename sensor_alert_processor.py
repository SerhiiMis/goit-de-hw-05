import json
from kafka import KafkaConsumer, KafkaProducer

IDENTIFIER = "serhii_mishovych"

INPUT_TOPIC = f"building_sensors_{IDENTIFIER}"
TEMP_ALERT_TOPIC = f"temperature_alerts_{IDENTIFIER}"
HUMIDITY_ALERT_TOPIC = f"humidity_alerts_{IDENTIFIER}"

consumer = KafkaConsumer(
    INPUT_TOPIC,
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="sensor-alert-processor"
)

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

print("📥 Processor started, waiting for sensor data...")

for message in consumer:
    data = message.value
    sensor_id = data["sensor_id"]
    temperature = data["temperature"]
    humidity = data["humidity"]
    timestamp = data["timestamp"]

    if temperature > 40:
        alert = {
            "sensor_id": sensor_id,
            "temperature": temperature,
            "timestamp": timestamp,
            "message": "⚠ Temperature above threshold!"
        }
        producer.send(TEMP_ALERT_TOPIC, value=alert)
        print(f"🔥 Temp Alert: {alert}")

    if humidity > 80 or humidity < 20:
        alert = {
            "sensor_id": sensor_id,
            "humidity": humidity,
            "timestamp": timestamp,
            "message": "💧 Humidity out of range!"
        }
        producer.send(HUMIDITY_ALERT_TOPIC, value=alert)
        print(f"💧 Humidity Alert: {alert}")
