# import  mysql.connector

# conexion = mysql.connector.connect(
#     user= "root",
#     host="localhost",
#     password="1048071288",
#     database="curso-python",
#     port="3306"
# )

# cursor = conexion.cursor()

# print(conexion)

from fastapi import FastAPI

app = FastAPI()
peoples = [
    {
        "id": 1,
        "username": "felixochoa"
    },
    {
        "id": 2,
        "usename": "abdul"
    },
    {
        "id": 3,
        "usename": "Aquiminovalle"

    }
]

@app.get("/")
async def root():
    return {"message":"aquimin es cule bollo"}



@app.get("/people")
async def getpeople():
    return {
        "people": peoples
    }

@app.get ("/people/{id}")
async def getpeopleByid(id: int):

    peoplesearch= {}
    for people in peoples:
        if( people["id"] == id ):
            peoplesearch == peoples
    
    return {
        "message": peoplesearch,
    }
@app.post("/create-people ")  
async def createpeople(id: int,usename: str):
    peoplecreate = {
        "id": id,
        "username": usename
    } 

    peoples.append(peoplecreate)

    return {
        "message": "la persona  se ha creado"
    }

@app.put("/edit-people")
async def editpeople(id: int,username: str):
    for people in peoples:
      if (people ["id"] == id ):
        people["id"] = id
        people["username"] = username
    return {
        "message ": "se esdito la persona "
    }

@app.delete("/delete-people")
async def deletepeoples(id: int):
    for people in peoples:
        if(people["id"] == id ):
            peoples.remove(people)

    return{
        "message":"se ha eliminado la persona "
    }