from fastapi.routing import APIRouter
from controllers.math import MathController
from fastapi import FastAPI

from services import Math


def kernel(app: FastAPI) -> None:
    # Services
    mathLib = Math()

    # Controllers
    app.include_router(MathController(mathService=mathLib).register(APIRouter(prefix='/math')))