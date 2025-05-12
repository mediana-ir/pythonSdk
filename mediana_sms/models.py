from typing import Dict, List, Optional
from pydantic import BaseModel

class PatternParameters(BaseModel):
    additionalProp1: Optional[str] = None
    additionalProp2: Optional[str] = None
    additionalProp3: Optional[str] = None

class SendPatternRequest(BaseModel):
    recipients: List[str]
    patternCode: str
    parameters: PatternParameters

class SendSMSRequest(BaseModel):
    sendingNumber: str
    recipients: List[str]
    messageText: str

class RequestStatus(BaseModel):
    request_id: int
    status: str
    details: Optional[Dict] = None