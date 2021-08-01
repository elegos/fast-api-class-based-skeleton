from dataclasses import dataclass
from typing import Union

from fastapi import FastAPI
from fastapi.routing import APIRouter
from services.abc import MathABC

from controllers.abc import ControllerABC


@dataclass
class MathController(ControllerABC):
    mathService: MathABC

    def register(self, app: APIRouter):
        app.get('/hello/{name}')(self.hello)
        app.get('/mathAction1')(self.mathAction1)

        return app

    def hello(self, name: str) -> str:
        return f'Hello {name}'
    
    def mathAction1(self, add1: Union[int, float], add2: Union[int, float], divide1: Union[int, float]) -> float:
        builder = self.mathService.builder()

        return builder.sum(add1, add2).divide(divide1).build()

