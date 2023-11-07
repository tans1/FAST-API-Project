from fastapi import APIRouter
from bson import ObjectId

from models.user import User
from config.db import connection
from schemas.schema import userEntity, usersEntity

user = APIRouter()

@user.get("/")
async def find_All_Users():
    return usersEntity(connection.local.user.find())

@user.get('/{id}')
async def get_Single_user(id):
    return  userEntity(connection.local.user.find_one({"_id":ObjectId(id)}))

@user.post("/")
async def create_User(userdata:User):
    connection.local.user.insert_one(dict(userdata))
    return usersEntity(connection.local.user.find())

@user.put('/{id}')
async def update_user(id, userdata: User):
    connection.local.user.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(userdata)
    })
    return userEntity(connection.local.user.find_one({"_id":ObjectId(id)}))

@user.delete('/{id}')
async def delete_user(id):
    return  userEntity(connection.local.user.find_one_and_delete({"_id":ObjectId(id)}))