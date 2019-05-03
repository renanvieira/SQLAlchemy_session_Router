from typing import Callable

from sqlalchemy import Boolean
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session


class RoutingSession(Session):
    _engine_selector: Callable[[Boolean], Engine]

    def __init__(self, engine_selector: Callable[[Boolean], Engine], **kwargs):
        self._engine_selector = engine_selector
        super().__init__(**kwargs)

    def get_bind(self, mapper=None, clause=None):
        return self._engine_selector(self._flushing)
