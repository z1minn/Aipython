from colorama import Fore, Style, init
init(autoreset=True)

def show_ascii_art(choice):
    if choice == "1":
        print(Fore.YELLOW + """
     O
    /|\\
    / \\
    사람
    """)
    elif choice == "2":
        print(Fore.CYAN + """
    [===]
   | 0 0 |
   |  ^  |
   | '-' |
   |_____|
   로봇
    """)
    elif choice == "3":
        print(Fore.MAGENTA + """
    /\\_/\\
   ( o.o )
    > ^ <
    고양이
    """)
    else:
        print(Fore.RED + "잘못된 입력입니다. 1, 2, 3 또는 0을 입력하세요.")

from colorama import Fore
from wcwidth import wcswidth

def print_table_menu(options, title="메뉴"):
    total_width = 36  # 내부 내용 너비
    border_color = Fore.GREEN
    text_color = Fore.BLUE

    # 위 테두리
    print(border_color + "┌" + "─" * total_width + "┐")

    # 제목 중앙 정렬 (한글 포함 고려)
    title_width = wcswidth(title)
    left_padding = (total_width - title_width) // 2
    right_padding = total_width - title_width - left_padding
    print(border_color + f"│{' ' * left_padding}{title}{' ' * right_padding}│")

    # 구분선
    print(border_color + "├" + "─" * total_width + "┤")

    # 항목 출력
    for key, value in options.items():
        prefix = f"  {key}. "
        prefix_width = wcswidth(prefix)
        value_width = wcswidth(value)
        padding = total_width - (prefix_width + value_width)
        print(text_color + f"│{prefix}{value}{' ' * padding}│")

    # 하단 테두리
    print(border_color + "└" + "─" * total_width + "┘")



def select_character_loop(max_count=None):
    count = 0
    while True:
        if max_count is not None and count >= max_count:
            print(Fore.YELLOW + f"{max_count}번의 선택이 끝났습니다. 프로그램을 종료합니다.")
            break

        if max_count is not None:
            print(f"\n({count + 1}/{max_count}) 캐릭터 선택")
        else:
            print("\n캐릭터 선택")

        options = {
            "1": "사람",
            "2": "로봇",
            "3": "고양이",
            "0": "종료"
        }
        print_table_menu(options, title="캐릭터 선택 메뉴")
        choice = input("입력: ")

        if choice == "0":
            print(Fore.YELLOW + "프로그램을 종료합니다.")
            break
        else:
            show_ascii_art(choice)
            if max_count is not None:
                count += 1

def main():
    options = {
        "1": "5번 선택 모드",
        "2": "무한 선택 모드 (0 입력 시 종료)"
    }
    print_table_menu(options, title="모드 선택")
    mode = input("입력: ")

    if mode == "1":
        select_character_loop(max_count=5)
    elif mode == "2":
        select_character_loop()
    else:
        print(Fore.RED + "잘못된 입력입니다. 프로그램을 종료합니다.")

if __name__ == "__main__":
    main()
