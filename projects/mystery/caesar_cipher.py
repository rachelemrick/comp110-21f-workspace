"""A set of functions to decode a Caesar Cipher."""

__author__ = 730348936


def decode_char(encoded_char: str) -> str:
    """Decodes a single character in a Caesar Cipher."""
    ascii_code: int = ord(encoded_char)
    normalized_code: int = ascii_code - 65
    real_code: int = (normalized_code - 1) % 26 + 65
    real_char: str = chr(real_code)
    return real_char


def decode_str(encoded_str: str) -> str:
    """Decodes a 5-character string in a Caesar Cipher."""
    decoded_str: str = ""
    char1: str = encoded_str[0]
    char2: str = encoded_str[1]
    char3: str = encoded_str[2]
    char4: str = encoded_str[3]
    char5: str = encoded_str[4]
    decoded_str += decode_char(char1) + decode_char(char2) + decode_char(char3) + decode_char(char4) + decode_char(char5)
    return decoded_str


decoded_message: str = decode_str("CFMMU") + decode_str("PXFSX") + decode_str("JOEPX")
print(decoded_message)