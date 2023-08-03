#!/usr/bin/env python3
"""
Script for handling Personal Data
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Replaces sensitive information in a message with a redacted value
    based on the list of fields to redact

    Args:
        fields (List[str]): List of fields to redact
        redaction (str): The value to use for redaction
        message (str): The string message to filter
        separator (str): The separator to use between fields

    Returns:
        str: The filtered string message with redacted values
    """
    # Loop through each field to be redacted
    for f in fields:
        # Use regular expression to replace sensitive information with the redaction string
        # The regex pattern looks for occurrences of the field followed by "=" and any characters until the separator
        # It then replaces this portion with the field followed by "=" and the redaction string followed by the separator
        message = re.sub(f'{f}=.*?{separator}',
                         f'{f}={redaction}{separator}', message)
    return message
