from abc import ABC, abstractmethod


class Logger(ABC):

    @abstractmethod
    def log(self, lvl: str, msg: str):
        pass
