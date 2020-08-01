import random

random_number = random.randint(0, 1000000)

with open(f"./{random_number}.txt", "w") as temp_file:
    temp_file.write(f"Hey, {random_number}")
    print("Created file:", random_number)
