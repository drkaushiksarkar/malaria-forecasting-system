"""Mortality error definitions."""


class MortalityError(Exception):
    """Base error for mortality operations."""
    code = "MORTALITY_ERROR"


class MortalityNotFoundError(MortalityError):
    code = "MORTALITY_NOT_FOUND"


class MortalityValidationError(MortalityError):
    code = "MORTALITY_VALIDATION"


class MortalityTimeoutError(MortalityError):
    code = "MORTALITY_TIMEOUT"


ERROR_CODES = {
    MortalityError.code: "General mortality error",
    MortalityNotFoundError.code: "Mortality resource not found",
    MortalityValidationError.code: "Mortality validation failed",
    MortalityTimeoutError.code: "Mortality operation timed out",
}
