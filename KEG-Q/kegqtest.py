from kegq import KEGQ

keyA = [12, 47, 4, 27, 42, 21, 23, 8, 1, 30, 50, 0, 31, 22, 25, 28, 48, 34, 19, 13, 6, 41, 44, 24, 9, 33, 43, 3, 15, 29, 5, 7, 26, 45, 11, 2, 16, 20, 18, 36, 17, 46, 51, 37, 14, 35, 49, 10, 39, 32, 40, 38]
keyB = [14, 28, 17, 9, 0, 30, 7, 42, 22, 26, 40, 13, 16, 19, 5, 37, 2, 31, 25, 44, 41, 48, 21, 23, 49, 32, 36, 6, 24, 38, 51, 20, 18, 43, 29, 15, 45, 8, 12, 35, 1, 4, 11, 27, 34, 33, 3, 50, 47, 46, 10, 39]
qkegA = KEGQ()

msg = "LETUSPLAYKEGTOGETHER"
ctxt = qkegA.encrypt(msg, keyA, keyB)
print(ctxt)
qkegB = KEGQ()

ptxt = qkegB.decrypt(ctxt, keyA, keyB)
print(ptxt)
