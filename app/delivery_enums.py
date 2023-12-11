from enum import Enum


class Dimensions(Enum):
    BIG = 200
    SMALL = 100


class ServiceWorkload(Enum):
    VERY_HIGH = 1.6
    HIGH = 1.4
    BIG = 1.2
    NORMAL = 1
