from abc import ABC
from dataclasses import dataclass
from typing import Any, Callable, List

from fastapi.routing import APIRouter

def _action(methods: List[str], *args, **kwargs) -> Callable:
    def decorator(method: Callable) -> Callable:
        method.__router__ = { 'methods': methods, 'args': args, 'kwargs': kwargs }

        return method
    
    return decorator

class API:
    @staticmethod
    def route(methods: List[str], *args, **kwargs) -> Callable:
        return _action(methods, *args, **kwargs)


    @staticmethod
    def delete(*args, **kwargs) -> Callable:
        return _action(['DELETE'], *args, **kwargs)

    @staticmethod
    def get(*args, **kwargs) -> Callable:
        return _action(['GET'], *args, **kwargs)
    
    @staticmethod
    def patch(*args, **kwargs) -> Callable:
        return _action(['PATCH'], *args, **kwargs)

    @staticmethod
    def post(*args, **kwargs) -> Callable:
        return _action(['POST'], *args, **kwargs)

    @staticmethod
    def put(*args, **kwargs) -> Callable:
        return _action('PUT', *args, **kwargs)

@dataclass
class ControllerABC(ABC):
    apiRouter: APIRouter
    
    def register(self) -> 'ControllerABC':
        methods = [func for func in dir(self) if callable(getattr(self, func)) and not func.startswith('__')]
        for func in methods:
            method = getattr(self, func)
            if '__router__' not in dir(method):
                continue
            data = method.__router__
            self.apiRouter.api_route(*data['args'], **data['kwargs'], methods=data['methods'])(method)

        return self
