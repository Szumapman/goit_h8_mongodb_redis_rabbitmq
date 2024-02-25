import sys

from part_II.consumer import consumer


CONSUMER_QUEUE_NAME = 'phone'

if __name__ == '__main__':
    try:
        consumer(CONSUMER_QUEUE_NAME)
    except KeyboardInterrupt:
        print(f'\nConsumer {CONSUMER_QUEUE_NAME} stopped')
        sys.exit(0)
