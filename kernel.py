from fastapi.routing import APIRouter
from controllers.math import MathController
from fastapi import FastAPI

from services import Math


def kernel(app: FastAPI) -> None:
    # Services
    mathLib = Math()

    # Controllers
    controllers = [MathController(APIRouter(prefix='/math'), mathService=mathLib)]
    for controller in controllers:
        app.include_router(controller.apiRouter)
