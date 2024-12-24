import base64

class Decrypt:
    def __init__(self, encoded_string):
        self.encoded_string = encoded_string
        self.result = self.method1(encoded_string)

    def method1(self, string: str):
        return self.method2(string, 'UTF-8')

    def method3(self, bArr, string: str):
        byte_array_length = len(bArr)
        string_length = len(string)
        i = 0
        i2 = 0
        bArr = bytearray(bArr)
        while i < byte_array_length:
            if i2 >= string_length:
                i2 = 0
            bArr[i] = bArr[i] ^ ord(string[i2])
            i += 1
            i2 += 1
        return bytes(bArr)

    def method2(self, string1: str, string2: str = 'UTF-8'):
        try:
            decoded_bytes = base64.b64decode(string1)
            return str(self.method3(decoded_bytes, string2), 'UTF-8')
        except Exception as e:
            print(f"Error: {e}")
            return None

if __name__ == "__main__":
    while True:
        encoded_string = str(input("Enter the encoded string: "))
        decryptor = Decrypt(encoded_string)
        print(decryptor.result)
