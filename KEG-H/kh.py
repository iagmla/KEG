from kegh import KEGH

msg = "A"
key = list(range(52))
kh = KEGH()
kh.key(key)
h = kh.digest(msg)
print(h)
