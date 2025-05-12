import requests
from typing import List, Dict
from .models import SendPatternRequest, SendSMSRequest, RequestStatus
from .exceptions import APIError, AuthenticationError

class MedianaSMSClient:
    BASE_URL = "https://api.mediana.ir/sms/v1"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        })

    def _request(self, method, endpoint, **kwargs):
        try:
            response = self.session.request(method, f"{self.BASE_URL}{endpoint}", **kwargs)
            if response.status_code == 401:
                raise AuthenticationError("Invalid API key")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise APIError(str(e), getattr(e.response, 'status_code', None))

    def send_pattern(self, recipients: List[str], pattern_code: str, parameters: Dict):
        data = {
            "recipients": recipients,
            "patternCode": pattern_code,
            "parameters": parameters
        }
        return self._request("POST", "/send/pattern", json=data)

    def send_sms(self, sending_number: str, recipients: List[str], message_text: str):
        data = {
            "sendingNumber": sending_number,
            "recipients": recipients,
            "messageText": message_text
        }
        return self._request("POST", "/send/sms", json=data)

    def get_status(self, request_id: int) -> RequestStatus:
        data = self._request("GET", f"/send-requests/status/{request_id}")
        return RequestStatus(request_id=request_id, status=data["status"], details=data)