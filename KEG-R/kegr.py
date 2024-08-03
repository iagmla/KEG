''' KEG-R Cipher '''
''' Karl's Encryption Gate (Revised) '''
''' Improved KEG Cipher '''
''' by KryptoMagick (Karl Zander) '''

class KEG:
    def __init__(self):
        self.values = {}
        self.discard = []
        suit = 0
        for x in range(52):
            if x % 13 == 0 and x != 0:
                suit += 1
            self.values[x] = (x % 26, suit, x)

    def key(self, key):
        # Set the deck to equal numbers 0-51
        self.deck = list(key)
        # Set the gate suit to be the suit
        # Of the first card in the deck
        self.gate_suit = self.values[self.deck[0]][1]
        #print(self.gate_suit)
        self.gate_card = self.values[self.deck[0]][0] % 13

    def step(self):
        step_card_index = 1
        crypt_card_index = 0
        card_values = self.values[self.deck[step_card_index]]
        step_value = card_values[2]
        card_suit = card_values[1]
        if card_suit == self.gate_suit and len(self.discard) != 0:
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
        #print(len(self.deck), len(self.discard))
        return chr(((num + self.values[self.deck[0]][0]) % 26) + 65)

    def decrypt_letter(self, letter):
        # Step the encryption pile
        self.step()
        # Convert the letter to number 0-25
        num = ord(letter) - 65
        # Decipher the letter
        #print(len(self.deck), len(self.discard))
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
