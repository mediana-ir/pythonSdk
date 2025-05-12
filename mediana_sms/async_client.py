import aiohttp
from typing import List, Dict
from .models import RequestStatus
from .exceptions import APIError, AuthenticationError

class AsyncMedianaSMSClient:
    BASE_URL = "https://api.mediana.ir/sms/v1"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession(headers={
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        })
        return self

    async def __aexit__(self, *args):
        await self.session.close()

    async def _request(self, method, endpoint, **kwargs):
        try:
            async with self.session.request(method, f"{self.BASE_URL}{endpoint}", **kwargs) as response:
                if response.status == 401:
                    raise AuthenticationError("Invalid API key")
                response.raise_for_status()
                return await response.json()
        except aiohttp.ClientError as e:
            raise APIError(str(e), getattr(e, 'status', None))

    async def send_pattern(self, recipients: List[str], pattern_code: str, parameters: Dict):
        data = {
            "recipients": recipients,
            "patternCode": pattern_code,
            "parameters": parameters
        }
        return await self._request("POST", "/send/pattern", json=data)

    async def send_sms(self, sending_number: str, recipients: List[str], message_text: str):
        data = {
            "sendingNumber": sending_number,
            "recipients": recipients,
            "messageText": message_text
        }
        return await self._request("POST", "/send/sms", json=data)

    async def get_status(self, request_id: int) -> RequestStatus:
        data = await self._request("GET", f"/send-requests/status/{request_id}")
        return RequestStatus(request_id=request_id, status=data["status"], details=data)