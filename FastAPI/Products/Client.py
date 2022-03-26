from pydantic import BaseModel
from pydantic.typing import List


class Client(BaseModel):
    frameArray: List[str] = None
