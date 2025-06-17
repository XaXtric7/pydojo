# Replace all occurrences of "Donkey" with "#####"

# Enter the filename (make sure the file exists in the same directory)
file_name = "example.txt"  # Replace with your actual file name

# Open and read the content
with open(file_name, 'r') as file:
    content = file.read()

# Replace the word
updated_content = content.replace("Donkey", "#####")

# Write the updated content back to the same file
with open(file_name, 'w') as file:
    file.write(updated_content)

print("All occurrences of 'Donkey' have been replaced with '#####'.")
