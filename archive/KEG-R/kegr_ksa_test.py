from kegr import KEG

key = list(range(52))
ekeg = KEG()
ekeg.key(key)

msg = "LETUSPLAYKEGTOGETHER"
ctxt = ekeg.encrypt(msg, ksa=True)
print(ctxt)
dkeg = KEG()
dkeg.key(key)

ptxt = dkeg.decrypt(ctxt, ksa=True)
print(ptxt)
