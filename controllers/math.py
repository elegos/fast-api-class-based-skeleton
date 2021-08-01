from dataclasses import dataclass
from typing import Union

from services.abc import MathABC

from controllers.abc import API, ControllerABC


@dataclass
class Response:
    result: float


@dataclass
class MathController(ControllerABC):
    mathService: MathABC

    @API.get('/hello/{name}')
    async def helloAction(self, name: str) -> str:
        return f'Hello {name}'

    @API.post('/mathAction1', response_model=Response)
    async def mathAction1(
        self, add1: Union[int, float], add2: Union[int, float], divide1: Union[int, float]
    ) -> float:
        builder = self.mathService.builder()

        return Response(builder.sum(add1, add2).divide(divide1).build())
