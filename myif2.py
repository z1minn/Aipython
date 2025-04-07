def show_ascii_art(choice):
    if choice == "1":
        print("""
     O
    /|\\
    / \\
    사람
    """)
    elif choice == "2":
        print("""
    [===]
   | 0 0 |
   |  ^  |
   | '-' |
   |_____|
   로봇
    """)
    elif choice == "3":
        print("""
    /\\_/\\
   ( o.o )
    > ^ <
    고양이
    """)
    else:
        print("잘못된 입력입니다. 1, 2, 3 또는 0을 입력하세요.")

def main():
    while True:
        print("\n원하는 캐릭터를 선택하세요:")
        print("1. 사람")
        print("2. 로봇")
        print("3. 고양이")
        print("0. 종료")
        choice = input("입력: ")

        if choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            show_ascii_art(choice)

if __name__ == "__main__":
    main()
