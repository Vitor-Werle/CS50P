import sys
import pyfiglet
import random

def main():
    args = parse_arguments()
    fonts = get_available_fonts()
    font = select_font(args, fonts)
    text = get_user_input()
    ascii_art = generate_ascii_art(text, font, fonts)
    print(ascii_art)

def parse_arguments():
    """Verifica os argumentos da linha de comando."""
    args = sys.argv[1:]
    if len(args) not in [0, 2]:
        sys.exit("Usage: python figlet.py [-f FONT | --font FONT]")
    return args

def get_available_fonts():
    """Retorna a lista de fontes disponíveis."""
    return pyfiglet.getFonts()

def select_font(args, fonts):
    """Seleciona a fonte com base nos argumentos fornecidos."""
    if len(args) == 2:
        if args[0] in ["-f", "--font"] and args[1] in fonts:
            return args[1]
        else:
            sys.exit("Invalid font or usage. Use: python figlet.py [-f FONT | --font FONT]")
    return None

def get_user_input():
    """Solicita o texto ao usuário."""
    return input("Input: ")

def generate_ascii_art(text, font, fonts):
    """Gera a arte ASCII com a fonte desejada ou uma fonte aleatória."""
    if font:
        return pyfiglet.figlet_format(text, font=font)
    else:
        random_font = random.choice(fonts)
        return pyfiglet.figlet_format(text, font=random_font)

if __name__ == "__main__":
    main()
