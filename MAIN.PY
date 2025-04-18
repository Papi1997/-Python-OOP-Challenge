#MAIN.PY

from pet import Pet

# ---------------------------
# Create Pet Instances
# ---------------------------

# Pet with default values (hunger=5, energy=5, happiness=5)
pet1 = Pet("Buddy")

# Pet with custom starting values
pet2 = Pet("Luna", hunger=3, energy=8, happiness=9)

# ---------------------------
# Interactions with Buddy
# ---------------------------

print("\n Interacting with Buddy:")

# Show Buddy's starting state
pet1.get_status()

# Feed Buddy (lowers hunger, raises happiness)
pet1.eat()

# Let Buddy take a nap (boosts energy)
pet1.sleep()

# Play with Buddy (uses energy, raises happiness, raises hunger)
pet1.play()

# Teach Buddy a new trick
pet1.train("Sit")

# Show all the tricks Buddy knows
pet1.show_tricks()

# Display updated status after interactions
pet1.get_status()

# ---------------------------
# Interactions with Luna
# ---------------------------

print("\n Interacting with Luna:")

# Show Luna's custom starting state
pet2.get_status()

# Play with Luna
pet2.play()

# Teach Luna multiple tricks
pet2.train("High Five")
pet2.train("Roll Over")

# Show Luna’s learned tricks
pet2.show_tricks()

# Display Luna's final status
pet2.get_status()
