"""Surveillance error definitions."""


class SurveillanceError(Exception):
    """Base error for surveillance operations."""
    code = "SURVEILLANCE_ERROR"


class SurveillanceNotFoundError(SurveillanceError):
    code = "SURVEILLANCE_NOT_FOUND"


class SurveillanceValidationError(SurveillanceError):
    code = "SURVEILLANCE_VALIDATION"


class SurveillanceTimeoutError(SurveillanceError):
    code = "SURVEILLANCE_TIMEOUT"


ERROR_CODES = {
    SurveillanceError.code: "General surveillance error",
    SurveillanceNotFoundError.code: "Surveillance resource not found",
    SurveillanceValidationError.code: "Surveillance validation failed",
    SurveillanceTimeoutError.code: "Surveillance operation timed out",
}
