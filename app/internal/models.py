
class Car(BaseModel):
    make: str
    model: str
    year: int
    color: str
    mileage: float
    price: float

class User(BaseModel): # we don't include password_hash in the definition of the class because we don't want to return it
    id: int
    name: str