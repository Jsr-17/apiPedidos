from pydantic import BaseModel

class Pedido(BaseModel):
    unidades:int
    referencias:int
    referencias_rotura:int
    unidades_rotura:int
    factura_comercial:str
    documentacion_agente: bool
    situacion:str
    documentacion:str
    fecha_embarque:str|None
    fecha_puerto:str|None
    items:list[dict[str,str|int]]

