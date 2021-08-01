from abc import ABC, abstractmethod

from fastapi import FastAPI
from fastapi.routing import APIRouter


class ControllerABC(ABC):
    @abstractmethod
    def register(self, app: APIRouter) -> APIRouter:
        pass
