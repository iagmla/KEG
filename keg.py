''' KEG Cipher '''
''' Kolor Encryption Gate '''
''' by KryptoMagick (Karl Zander) '''

class KEG:
    def __init__(self):
        self.values = {}
        self.discard = []
        suit = 0
        value = 0
        for x in range(52):
            if x % 13 == 0 and x != 0:
                suit += 1
            self.values[x] = (value, suit)
            value = (value + 1) % 26

    def key(self, key):
        # Set the deck to equal numbers 0-51
        self.deck = list(key)
        # Set the gate suit to be the suit
        # Of the first card in the deck
        self.suit = self.values[self.deck[0]][1]

    def step(self):
        values = self.values[self.deck[1]]
        step_value = values[0]
        # If the stepping card equals the gate suit
        # Move the dicard pile to the rear of the encryption pile
        if values[1] == self.suit and len(self.discard) != 0:
            for x in range(len(self.discard)):
                self.deck.append(self.discard.pop(0))
            # Discard the stepping card
            self.discard.append(self.deck.pop(1))
        else:
            # Discard the stepping card
            self.discard.append(self.deck.pop(1))
        # Step the encryption deck by removing the first card
        # Place it in the rear
        self.deck.append(self.deck.pop(0))
        # Step the encryption deck by the stepping value
        # Removing the first card and place it in the rear
        # Repeat until the stepping value has been reached
        for x in range(step_value):
            self.deck.append(self.deck.pop(0))

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

    def encrypt(self, letters):
        ctxt = []
        for x in range(len(letters)):
            letter = self.encrypt_letter(letters[x])
            ctxt.append(letter)
        return "".join(ctxt)

    def decrypt(self, letters):
        ptxt = []
        for x in range(len(letters)):
            letter = self.decrypt_letter(letters[x])
            ptxt.append(letter)
        return "".join(ptxt)
