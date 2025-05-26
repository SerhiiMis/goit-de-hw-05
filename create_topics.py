from kafka.admin import KafkaAdminClient, NewTopic


IDENTIFIER = "serhii_mishovych"

admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092",
    client_id="admin"
)

topic_list = [
    NewTopic(name=f"building_sensors_{IDENTIFIER}", num_partitions=1, replication_factor=1),
    NewTopic(name=f"temperature_alerts_{IDENTIFIER}", num_partitions=1, replication_factor=1),
    NewTopic(name=f"humidity_alerts_{IDENTIFIER}", num_partitions=1, replication_factor=1)
]

admin_client.create_topics(new_topics=topic_list, validate_only=False)

print("\n✅ Created Topics:")
for topic in admin_client.list_topics():
    if IDENTIFIER in topic:
        print(topic)
