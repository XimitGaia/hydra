import inspect

import meeseeks

from hydra.src.domain.enums.types.consumer import ConsumerType
from hydra.src.domain.enums.types.run_mode import RunMode
from hydra.src.domain.models.seed import Seed


@meeseeks.OnlyOne
class SeedRegister:
    def __init__(self):
        self.seeds = list()

    def register_seed(self, service, consumer_type: ConsumerType, run_mode: RunMode):
        self.__is_consumer_type_valid(service=service, consumer_type=consumer_type)
        self.__is_run_mode_valid(service=service, run_mode=run_mode)
        # use pickel to send to new process instance
        seed = Seed(consumer_type=consumer_type, run_mode=run_mode, service=service)
        self.seeds.append(seed)

    @staticmethod
    def __is_consumer_type_valid(service, consumer_type: ConsumerType) -> None:
        if not consumer_type in ConsumerType:
            raise ValueError()

        service_base_class_by_consumer_type = {
            ConsumerType.KAFKA: int,
            ConsumerType.SQS: int,
            ConsumerType.RABBITMQ: int,
        }
        service_base_class = service_base_class_by_consumer_type.get(consumer_type)

        if not issubclass(service, service_base_class):
            raise ValueError()

    @staticmethod
    def __is_run_mode_valid(service, run_mode: RunMode) -> None:
        if not run_mode in RunMode:
            raise ValueError()

        is_coroutine_function = inspect.iscoroutinefunction(service.run)

        run_mode_by_is_coroutine_function = {
            True: run_mode.ASYNC,
            False: run_mode.SYNC,
        }

        run_mode_check = run_mode_by_is_coroutine_function.get(is_coroutine_function)

        if run_mode != run_mode_check:
            raise ValueError()
