
from pydantic import BaseModel

class SSHKey(BaseModel):
    name:str
    public_key:str