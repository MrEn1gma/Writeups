from Cryptodome.Cipher import ARC4

arc4_key = b"r4ns0mw@rE_c4n_d357r0y_f1l3s_n0w"
arc4_cipher = open("IOC\\user.html.enc", "rb").read()
arc4_init = ARC4.new(arc4_key)
out = arc4_init.decrypt(arc4_cipher)
open("flag\\user.html", "wb").write(out)

print("OK !!!")
