from fastapi import FastAPI

from kernel import kernel

app = FastAPI()
kernel(app)
