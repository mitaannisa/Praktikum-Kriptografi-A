from Crypto.Util.strxor import strxor
import requests

ciphertext = bytes.fromhex(requests.get("https://aes.cryptohack.org/bean_counter/encrypt/").json()["encrypted"])
es = "89504e470d0a1a0a0000000d49484452"

key = strxor(ciphertext[:16], bytes.fromhex(es)) 

last_eleven_bytes = b"\xa2&\x08\xe6\xb8\xf6\x91\x14\xff\xd3/"
decrypted_last_eleven = strxor(key[:11], last_eleven_bytes)

with open("png.exe.png.exe.png", "wb") as f:
    i = 0
    block = ciphertext[i:i+16]
    while block:
        f.write(strxor(block, key) if len(block) == 16 else decrypted_last_eleven)
        i += 16
        block = ciphertext[i:i+16]