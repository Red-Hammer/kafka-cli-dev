import argparse
import asyncio
from kafka import KafkaConsumer
import json

def parse_cli_args(argv=None):
    parser = argparse.ArgumentParser(
            description='Do something'
    )

    parser.add_argument(
            '--test',
            action='store_true'
    )
    result = parser.parse_args(argv)

    if result.test:
        print('yeeeeeeeeeeeet')
        exit(126)
    return result

def get_messages():
    consumer = KafkaConsumer(
            'test',
            bootstrap_servers=['192.168.1.93:9092'],
            value_deserializer=lambda m: json.loads(m.decode('ascii'))
                             )

    for message in consumer:
        print(message)


def main(argv = None):
    arguments = parse_cli_args(argv)
    print('Got some args')
    print(arguments)
    get_messages()

if __name__ == '__main__':
    main()