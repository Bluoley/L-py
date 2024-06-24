import random
import hangman_art

word_list = ["blusito", "plebes", "yelito", "bluoley"]
print(hangman_art.logo)
random_word = random.choice(word_list)
final_word = list(random_word)

output = []
for _ in range(len(final_word)):
    output.append("_")

print(f"{' '.join(output)}")
isOver = False
fail = 7

while isOver != True:
    letter_input = input("\nType a letter: ").lower()

    for index, letter in enumerate(final_word):
        if letter == letter_input:
            output[index] = letter_input

        if not "_" in output:
            isOver = True
            print("You Win")

    if not letter_input in final_word:
        print(hangman_art.stages[fail - 1])
        fail -= 1

        if (fail == 0):
            isOver = True
            print("You Lose")

    print(f"\n{' '.join(output)}")
