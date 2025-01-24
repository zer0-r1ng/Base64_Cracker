import base64
import binascii
import re

# Check whether the string is a validly Base64 encoding string or not
def is_base64(s):
    try:
        return base64.b64encode(base64.b64decode(s)).decode() == s
    except (binascii.Error, UnicodeDecodeError):
        return False

# Recursive to decode multi-layer Base64-encoded strings
def decode_layer(encoded_str, max_layers=100):
    decoded_str = encoded_str
    layers = 0

    while layers < max_layers and is_base64(decoded_str):
        try:
            decoded_str = base64.b64decode(decoded_str).decode('utf-8', errors='ignore')
            layers += 1
        except (binascii.Error, UnicodeDecodeError):
            break

    if layers == 0:
        print("Failed to detect a valid Base64 encoding!")
    else:
        print(f"Success to decode {layers} layer Base64 encoding.")

    return decoded_str


def main():
    print("A tool to decode multi-layer Base64 decoding")
    encoded_str = input("Please enter the Base64 string to decode: ").strip()

    # Try to get rid of any non-Base64 characters such as line breaks, spaces, etc.
    encoded_str = re.sub(r'[^A-Za-z0-9+/=]', '', encoded_str)

    result = decode_layer(encoded_str)
    print(f"The result:\n{result}")

# Check the entry point
if __name__ == "__main__":
    main()