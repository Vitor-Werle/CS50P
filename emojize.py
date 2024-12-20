import emoji

user_input = input("Input: ")

convert_text = emoji.emojize(user_input, language="alias")

print(f"Output: {convert_text}")