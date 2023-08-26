from pydantic import BaseModel

class FloorRequest(BaseModel):
    level: int

class RequestID(BaseModel):
    request_id: str