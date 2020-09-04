from abc import ABC, ABCMeta, abstractmethod
from collections.abc import Iterable
from datetime import datetime
from typing import Iterator

from dateutil.parser import parse


class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta):
    @abstractmethod
    def is_due(self) -> bool:
        raise NotImplementedError


class DeadlinedReminder(Iterable, ABC):
    @abstractmethod
    def is_due(self) -> bool:
        raise NotImplementedError


class DateReminder(DeadlinedReminder):

    def __init__(self, text: str, date: str):
        self.date = parse(date, dayfirst=True)
        self.text = text

    def is_due(self) -> bool:
        return self.date <= datetime.now()

    def __iter__(self) -> Iterator[str]:
        return iter([self.text, self.date.isoformat()])
