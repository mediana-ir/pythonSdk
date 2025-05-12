
```
# Mediana SMS Python SDK
A modern Python SDK for the Mediana SMS API with both synchronous and asynchronous support.

## Features

- **Full API Coverage**: Supports all Mediana SMS API endpoints
- **Sync/Async Support**: Choose between synchronous or asynchronous clients
- **Type Annotations**: Full type hints for better IDE support
- **Pydantic Models**: Request/response validation
- **Error Handling**: Comprehensive exception hierarchy

## Installation

```bash
pip install mediana-sms-sdk
```

## Quick Start

### Synchronous Client

```python
from mediana_sms import MedianaSMSClient

# Initialize client
client = MedianaSMSClient(api_key="your_api_key")

# Send SMS
response = client.send_sms(
    sending_number="989982009183",
    recipients=["09100000000"],
    message_text="Hello from SDK"
)

print("Message ID:", response["requestId"])
```

### Asynchronous Client

```python
import asyncio
from mediana_sms import AsyncMedianaSMSClient

async def main():
    async with AsyncMedianaSMSClient("your_api_key") as client:
        # Send pattern SMS
        response = await client.send_pattern(
            recipients=["09100000000"],
            pattern_code="welcome_pattern",
            parameters={"name": "John"}
        )
        print("Pattern sent:", response)

asyncio.run(main())
```

## API Reference

### Synchronous Methods

```python
client.send_sms(
    sending_number: str,
    recipients: List[str],
    message_text: str
) -> Dict

client.send_pattern(
    recipients: List[str],
    pattern_code: str,
    parameters: Dict[str, str]
) -> Dict

client.get_status(request_id: int) -> RequestStatus
```

### Asynchronous Methods

Same methods as synchronous client but prefixed with `await`:

```python
await async_client.send_sms(...)
await async_client.send_pattern(...)
await async_client.get_status(...)
```

## Error Handling

The SDK provides specific exception types:

```python
try:
    client.send_sms(...)
except AuthenticationError:
    print("Invalid API key")
except APIError as e:
    print(f"API Error: {e} (Status: {e.status_code})")
except ValidationError:
    print("Invalid input parameters")
```

## Examples

See complete examples in the `examples/` directory:

1. [Send SMS](examples/send_sms.py)
2. [Send Pattern SMS](examples/send_pattern.py)
3. [Check Status](examples/check_status.py)
4. [Async Usage](examples/async_example.py)
