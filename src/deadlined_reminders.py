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

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is not DeadlinedReminder:
            return NotImplemented

        def attr_in_hierarchy(attr):
            return any(attr in SuperClass.__dict__ for SuperClass in subclass.__mro__)

        if not all(attr_in_hierarchy(attr) for attr in ('__iter__', 'is_due')):
            return NotImplemented

        return True

    @abstractmethod
    def __init__(self, text: str, date: str):
        pass

    @abstractmethod
    def is_due(self) -> bool:
        raise NotImplementedError


class DateReminder(DeadlinedReminder):

    def __init__(self, text: str, date: str):
        super().__init__(text, date)
        self.date = parse(date, dayfirst=True)
        self.text = text

    def is_due(self) -> bool:
        return self.date <= datetime.now()

    def __iter__(self) -> Iterator[str]:
        return iter([self.text, self.date.isoformat()])
