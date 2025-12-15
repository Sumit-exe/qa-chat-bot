from pydantic import BaseModel

class AskRequest(BaseModel):
    website_url: str
    question: str
