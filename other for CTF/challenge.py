from N1ES import N1ES
import base64
key = "wxy191iss00000000000cute"
n1es = N1ES(key)
flag = "N1CTF{F3istel_n3tw0rk_c4n_b3_ea5i1y_s0lv3d_/--/}"
cipher = bytes(n1es.encrypt(flag),encoding = "utf8")
print(str(base64.b64encode(cipher),encoding = "utf8"))
print(n1es.decrypt(str(base64.b64decode(b'HRlgC2ReHW1/WRk2DikfNBo1dl1XZBJrRR9qECMNOjNHDktBJSxcI1hZIz07YjVx'),encoding = "utf8")))
