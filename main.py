import random
import requests
import shutil
import os


def generate_roblox_card():
    prefix = "ROBLOX-"
    suffix = "".join(random.choices("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=10))
    return prefix + suffix


def generate_amazon_card():
    prefix = "AMAZON-"
    suffix = "".join(random.choices("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=10))
    return prefix + suffix


def generate_valorant_card():
    prefix = "VALORANT-"
    suffix = "".join(random.choices("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=10))
    return prefix + suffix


def generate_league_of_legends_card():
    prefix = "LOL-"
    suffix = "".join(random.choices("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=10))
    return prefix + suffix


def generate_gift_card(card_type):
    if card_type == "1":
        return generate_roblox_card()
    elif card_type == "2":
        return generate_amazon_card()
    elif card_type == "3":
        return generate_valorant_card()
    elif card_type == "4":
        return generate_league_of_legends_card()
    else:
        return "Invalid card type"


def fetch_announcement():
    url = "https://raw.githubusercontent.com/blzsr/Secret/main/annc.txt"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.strip()
    else:
        return "Error fetching announcement"


def gradient_text(text, start_color, end_color):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    def interpolate(start, end, step, max_steps):
        return int(start + (end - start) * step / max_steps)

    gradient_text = ""
    for i, char in enumerate(text):
        r = interpolate(start_r, end_r, i, len(text))
        g = interpolate(start_g, end_g, i, len(text))
        b = interpolate(start_b, end_b, i, len(text))
        gradient_text += f"\033[38;2;{r};{g};{b}m{char}\033[0m"
    return gradient_text


def center_text(text):
    terminal_width = shutil.get_terminal_size().columns
    lines = text.split("\n")
    centered_lines = [line.center(terminal_width) for line in lines]
    return "\n".join(centered_lines)


def display_header(ascii_art, announcement, start_color, end_color):
    os.system("cls" if os.name == "nt" else "clear")
    print(gradient_text(center_text(ascii_art), start_color, end_color))
    print(gradient_text(center_text(announcement), start_color, end_color))


def main():
    start_color = (128, 0, 128)  # Purple
    end_color = (0, 0, 255)  # Blue

    ascii_art = """
  ██████  ██▀███   ▄████▄       ▄████  ██▓  █████▒▄▄▄█████▓ ▄████▄   ▄▄▄       ██▀███  ▓█████▄ 
▒██    ▒ ▓██ ▒ ██▒▒██▀ ▀█      ██▒ ▀█▒▓██▒▓██   ▒ ▓  ██▒ ▓▒▒██▀ ▀█  ▒████▄    ▓██ ▒ ██▒▒██▀ ██▌
░ ▓██▄   ▓██ ░▄█ ▒▒▓█    ▄    ▒██░▄▄▄░▒██▒▒████ ░ ▒ ▓██░ ▒░▒▓█    ▄ ▒██  ▀█▄  ▓██ ░▄█ ▒░██   █▌
  ▒   ██▒▒██▀▀█▄  ▒▓▓▄ ▄██▒   ░▓█  ██▓░██░░▓█▒  ░ ░ ▓██▓ ░ ▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██▀▀█▄  ░▓█▄   ▌
▒██████▒▒░██▓ ▒██▒▒ ▓███▀ ░   ░▒▓███▀▒░██░░▒█░      ▒██▒ ░ ▒ ▓███▀ ░ ▓█   ▓██▒░██▓ ▒██▒░▒████▓ 
▒ ▒▓▒ ▒ ░░ ▒▓ ░▒▓░░ ░▒ ▒  ░    ░▒   ▒ ░▓   ▒ ░      ▒ ░░   ░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒▓  ▒ 
░ ░▒  ░ ░  ░▒ ░ ▒░  ░  ▒        ░   ░  ▒ ░ ░          ░      ░  ▒     ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ▒  ▒ 
░  ░  ░    ░░   ░ ░           ░ ░   ░  ▒ ░ ░ ░      ░      ░          ░   ▒     ░░   ░  ░ ░  ░ 
      ░     ░     ░ ░               ░  ░                   ░ ░            ░  ░   ░        ░    
                  ░                                        ░                            ░      
"""

    announcement = fetch_announcement()

    terminal_width = shutil.get_terminal_size().columns
    box_top = "╭" + "─" * (terminal_width - 2) + "╮"
    box_bottom = "╰" + "─" * (terminal_width - 2) + "╯"

    menu_options = [
        "1. Generate Roblox Card",
        "2. Generate Amazon Card",
        "3. Generate Valorant Card",
        "4. Generate League of Legends Card",
        "5. Exit",
    ]

    while True:
        display_header(ascii_art, announcement, start_color, end_color)

        print(gradient_text(center_text("Menu"), start_color, end_color))
        print(gradient_text(box_top, start_color, end_color))
        for option in menu_options:
            print(gradient_text(option.center(terminal_width), start_color, end_color))
        print(gradient_text(box_bottom, start_color, end_color))

        choice = input(f"{gradient_text('╰───>', start_color, end_color)} ").strip()

        if choice == "5":
            print(gradient_text(center_text("Exiting..."), start_color, end_color))
            break
        elif choice in ["1", "2", "3", "4"]:
            print(
                gradient_text(
                    center_text("How many cards to generate?"), start_color, end_color
                ),
                end=" ",
            )
            num_cards = int(input().strip())
            cards = [generate_gift_card(choice) for _ in range(num_cards)]

            display_header(ascii_art, announcement, start_color, end_color)

            print(
                gradient_text(center_text("Generated Cards:"), start_color, end_color)
            )
            for card in cards:
                print(
                    gradient_text(card.center(terminal_width), start_color, end_color)
                )

            print(
                gradient_text(
                    center_text("Save to file? (y/n)"), start_color, end_color
                ),
                end=" ",
            )
            save_choice = input().strip().lower()

            if save_choice == "y":
                service_name = menu_options[int(choice) - 1].split()[2].lower()
                filename = f"{service_name}_cards.txt"
                with open(filename, "w") as f:
                    for card in cards:
                        f.write(card + "\n")
                print(
                    gradient_text(
                        center_text(f"Cards saved to {filename}"),
                        start_color,
                        end_color,
                    )
                )
            else:
                print(
                    gradient_text(
                        center_text("Cards not saved"), start_color, end_color
                    )
                )
        else:
            print(
                gradient_text(
                    center_text("Invalid selection, please choose a valid option."),
                    start_color,
                    end_color,
                )
            )


if __name__ == "__main__":
    main()
