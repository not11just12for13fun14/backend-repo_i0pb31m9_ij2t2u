from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Inquiry(BaseModel):
    names: str = Field(..., description="Names of the couple")
    email: EmailStr = Field(..., description="Contact email")
    date: Optional[str] = Field(None, description="Wedding date (YYYY-MM-DD)")
    location: Optional[str] = Field(None, description="Wedding location")
    message: Optional[str] = Field(None, description="Details and wishes")
