from Crypto.Util.number import bytes_to_long
from Crypto.Util.number import long_to_bytes

base10 = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
flag = long_to_bytes(base10)
print(flag)