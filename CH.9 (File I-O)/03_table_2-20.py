import os

# Create the folder if it doesn't exist
folder_name = "Tables for 13-year-old"
os.makedirs(folder_name, exist_ok=True)

# Loop through tables from 2 to 20
for i in range(2, 21):
    filename = f"{folder_name}/Table of {i}.txt"
    with open(filename, "w") as f:
        # Write the multiplication table of i
        f.write(f"Multiplication Table of {i}\n")
        f.write("=" * 25 + "\n")
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i*j}\n")

print("Multiplication tables from 2 to 20 have been written to the folder successfully!")
