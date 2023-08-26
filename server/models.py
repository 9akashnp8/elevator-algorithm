from pydantic import BaseModel

class FloorRequest(BaseModel):
    destination_level: int
    current_level: int

class RequestID(BaseModel):
    request_id: str