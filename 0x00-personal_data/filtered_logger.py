#!/usr/bin/env python3
"""
0. Regex-ing
"""
import re


def filter_datum(fields, redaction, message, separator):
    """filter_datum returns the log message obfuscated:"""
    pattern = f"({'|'.join(fields)})=[^{separator}]*"
    return re.sub(pattern, lambda m: m.group(0).split('=')[0]
                  + f'={redaction}', message)
