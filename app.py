from fastapi import FastAPI, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from Model.conexion import Conexion
from Schema.restaurantes_schema import schema
import uuid
import json

app = FastAPI()
conn = Conexion()

@app.get('/', status_code=HTTP_200_OK)
def read_root():
    items = []
    for data2 in conn.leer_t():
        dic = {
            "id": str(uuid.uuid4()),
            "rating": data2[1],
            "name": data2[2],
            "site": data2[3],
            "email": data2[4],
            "phone": data2[5],
            "street": data2[6],
            "city": data2[7],
            "state": data2[8],
            "lat": data2[9],
            "lng": data2[10]
        }
        items.append(dic)
    return json.dumps(items, indent=4)

@app.get("/API/leer/{state}", status_code=HTTP_200_OK)
def get_one(state:str):
    item = []
    data2 = conn.leer_u(state)
    dic = {
            "id": str(uuid.uuid4()),
            "rating": data2[1],
            "name": data2[2],
            "site": data2[3],
            "email": data2[4],
            "phone": data2[5],
            "street": data2[6],
            "city": data2[7],
            "state": data2[8],
            "lat": data2[9],
            "lng": data2[10]
        }
    return dic

@app.post("/API/insertar", status_code=HTTP_201_CREATED)
def insertar(rest_data:schema):
    data2 = rest_data.dict()
    my_uuid= uuid.uuid4()
    data2["id"] = my_uuid
    conn.escribir(data2)
    return Response(status_code=HTTP_201_CREATED)

@app.put("/API/actualizar/{state}", status_code=HTTP_204_NO_CONTENT)
def actualizar(rest_data:schema, state:str):
    data2 = rest_data.dict()
    data2["state"] = state
    conn.actualizar(data2)
    return Response(status_code=HTTP_204_NO_CONTENT)

@app.delete("/API/borrar/{state}", status_code=HTTP_204_NO_CONTENT)
def borrar(state:str):
    conn.borrar(state)
    return Response(status_code=HTTP_204_NO_CONTENT)


    
