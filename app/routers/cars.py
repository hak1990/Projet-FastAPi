#System imports

#Libs imports
from fastapi import APIRouter

#Local imports
from internal.models import Car

router = APIRouter()

# bellow is a second way to instantiate a list of data. Here we instantiate them as instances of Car
car_list = [
    Car(make="Toyota", model="Camry", year=2015, color="blue", mileage=50000.0, price=15000.0),
    Car(make="Honda", model="Civic", year=2017, color="black", mileage=35000.0, price=18000.0),
    Car(make="Ford", model="Mustang", year=2020, color="red", mileage=10000.0, price=30000.0),
    Car(make="Chevrolet", model="Corvette", year=2021, color="white", mileage=500.0, price=80000.0)
]

@router.get("/cars")
async def get_all_cars():
    return car_list

@router.get("/cars")
async def get_all_users():
    return ""

