from app.routers.products import router as products_router
from app.routers.locations import router as locations_router

routers = [
    products_router,
    locations_router,
]