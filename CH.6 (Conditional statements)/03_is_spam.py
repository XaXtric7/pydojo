# List of spam phrases (in lowercase)
spam_keywords = ["make a lot of money",
                 "buy now", "subscribe this", "click this"]

# Take comment input from the user
comment = input("Enter the comment: ").lower()

# Check if any spam phrase is in the comment
is_spam = False
for phrase in spam_keywords:
    if phrase in comment:
        is_spam = True
        break

# Print result
if is_spam:
    print("This is a spam comment.")
else:
    print("This is not a spam comment.")
