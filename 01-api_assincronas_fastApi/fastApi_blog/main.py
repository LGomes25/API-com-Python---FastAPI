from fastapi import FastAPI
from .controllers import post, auth

app = FastAPI()
app.include_router(auth.router)
app.include_router(post.router)








