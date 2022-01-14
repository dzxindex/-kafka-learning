from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='192.168.42.200:9092')
# for _ in range(10):
producer.send('foobar', b'some_message_bytes')


# from kafka import KafkaProducer
#
# bootstrap_servers = ['192.168.42.200:9092']
# topicName = 'myTopic'
#
# producer = KafkaProducer(bootstrap_servers = bootstrap_servers,
# api_version = (0, 11, 5),
# request_timeout_ms=1000000, api_version_auto_timeout_ms=1000000)
# producer = KafkaProducer()