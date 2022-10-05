from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from videoGames import vgRouter

# Defining our Server
server = FastAPI()

origins = ['*']

server.add_middleware(
    CORSMiddleware, 
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)

@server.get('/')
def welcomeUser():
    return {"message": "Welcome to my API!"}

# Using our Video Games router
server.include_router(vgRouter.router)