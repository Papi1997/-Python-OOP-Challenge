
#PET.PY

class Pet:
    def __init__(self, name, hunger=5, energy=5, happiness=5):

        """
        Constructor to initialize a new Pet instance.

        Args:
            name (str): Name of the pet.
            hunger (int): Starting hunger level (0 = full, 10 = starving).
            energy (int): Starting energy level (0 = exhausted, 10 = fully rested).
            happiness (int): Starting happiness level (0 = sad, 10 = very happy).
        """

        self.name = name
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness
        self.tricks = []  # Stores all tricks learned by the pet

    def eat(self):
    
        """
        Feed the pet. Reduces hunger and increases happiness.
        - Hunger decreases by 3 points, but not below 0.
        - Happiness increases by 1, up to a maximum of 10.
        """
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating. Hunger: {self.hunger}/10 | Happiness: {self.happiness}/10")


    def sleep(self):

        """
        Let the pet sleep. Increases energy.
        - Energy increases by 5, but not above 10.
        """


        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping. Energy: {self.energy}/10") # Using f-string formatting

    def play(self):

        """
        Play with the pet.
        - Decreases energy by 2 (if enough energy).
        - Increases happiness by 2, up to 10.
        - Increases hunger by 1, up to 10.
        """

        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} is playing. Energy: {self.energy}/10 | Happiness: {self.happiness}/10 | Hunger: {self.hunger}/10")
        else:
            print(f"{self.name} is too tired to play. Try sleeping first!")

    def get_status(self):

        """
        Display the current status of the pet: hunger, energy, and happiness.
        """
        print(f"\n {self.name}'s Current Status:")
        print(f"  Hunger:    {self.hunger}/10")
        print(f"  Energy:    {self.energy}/10")
        print(f"  Happiness: {self.happiness}/10")

    def train(self, trick):
        """
        Teach your pet a new trick.
        - Adds the trick to the tricks list.
        - Increases happiness by 1 (up to 10).
        
        Args:
            trick (str): Name of the trick being taught.
        """
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} learned a new trick: '{trick}'! Happiness: {self.happiness}/10")

    def show_tricks(self):
    
        """
        Show a list of all tricks the pet has learned.
        """
        
        print(f"\n Tricks that {self.name} knows:")
        if self.tricks:
            for trick in self.tricks:
                print(f"  - {trick}")
        else:
            print(f"  {self.name} hasn't learned any tricks yet.")





