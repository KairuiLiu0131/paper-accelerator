"""Logging utilities for consistent application-wide logging."""

import logging


def get_logger(name: str) -> logging.Logger:
    """Return a configured logger instance for the given module name."""
    # TODO: configure handlers, formatting, and log levels.
    return logging.getLogger(name)
