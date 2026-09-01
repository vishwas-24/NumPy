# Pythong file dectection

import os

file_path = "myself.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

else:
    print("That location don't exists")