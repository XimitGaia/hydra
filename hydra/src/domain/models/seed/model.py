from dataclasses import dataclass

from hydra.src.domain.enums.types.consumer import ConsumerType
from hydra.src.domain.enums.types.run_mode import RunMode


@dataclass
class Seed:
    consumer_type: ConsumerType
    run_mode: RunMode
    service: any
