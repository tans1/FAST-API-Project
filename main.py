from fastapi import FastAPI
from routes.route import user

app = FastAPI()
app.include_router(user)
