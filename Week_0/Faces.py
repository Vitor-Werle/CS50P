def main():
    emotion = input("")
    print(convert_emotion(emotion))

def convert_emotion(emotion):
    return emotion.replace(":)", "🙂").replace(":(", "🙁")

main()