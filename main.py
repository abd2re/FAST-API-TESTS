from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import json
from generate_json_requests import max_queries

class Request(BaseModel):
    id: str
    ip_source: str
    ip_destination: str
    date: datetime = datetime.now()
    message: str = ""
  
  

requests: list[Request] = list()

for i in range(max_queries):
    with open(f"json_requests/{i}.json", "r") as file:
        data = json.load(file)
    request: Request = Request(**data)
    requests.append(request)


app = FastAPI()

@app.get("/")
@app.get('/requests')
async def root(skip: int = 0, limit: int = 10):
    return requests[skip: skip + limit]

@app.get('/requests/{request_id}')
async def get_request(request_id: str):
    try:
        request: Request = next(filter(lambda request: request.id == request_id, requests))
        return request
    except:
        raise HTTPException(404, "Request ID not found")

@app.post("/send_request")
async def send_request():
    return