def load_story(filename="story"):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print("❌ Error: 'story' file not found.")
        return None


def extract_placeholders(story):
    words = set()
    start_of_word = -1
    for i, char in enumerate(story):
        if char == "{":
            start_of_word = i
        elif char == "}" and start_of_word != -1:
            word = story[start_of_word : i + 1]
            words.add(word)
            start_of_word = -1
    return sorted(words)  # ensures consistent order


def get_input_for(word):
    prompt = word.strip("{}").replace("_", " ").capitalize()
    while True:
        user_input = input(f"Enter a {prompt}: ").strip()
        if user_input:
            return user_input
        print("Input cannot be blank.")


def play_madlibs():
    story_template = load_story()
    if story_template is None:
        return

    while True:
        story = story_template[:]  # fresh copy
        placeholders = extract_placeholders(story)
        answers = {word: get_input_for(word) for word in placeholders}

        for word, replacement in answers.items():
            story = story.replace(word, replacement)

        print("\n📝 Here's your story:\n")
        print(story)

        # Optional: Save to file
        save = input("\nWould you like to save the story to a file? (y/n): ").lower()
        if save == "y":
            with open("madlib_output.txt", "w") as f:
                f.write(story)
            print("✅ Story saved to madlib_output.txt")

        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != "y":
            break


play_madlibs()
