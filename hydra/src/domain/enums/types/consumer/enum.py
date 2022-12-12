from enum import Enum


class ConsumerType(Enum):
    KAFKA = 0
    SQS = 1
    RABBITMQ = 2
