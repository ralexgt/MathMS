from fastapi import FastAPI
from controllers.math_controller import router as math_router
from models.database import Database
 
db = Database()
app = FastAPI(
  title="Math Microservice",
  description="A microservice that does some computational work for you",
)

app.include_router(math_router)

@app.get("/")
def root():
  return {"message": "Welcome to the Math microservice"}



