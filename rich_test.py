from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from rich.rule import Rule
from rich import box

console = Console()

def show_welcome_banner():
    banner = Text("""
  __                  ___       ___              
 /\ \                /\_ \     /\_ \             
 \ \ \___       __   \//\ \    \//\ \      ___   
  \ \  _ `\   /'__`\   \ \ \     \ \ \    / __`\  
   \ \ \ \ \ /\  __/    \_\ \_    \_\ \_ /\ \L\ \  
    \ \_\ \_\\ \____\   /\____\   /\____\\ \____/   
     \/_/\/_/ \/____/   \/____/   \/____/ \/___/    
""", style="bold cyan")
    console.print(banner)
    console.rule("[bold green]캐릭터 선택 프로그램[/bold green]")

def show_ascii_art(choice):
    if choice == "1":
        art = """
     O
    /|\\
    / \\
    사람
        """
        console.print(Panel.fit(art, title="사람", style="bold yellow", border_style="yellow", padding=(1, 4)))
    elif choice == "2":
        art = """
    [===]
   | 0 0 |
   |  ^  |
   | '-' |
   |_____|
   로봇
        """
        console.print(Panel.fit(art, title="로봇", style="bold cyan", border_style="cyan", padding=(1, 4)))
    elif choice == "3":
        art = """
    /\\_/\\
   ( o.o )
    > ^ <
    고양이
        """
        console.print(Panel.fit(art, title="고양이", style="bold magenta", border_style="magenta", padding=(1, 4)))
    else:
        console.print(Panel("잘못된 입력입니다. 1, 2, 3 또는 0을 입력하세요.", style="bold red"))

def print_table_menu(options, title="메뉴"):
    table = Table(title=title, title_style="bold green", box=box.HEAVY_EDGE, border_style="bright_green")
    table.add_column("번호", justify="center", style="bold white", no_wrap=True)
    table.add_column("설명", style="bold cyan")

    for key, value in options.items():
        table.add_row(key, value)

    console.print(table)

def select_character_loop(max_count=None):
    count = 0
    while True:
        if max_count is not None and count >= max_count:
            console.print(Panel.fit(f"{max_count}번의 선택이 끝났습니다. 프로그램을 종료합니다.", style="bold yellow"))
            break

        console.rule("[bold blue]캐릭터 선택[/bold blue]")
        if max_count is not None:
            console.print(f"[bold]{count + 1}/{max_count}번째 선택[/bold]\n")

        options = {
            "1": "사람",
            "2": "로봇",
            "3": "고양이",
            "0": "종료"
        }
        print_table_menu(options, title="캐릭터 선택 메뉴")
        choice = Prompt.ask("[bold green]원하는 캐릭터 번호를 입력하세요[/bold green]")

        if choice == "0":
            console.print(Panel.fit("프로그램을 종료합니다.", style="bold yellow"))
            break
        else:
            show_ascii_art(choice)
            if max_count is not None:
                count += 1

def main():
    show_welcome_banner()

    options = {
        "1": "5번 선택 모드",
        "2": "무한 선택 모드 (0 입력 시 종료)"
    }
    print_table_menu(options, title="모드 선택")
    mode = Prompt.ask("[bold green]모드를 선택하세요[/bold green]")

    if mode == "1":
        select_character_loop(max_count=5)
    elif mode == "2":
        select_character_loop()
    else:
        console.print(Panel.fit("잘못된 입력입니다. 프로그램을 종료합니다.", style="bold red"))

if __name__ == "__main__":
    main()
