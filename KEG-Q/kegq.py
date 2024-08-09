''' KEG-Q Cipher '''
''' Kolor Encryption Gate '''
''' Quantum Safe '''
''' by KryptoMagick (Karl Zander) '''

class KEG:
    def __init__(self):
        self.values = {}
        self.discard = []
        color = 0
        for x in range(52):
            if x % 26 == 0 and x != 0:
                color += 1
            self.values[x] = (x % 26, color, x)

    def key(self, key):
        # Set the deck to equal numbers 0-51
        self.deck = list(key)
        # Set the gate color to be the color
        # Of the first card in the deck
        self.gate_color = self.values[self.deck[0]][1]

    def step(self):
        step_card_index = 1
        crypt_card_index = 0
        card_values = self.values[self.deck[step_card_index]]
        step_value = card_values[2]
        card_color = card_values[1]
        if card_color == self.gate_color and len(self.discard) != 0:
            for x in range(len(self.discard)):
                self.deck.append(self.discard.pop(0))
        # Discard the stepping card
        self.discard.append(self.deck.pop(step_card_index))
        # Step the encryption deck by removing the first card
        # Place it in the rear
        self.deck.append(self.deck.pop(crypt_card_index))
        # Step the encryption deck by the stepping value
        # Removing the first card and place it in the rear
        # Repeat until the stepping value has been reached
        for x in range(step_value):
            self.deck.append(self.deck.pop(crypt_card_index))

    def key_scheduler(self):
        for x in range(52):
            self.step()

    def encrypt_letter(self, letter):
        # Step the encryption pile
        self.step()
        # Convert the letter to number 0-25
        num = ord(letter) - 65
        # Encipher the letter
        return chr(((num + self.values[self.deck[0]][0]) % 26) + 65)

    def decrypt_letter(self, letter):
        # Step the encryption pile
        self.step()
        # Convert the letter to number 0-25
        num = ord(letter) - 65
        # Decipher the letter
        return chr(((num - self.values[self.deck[0]][0]) % 26) + 65)

    def encrypt(self, letters, ksa=False):
        ctxt = []
        if ksa:
            self.key_scheduler()
        for x in range(len(letters)):
            letter = self.encrypt_letter(letters[x])
            ctxt.append(letter)
        return "".join(ctxt)

    def decrypt(self, letters, ksa=False):
        ptxt = []
        if ksa:
            self.key_scheduler()
        for x in range(len(letters)):
            letter = self.decrypt_letter(letters[x])
            ptxt.append(letter)
        return "".join(ptxt)

class KEGQ:
    def encrypt(self, letters, keyA, keyB):
        kegA = KEG()
        kegA.key(keyA)
        kegB = KEG()
        kegB.key(keyB)
        ctxt = []
        for x in range(len(letters)):
            letter = kegA.encrypt(letters[x])
            letter = kegB.encrypt(letter)
            ctxt.append(letter)
        return "".join(ctxt)

    def decrypt(self, letters, keyA, keyB):
        kegA = KEG()
        kegA.key(keyA)
        kegB = KEG()
        kegB.key(keyB)
        ptxt = []
        for x in range(len(letters)):
            letter = kegA.decrypt(letters[x])
            letter = kegB.decrypt(letter)
            ptxt.append(letter)
        return "".join(ptxt)
