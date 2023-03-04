#System imports

#Libs imports
from fastapi import FastAPI, Response, status

#Local imports
from routers import cars, users

app = FastAPI()

app.include_router(cars.router, tags=["Car"])
app.include_router(users.router, tags=["User"])
