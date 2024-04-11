from fastapi import FastAPI
from routes import pedidos
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)
app.include_router(pedidos.router)

@app.get("/")
async def inicio():
    return "Bienvenido"
