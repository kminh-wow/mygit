import base64

def encode_base64(text):
    # 문자열을 바이트로 변환 후 Base64로 인코딩
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    # 인코딩된 바이트를 문자열로 변환해 반환
    return encoded_bytes.decode('utf-8')

def decode_base64(encoded_text):
    # Base64 문자열을 바이트로 변환 후 디코딩
    decoded_bytes = base64.b64decode(encoded_text.encode('utf-8'))
    # 디코딩된 바이트를 문자열로 변환해 반환
    return decoded_bytes.decode('utf-8')

# 예제 사용
if __name__ == "__main__":
    # 인코딩할 원본 문자열
    original_text = "Hello, World!"
    
    # Base64 인코딩
    encoded = encode_base64(original_text)
    print(f"Encoded: {encoded}")
    
    # Base64 디코딩
    decoded = decode_base64(encoded)
    print(f"Decoded: {decoded}")