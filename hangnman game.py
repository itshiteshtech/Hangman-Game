import random

# Categories
categories = {
    "animals": ["tiger", "elephant", "giraffe"],
    "fruits": ["apple", "banana", "mango"],
    "programming": ["python", "java", "coding"]
}

# Choose category
print("Choose Category:")
for key in categories:
    print("-", key)

category = input("Enter category: ").lower()

if category not in categories:
    print("Invalid category! Default: animals")
    category = "animals"

word = random.choice(categories[category])

guessed_letters = []
lives = 5
score = 0

# Display word
def display_word():
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

# Game loop
while lives > 0:
    print("\nWord:", display_word())
    print("Lives:", lives, " Score:", score)

    choice = input("Enter letter or type 'hint': ").lower()

    # Hint system
    if choice == "hint":
        for letter in word:
            if letter not in guessed_letters:
                guessed_letters.append(letter)
                score -= 5
                print("Hint used! Letter revealed:", letter)
                break
        continue

    if len(choice) != 1 or not choice.isalpha():
        print("Enter a single letter!")
        continue

    if choice in guessed_letters:
        print("Already guessed!")
        continue

    guessed_letters.append(choice)

    if choice in word:
        print("Correct 👍")
        score += 10
    else:
        print("Wrong ❌")
        lives -= 1
        score -= 5

    # Win check
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 You Win!")
        print("Word was:", word)
        print("Final Score:", score)
        break

# Lose condition
if lives == 0:
    print("\n😢 You Lose!")
    print("Word was:", word)