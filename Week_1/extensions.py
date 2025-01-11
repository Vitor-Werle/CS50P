def main():
    question = input("Format: ")
    question = question.strip().lower()
    convert(question)

def convert(input):
    if input.endswith((".jpg", ".jpeg")):
        print("image/jpeg")
    elif input.endswith(".gif"):
        print("image/gif")
    elif input.endswith(".png"):
        print("image/png")
    elif input.endswith(".pdf"):
        print("application/pdf")
    elif input.endswith(".txt"):
        print("text/plain")
    elif input.endswith(".zip"):
        print("application/zip")
    else:
        print("Formato desconhecido")

main()
