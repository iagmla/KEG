''' KEG-H Hash Function and Message Authentication Code '''
''' Kolor Encryption Gate - Hash '''
''' by KryptoMagick (Karl Zander) '''

class KEGH:
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

    def pickup(self):
        for x in range(len(self.discard)):
            self.deck.append(self.discard.pop(0))

    def key_scheduler(self):
        for x in range(52):
            self.step()

    def hash_letter(self, letter):
        # Perform the key scheduler
        self.key_scheduler()
        # Step the encryption pile
        self.step()
        # Convert the letter to number 0-25
        num = ord(letter) - 65
        # If the card in the N-th (0-26) position is equal to the gate color
        # Pull that card and place it at the rear of the deck
        # If not, pull the card in the N-th + N place and place it at the rear 
        if self.values[self.deck[num]][1] == self.gate_color:
            self.deck.append(self.deck.pop(num))
        else:
            self.deck.append(self.deck.pop(num + num))

    def digest(self, letters):
        h = []
        for x in range(len(letters)):
            letter = self.hash_letter(letters[x])
        # Pickup the discard pile and place it at the rear
        self.pickup()
        # Convert the hash deck to A-Z letters
        # Or leave them 0-51 values, your choice
        for x in range(52):
            card_value = self.values[self.deck[x]][0]
            h.append(chr(card_value + 65))
        return "".join(h)
