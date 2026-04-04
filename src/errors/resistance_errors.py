"""Resistance error definitions."""


class ResistanceError(Exception):
    """Base error for resistance operations."""
    code = "RESISTANCE_ERROR"


class ResistanceNotFoundError(ResistanceError):
    code = "RESISTANCE_NOT_FOUND"


class ResistanceValidationError(ResistanceError):
    code = "RESISTANCE_VALIDATION"


class ResistanceTimeoutError(ResistanceError):
    code = "RESISTANCE_TIMEOUT"


ERROR_CODES = {
    ResistanceError.code: "General resistance error",
    ResistanceNotFoundError.code: "Resistance resource not found",
    ResistanceValidationError.code: "Resistance validation failed",
    ResistanceTimeoutError.code: "Resistance operation timed out",
}
