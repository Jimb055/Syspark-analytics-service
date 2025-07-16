from fastapi import FastAPI
from app.api.routes import router as analytics_router

app = FastAPI(
    title="SysPark Analytics Service",
    version="1.0.0",
    description="Microservice for global system statistics."
)

app.include_router(analytics_router, prefix="/api/statistics")
