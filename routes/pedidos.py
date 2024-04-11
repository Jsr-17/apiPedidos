from fastapi import APIRouter
from database import db
from Models.pedido import Pedido
from schemas.pedido import esquema_pedido,list_pedido
from bson import ObjectId

router=APIRouter()

@router.post("/crearPedido")
async def crearPedido(pedido:Pedido):
    d_pedido=dict(pedido)

    id= db.coleccion.insert_one(d_pedido).inserted_id

    pedido_nuevo= esquema_pedido(db.coleccion.find_one({"_id":id}))
    return pedido_nuevo

@router.get("/pedido")
async def retornarPedidos():
    return list_pedido(db.coleccion.find())

@router.get("/obtenerPorId/{id}")
async def obtenerPorId(id:str):
    return esquema_pedido(db.coleccion.find_one({"_id":ObjectId(id)}))