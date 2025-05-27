print("WELCOME TO YOUR SMART DIARY")
name=input("Enter your name:")
print(f"Hello {name}")
dob=input("Your date of birth:")
colour=input("What is your favorite colour?")
meal=input("What is your favourite dish?")
hobby=input("what is your hobby?")
print(f"{name} was born on {dob}")
print(f"She loves colour {colour}, her favorite meal is {meal}, and she likes to {hobby}.")

mood=input("what's your mood?(1-10):")
new_mood=int(mood)

#diary_entry
diary_entry=[name, dob, colour, meal, hobby, mood]
print(diary_entry)
average_mood=new_mood/3
print(f"average_mood: {average_mood:.2f}")


longest_entry = max(diary_entry, key=len)

print("The longest entry is:", longest_entry)

word_counts = [len(entry.split()) for entry in diary_entry]

for entry, count in zip(diary_entry, word_counts):
    print(f"'{entry}' has {count} words.")

print('allan')