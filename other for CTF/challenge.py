from N1ES import N1ES
import base64
key = b"wxy191iss00000000000cute"
n1es = N1ES(key)
flag = "N1CTF{*****************************************}"
cipher = n1es.encrypt(flag)
print(len(key))
print (base64.b64encode(cipher))
print(base64.b64decode('HRlgC2ReHW1/WRk2DikfNBo1dl1XZBJrRR9qECMNOjNHDktBJSxcI1hZIz07YjVx'))
print(N1ES.decrypt(base64.b64decode('HRlgC2ReHW1/WRk2DikfNBo1dl1XZBJrRR9qECMNOjNHDktBJSxcI1hZIz07YjVx')))

