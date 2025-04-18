class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        # Decrease hunger by 3 but not below 0
        self.hunger = max(0, self.hunger - 3)        
        self.happiness = min(10, self.happiness + 1)  # Increase happiness by 1
        print(f"{self.name} eats and feels happier!")
    def sleep(self):
        # Increases energy by 5 points (but not above 10)
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} sleeps and feels more energetic!")
    def play(self):
        if self.energy > 0: # Check if the pet has enough energy to play
            # Decrease energy by 2, increase happiness by 2, and hunger by 1
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} plays and has fun!")
        else:
            print(f"{self.name} is too tired to play.") 
    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows the trick: {trick}.")
    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} doesn't know any tricks yet.")
    def get_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        print(f"Tricks: {', '.join(self.tricks) if self.tricks else 'None'}")

# Example usage
if __name__ == "__main__":
    pet = Pet("Buddy")
    pet.get_status()
    pet.eat()
    pet.sleep()
    pet.play()
    pet.train("Roll Over")
    pet.show_tricks()
    pet.get_status()