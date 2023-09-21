import random
weed = ["Blueberry kush", "Pineapple OG", "Sour Apple", "Cinnamon Stix"]
type_weed = ["Flower", "Concentrate", "Edible", "Tincture", "Live Resin"]
people = ["Mark", "Cannon", "Chris", "John", "May"]

random_people = random.choice(people)
random_weed = random.choice(weed)
random_type_weed = random.choice(type_weed)

print(f"{random_people} purchased the {random_weed} za in tha {random_type_weed} form!")
