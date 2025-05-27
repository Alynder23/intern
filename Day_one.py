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
print(average_mood)

#longest entry
longest_entry=[name, dob, colour, meal, hobby, new_mood, average_mood]
print(longest_entry)
word_count=len(longest_entry)
print("word_count")