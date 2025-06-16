fav_lang = {}  # Empty dictionary

for i in range(4):
    name = input(f"Enter friend {i+1}'s name: ")
    language = input(f"Enter {name}'s favorite programming language: ")
    fav_lang[name] = language  # Store name as key and language as value

print("\nFavorite Languages Dictionary:")
print(fav_lang)
