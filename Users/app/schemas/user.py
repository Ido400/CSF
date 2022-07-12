from typing import List

from pydantic import BaseModel

from Users.app.schemas.ssh_key import SSHKey

class User(BaseModel):
    user_name:str
    name:str
    last_name:str
    ssh_keys:List[SSHKey]
