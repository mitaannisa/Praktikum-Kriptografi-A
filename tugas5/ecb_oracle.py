import requests 
# f = open("out.txt","w")
def char_to_hex(txt):
    u = format(txt, "x")
    if(len(u)==1): 
        u='0'+u
    return u
BASE_URL = "http://aes.cryptohack.org/ecb_oracle"
list_64 = []
for i in range(1,33):
    r = requests.get(f"{BASE_URL}/encrypt/{'aa'*i}")
    data = r.json()
    ciphertext = data["ciphertext"]
    list_64.append(ciphertext)
    # f.write(ciphertext+'\n')
pre_cipher = []
for i in range(0,32):
    pre_cipher.append(list_64[i][:64])
flag_cipher = list_64[31][64:128]
# for _ in pre_cipher:
#     print(_)
print(flag_cipher)
res = ""
plaintext = 'a'*64
for _ in range(0,31):
    root = plaintext[2:64]
    for ch in range(32,127):
        current_char = char_to_hex(ch)
        plaintext_send = root + current_char
        # print(plaintext_send)
        r = requests.get(f"{BASE_URL}/encrypt/{plaintext_send}")
        data = r.json()
        ciphertext = data["ciphertext"][:64]
        # print("aka1: ",ciphertext)
        # print("aka2: ",pre_cipher[15-(_+1)])
        if(ciphertext==pre_cipher[31-(_+1)]):
            res=res+chr(ch)
            plaintext = plaintext_send 
            print(res)
            break

print(res)