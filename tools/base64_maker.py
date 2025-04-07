import base64

def encode_base64(text):
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def decode_base64(encoded_text):
    decoded_bytes = base64.b64decode(encoded_text.encode('utf-8'))
    return decoded_bytes.decode('utf-8')

if __name__ == "__main__":
    while True:
        try:
            mode = int(input("Select mode to base64 (1: encoding / 2: decoding) >> "))
            if mode not in [1, 2]:
                print("Invalid input! Please enter 1 or 2.")
                continue

            if mode == 1:
                original_text = str(input("Insert STR to encode >> "))
                encoded = encode_base64(original_text)
                print(f"Encoded: {encoded}")
                break
            elif mode == 2:
                original_text = str(input("Insert STR to decode >> "))
                decoded = decode_base64(original_text)
                print(f"Decoded: {decoded}")
                break

        except ValueError:
            print("Invalid input! Please enter a number (1 or 2).")
        except base64.binascii.Error:
            print("Invalid Base64 string! Please enter a valid encoded string.")
        except Exception as e:
            print(f"An error occurred: {e}")