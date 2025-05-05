from fastapi import FastAPI
from app.database import Base, engine
from app.routers import router_product  # Import your router

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Krishna Jewellers API")

# Register the router
app.include_router(router_product.router)
