from datetime import datetime, UTC

from pydantic import BaseModel, Field

class PostIn(BaseModel):
    title: str
    published_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    published: bool =False
    author: str

