from enum import Enum


class VehicleType(str, Enum):
    HEAVY_TRANSPORT = "HEAVY_TRANSPORT"
    PRIVATE = "PRIVATE"


class OwnerType(str, Enum):
    COMPANY = "COMPANY"
    INDIVIDUAL = "INDIVIDUAL"


class StationStatus(str, Enum):
    AVAILABLE = "AVAILABLE"
    OCCUPIED = "OCCUPIED"
    OUT_OF_SERVICE = "OUT_OF_SERVICE"
