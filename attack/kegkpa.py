from kegtest import KEG

''' Demonstrate Resistance to Known Plaintext Attacks '''

kpa_length = 52
known_plaintext = "HELLOWORLDIAMUSINGTHEKEGCIPHERPLEASEATTACKMEANDTHEVI"
print("Known Plaintext:", known_plaintext)
ctxt = "KNGEEHQCKJLYRIZYAHPQLSTKFGJWCTOZPKRRTIZJWXBBGDNSVYGOOCKUDZGQKERFYTZPQJPXVIDEINFISTN"
print("Ciphertext:", ctxt)

known_key_stream = []
for x in range(kpa_length):
    ctxt_num = ord(ctxt[x]) - 65
    msg_num = ord(known_plaintext[x]) - 65
    ks_num = (ctxt_num - msg_num) % 26
    known_key_stream.append(ks_num)

print("Known Key Stream:", known_key_stream)
ka = KEG()
ka.key(known_key_stream)

unknown_ctxt = ""
for x in range(kpa_length, len(ctxt)):
    unknown_ctxt += ctxt[x]

possible_ptxt = ka.decrypt(unknown_ctxt)
print("Possible Plaintext:", possible_ptxt)
