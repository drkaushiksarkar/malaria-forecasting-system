"""Epidemiology error definitions."""


class EpidemiologyError(Exception):
    """Base error for epidemiology operations."""
    code = "EPIDEMIOLOGY_ERROR"


class EpidemiologyNotFoundError(EpidemiologyError):
    code = "EPIDEMIOLOGY_NOT_FOUND"


class EpidemiologyValidationError(EpidemiologyError):
    code = "EPIDEMIOLOGY_VALIDATION"


class EpidemiologyTimeoutError(EpidemiologyError):
    code = "EPIDEMIOLOGY_TIMEOUT"


ERROR_CODES = {
    EpidemiologyError.code: "General epidemiology error",
    EpidemiologyNotFoundError.code: "Epidemiology resource not found",
    EpidemiologyValidationError.code: "Epidemiology validation failed",
    EpidemiologyTimeoutError.code: "Epidemiology operation timed out",
}
