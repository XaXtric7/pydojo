def game():
    # Simulate playing a game and returning a score
    score = int(input("Enter your score: "))
    return score


# Get the current score
current_score = game()

# Try to read the previous high score
try:
    with open("D:\Sarthak\VScode workshop\Python(py) Files\CWH\CH.9 (File I-O)\Hi-score.txt", "r") as file:
        content = file.read()
        if content.strip() == "":
            high_score = 0
        else:
            high_score = int(content)
except FileNotFoundError:
    high_score = 0

# Compare and update if new score is higher
if current_score > high_score:
    print("Congratulations! New high score!")
    with open("Hi-score.txt", "w") as file:
        file.write(str(current_score))
else:
    print(f"Your score: {current_score}. High score remains: {high_score}")
