from datetime import datetime

# Validate name and other text inputs (letters only)
def get_valid_text(prompt):
    while True:
        text = input(prompt)
        if text.replace(" ", "").isalpha():
            return text
        print("❌ Please enter letters only (no numbers or symbols).")

# Validate date in dd/mm/yyyy format
def get_valid_dob():
    while True:
        dob = input("Your date of birth (dd/mm/yyyy): ")
        try:
            valid_dob = datetime.strptime(dob, "%d/%m/%Y")
            return valid_dob.strftime("%d/%m/%Y")
        except ValueError:
            print("❌ Invalid format. Please use dd/mm/yyyy.")

# Validate mood between 1 and 10
def get_valid_mood():
    while True:
        mood = input("What's your mood? (1-10): ")
        try:
            mood = int(mood)
            if 1 <= mood <= 10:
                return mood
            else:
                print("❌ Mood must be a number between 1 and 10.")
        except ValueError:
            print("❌ Please enter a numeric value.")

# Save diary entry to a text file, one line per field
def save_to_txt(filename, entry_data):
    with open(filename, 'a') as file:
        file.write(f"Name: {entry_data['Name']}\n")
        file.write(f"DOB: {entry_data['DOB']}\n")
        file.write(f"Color: {entry_data['Color']}\n")
        file.write(f"Meal: {entry_data['Meal']}\n")
        file.write(f"Hobby: {entry_data['Hobby']}\n")
        file.write(f"Mood: {entry_data['Mood']}\n")
        file.write(f"Average Mood: {entry_data['AverageMood']:.2f}\n")
        file.write(f"Longest Entry: {entry_data['LongestEntry']}\n")
        file.write("-" * 30 + "\n")  # Separator line

# Welcome
print("📝 WELCOME TO YOUR SMART DIARY 📝\n")

# Inputs
name = get_valid_text("Enter your name: ")
print(f"\nHello {name}!\n")

dob = get_valid_dob()
colour = get_valid_text("What is your favorite colour? ")
meal = get_valid_text("What is your favourite dish? ")
hobby = get_valid_text("What is your hobby? ")
mood = get_valid_mood()

# Diary entry list
diary_entry = [name, dob, colour, meal, hobby, str(mood)]

# Output summary
print(f"\n{name} was born on {dob}.")
print(f"{name} loves colour {colour}, enjoys eating {meal}, and likes to {hobby}.")
print(f"Mood rating: {mood}/10")

# Average mood (example)
average_mood = mood / 3
print(f"Calculated average mood: {average_mood:.2f}")

# Longest
longest_entry = max(diary_entry, key=len)
print("\n📌 Longest entry:", longest_entry)

# Word counts
print("\n📌 Word Counts:")
word_counts = [len(entry.split()) for entry in diary_entry]
for entry, count in zip(diary_entry, word_counts):
    print(f"'{entry}' has {count} word(s).")

# Save entry
entry_data = {
    "Name": name,
    "DOB": dob,
    "Color": colour,
    "Meal": meal,
    "Hobby": hobby,
    "Mood": mood,
    "AverageMood": average_mood,
    "LongestEntry": longest_entry
}

save_to_txt("smart_diary.txt", entry_data)

# Append the special sentence with proper encoding
with open("smart_diary.txt", 'a', encoding="utf-8") as file:
    file.write("This is my happy diary 😊\n")
    file.write("=" * 30 + "\n\n")

# Read and display the contents of the diary file
print(f"\n✅ Diary entry saved to 'smart_diary.txt'.")
print(f"\n📖 Here's what's in your diary now:\n")

with open("smart_diary.txt", 'r', encoding="utf-8") as file:
    content = file.read()
    print(content)

print(f"Have a nice day, {name}! 🌟")