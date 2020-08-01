import os
import random


os.makedirs("./data", exist_ok=True)

random_number = random.randint(0, 1000000)

with open(f"./data/{random_number}.txt", "w") as temp_file:
    temp_file.write(f"Hey, {random_number}")
