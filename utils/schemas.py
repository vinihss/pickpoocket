from pydantic import BaseModel


class BrowserInfo(BaseModel):
    userAgent: str
    ip: str
    cookies: dict
    latitude: float
    longitude: float