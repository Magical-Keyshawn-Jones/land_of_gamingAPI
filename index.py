from fastapi import FastAPI
import uvicorn
from videoGames import vgRouter

# Defining our Server
server = FastAPI()

@server.get('/')
def welcomeUser():
    return {"message": "Welcome to my API!"}

# Using our Video Games router
server.include_router(vgRouter.router)