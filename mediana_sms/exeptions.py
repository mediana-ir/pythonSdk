class MedianaSMSException(Exception):
    """Base exception for all SDK errors"""
    pass

class AuthenticationError(MedianaSMSException):
    """Invalid API key"""
    pass

class APIError(MedianaSMSException):
    """API request failed"""
    def __init__(self, message, status_code=None):
        self.status_code = status_code
        super().__init__(message)

class ValidationError(MedianaSMSException):
    """Invalid input data"""
    pass