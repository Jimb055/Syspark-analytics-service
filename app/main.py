from fastapi import FastAPI
from app.api.routes import router as analytics_router
from app.database import Base, engine  # Importa Base y engine para crear tablas

app = FastAPI(
    title="SysPark Analytics Service",
    version="1.0.0",
    description="Microservice for global system statistics."
)

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

# Incluir rutas
app.include_router(analytics_router, prefix="/api/statistics")
