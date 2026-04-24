from fastapi import FastAPI
from app.database.connection import engine
from app.routes import user_routes
from app.routes import family_routes
from app.routes import family_member_routes
from app.routes import shopping_list_routes
from app.routes import shopping_list_item_routes
from app.routes import product_routes
from app.routes import brand_routes
from app.routes import product_variant_routes
from app.routes import supermarket_routes
from app.routes import price_routes
from app.routes import purchase_routes
from app.routes import purchase_item_routes


app = FastAPI()

app.include_router(user_routes.router)
app.include_router(family_routes.router)
app.include_router(family_member_routes.router)
app.include_router(shopping_list_routes.router)
app.include_router(shopping_list_item_routes.router)
app.include_router(product_routes.router)
app.include_router(brand_routes.router)
app.include_router(product_variant_routes.router)
app.include_router(supermarket_routes.router)
app.include_router(price_routes.router)
app.include_router(purchase_routes.router)
app.include_router(purchase_item_routes.router)


@app.get("/")
def root():
    return {"message": "Smart Shopping API 🚀"}


@app.get("/test-db")
def test_db():
    try:
        connection = engine.connect()
        return {"message": "Conexión exitosa 🚀"}
    except:
        return {"error": "Falló la conexión"}