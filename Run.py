try:
    import random, os, csv, sys, requests, string, time
    from rich import print as Println
    from rich.console import Console
    from rich.panel import Panel
    from rich.columns import Columns
except ModuleNotFoundError:
    print("This program requires 'rich' library to be installed. Use 'pip install rich' to install it.")
    __import__('sys').exit()

PROVIDER = {
    "Telkomsel": ["0811", "0812", "0813", "0821", "0822", "0823", "0851", "0852", "0853"],
    "Indosat": ["0814", "0815", "0816", "0855", "0856", "0857", "0858"],
    "XL Axiata": ["0817", "0818", "0819", "0859", "0877", "0878"],
    "Axis": ["0831", "0832", "0833", "0838"],
    "Smartfren": ["0881", "0882", "0883", "0884", "0885", "0886", "0887", "0888", "0889"],
    "Three (3)": ["0895", "0896", "0897", "0898", "0899"]
}
NUMBERS = set()

def BANNER() -> None:
    os.system("cls" if os.name == "nt" else "clear")
    Println(
        Panel(r"""[bold red]𒊹 [bold yellow]𒊹 [bold green]𒊹
[bold blue]   ___________    _        _   _                 _     
  |_   _|  ___|  | |      | \ | |               | |    
    | | | |_ __ _| | _____|  \| |_   _ _ __ ___ | |__  
    | | |  _/ _` | |/ / _ \ . ` | | | | '_ ` _ \| '_ \ 
   _| |_| || (_| |   <  __/ |\  | |_| | | | | | | |_) |
[bold blue]   \___/\_| \__,_|_|\_\___\_| \_/\__,_|_| |_| |_|_.__/ 
        [underline red]Fake Number Indonesian - Coded by Rozhak""", style="bold bright_black", width=60)
    )

class FEATURES:

    def __init__(self) -> None:
        try:
            BANNER()
            with requests.Session() as session:
                response = session.get("https://ipinfo.io/json", allow_redirects=False, verify=True)
                data = response.json()
                self.ip, self.city = (data["ip"], data["city"])
        except Exception:
            self.ip, self.city = (None, None)

        Println(
            Columns(
                [
                    Panel(f"[bold white]IP Address: [bold green]{str(self.ip)[:11]}xxx", style="bold bright_black", width=30),
                    Panel(f"[bold white]City: [bold green]{self.city}", style="bold bright_black", width=29)
                ]
            )
        )

        Println(
            Panel("""[bold white][[bold green]1[bold white]] Create Number From Telkomsel
[bold white][[bold green]2[bold white]] Create Number From Axis
[bold white][[bold green]3[bold white]] Create Number From Smartfren
[bold white][[bold green]4[bold white]] Create Number From Three (3)
[bold white][[bold green]5[bold white]] Create Number From XL Axiata
[bold white][[bold green]6[bold white]] Create Number From Indosat
[bold white][[bold red]7[bold white]] Exit ([bold red]Close Program[bold white])""", style="bold bright_black", width=60, title="[bold bright_black]>> [Key Features] <<", title_align="center", subtitle="[bold bright_black]╭─────────", subtitle_align="left")
        )
        self.choice = Console().input("[bold bright_black]   ╰─> ")
        if self.choice in ["1", "01"]:
            try:
                Println(
                    Panel(f"[bold white]Silakan Masukan Jumlah Nomor Telepon Yang Ingin Anda Cip\ntakan, Pastikan Anda Hanya Memasukkan Angka Saja!", style="bold bright_black", width=60, title="[bold bright_black]>> [Jumlah Nomor] <<", title_align="center", subtitle="[bold bright_black]╭─────────", subtitle_align="left")
                )
                self.count = int(Console().input("[bold bright_black]   ╰─> "))
                self.provider = "Telkomsel"
                MAKE().NUMBERS(self.provider, count=self.count)

                self.filename = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                self.SAVE(NUMBERS, self.provider, f"Temporary/{self.filename}.csv")
                sys.exit()
            except Exception as error:
                Println(
                    Panel(f"[bold red]{str(error).title()}!", style="bold bright_black", width=60, title="[bold bright_black]>> [Error] <<")
                )
        elif self.choice in ["2", "02"]:
            try:
                Println(
                    Panel(f"[bold white]Silakan Masukan Jumlah Nomor Telepon Yang Ingin Anda Cip\ntakan, Pastikan Anda Hanya Memasukkan Angka Saja!", style="bold bright_black", width=60, title="[bold bright_black]>> [Jumlah Nomor] <<", title_align="center", subtitle="[bold bright_black]╭─────────", subtitle_align="left")
                )
                self.count = int(Console().input("[bold bright_black]   ╰─> "))
                self.provider = "Axis"
                MAKE().NUMBERS(self.provider, count=self.count)

                self.filename = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                self.SAVE(NUMBERS, self.provider, f"Temporary/{self.filename}.csv")
                sys.exit()
            except Exception as error:
                Println(
                    Panel(f"[bold red]{str(error).title()}!", style="bold bright_black", width=60, title="[bold bright_black]>> [Error] <<")
                )
        elif self.choice in ["3", "03"]:
            try:
                Println(
                    Panel(f"[bold white]Silakan Masukan Jumlah Nomor Telepon Yang Ingin Anda Cip\ntakan, Pastikan Anda Hanya Memasukkan Angka Saja!", style="bold bright_black", width=60, title="[bold bright_black]>> [Jumlah Nomor] <<", title_align="center", subtitle="[bold bright_black]╭─────────", subtitle_align="left")
                )
                self.count = int(Console().input("[bold bright_black]   ╰─> "))
                self.provider = "Smartfren"
                MAKE().NUMBERS(self.provider, count=self.count)

                self.filename = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                self.SAVE(NUMBERS, self.provider, f"Temporary/{self.filename}.csv")
                sys.exit()
            except Exception as error:
                Println(
                    Panel(f"[bold red]{str(error).title()}!", style="bold bright_black", width=60, title="[bold bright_black]>> [Error] <<")
                )
        elif self.choice in ["4", "04"]:
            try:
                Println(
                    Panel(f"[bold white]Silakan Masukan Jumlah Nomor Telepon Yang Ingin Anda Cip\ntakan, Pastikan Anda Hanya Memasukkan Angka Saja!", style="bold bright_black", width=60, title="[bold bright_black]>> [Jumlah Nomor] <<", title_align="center", subtitle="[bold bright_black]╭─────────", subtitle_align="left")
                )
                self.count = int(Console().input("[bold bright_black]   ╰─> "))
                self.provider = "Three (3)"
                MAKE().NUMBERS(self.provider, count=self.count)

                self.filename = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                self.SAVE(NUMBERS, self.provider, f"Temporary/{self.filename}.csv")
                sys.exit()
            except Exception as error:
                Println(
                    Panel(f"[bold red]{str(error).title()}!", style="bold bright_black", width=60, title="[bold bright_black]>> [Error] <<")
                )
        elif self.choice in ["5", "05"]:
            try:
                Println(
                    Panel(f"[bold white]Silakan Masukan Jumlah Nomor Telepon Yang Ingin Anda Cip\ntakan, Pastikan Anda Hanya Memasukkan Angka Saja!", style="bold bright_black", width=60, title="[bold bright_black]>> [Jumlah Nomor] <<", title_align="center", subtitle="[bold bright_black]╭─────────", subtitle_align="left")
                )
                self.count = int(Console().input("[bold bright_black]   ╰─> "))
                self.provider = "XL Axiata"
                MAKE().NUMBERS(self.provider, count=self.count)

                self.filename = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                self.SAVE(NUMBERS, self.provider, f"Temporary/{self.filename}.csv")
                sys.exit()
            except Exception as error:
                Println(
                    Panel(f"[bold red]{str(error).title()}!", style="bold bright_black", width=60, title="[bold bright_black]>> [Error] <<")
                )
        elif self.choice in ["6", "06"]:
            try:
                Println(
                    Panel(f"[bold white]Silakan Masukan Jumlah Nomor Telepon Yang Ingin Anda Cip\ntakan, Pastikan Anda Hanya Memasukkan Angka Saja!", style="bold bright_black", width=60, title="[bold bright_black]>> [Jumlah Nomor] <<", title_align="center", subtitle="[bold bright_black]╭─────────", subtitle_align="left")
                )
                self.count = int(Console().input("[bold bright_black]   ╰─> "))
                self.provider = "Indosat"
                MAKE().NUMBERS(self.provider, count=self.count)

                self.filename = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                self.SAVE(NUMBERS, self.provider, f"Temporary/{self.filename}.csv")
                sys.exit()
            except Exception as error:
                Println(
                    Panel(f"[bold red]{str(error).title()}!", style="bold bright_black", width=60, title="[bold bright_black]>> [Error] <<")
                )
        elif self.choice in ["7", "07"]:
            Println(
                Panel(f"[bold white]Anda Telah Memilih Opsi Keluar, Terima Kasih Telah Mengg\nunakan Program Ini!", style="bold bright_black", width=60, title="[bold bright_black]>> [Keluar] <<")
            )
            sys.exit()
        else:
            Println(
                Panel(f"[bold red]Pilihan Yang Anda Masukkan Tidak Tersedia Dalam Program Ini, Silakan Coba Lagi!", style="bold bright_black", width=60, title="[bold bright_black]>> [Pilihan Salah] <<")
            )
            time.sleep(5.0)
            FEATURES()

    def SAVE(self, numbers: list, provider: str, filename: str) -> None:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    "Provider", "Nomor Palsu", "Format Nomor"
                ]
            )
            for number in numbers:
                writer.writerow(
                    [
                        provider, number, MAKE().FORMAT(number)
                    ]
                )
        Println(
            Panel(f"[bold green]Selamat![bold white] Kami Telah Berhasil Menyimpan Semua Nomor Telep\non Ke Dalam File[bold red] {filename}[bold white]!", style="bold bright_black", width=60, title="[bold bright_black]>> [Sukses] <<")
        )

class MAKE:

    def __init__(self) -> None:
        pass

    def NUMBERS(self, provider: str, count: int) -> bool:
        for _ in range(count):
            code = random.choice(PROVIDER[provider])
            number = ''.join([str(random.randint(0, 9)) for _ in range(7)])
            NUMBERS.add(f"{code}{number}")
        if len(NUMBERS) >= 1:
            return True
        return False
    
    def FORMAT(self, number: str) -> str:
        return f"{number[:4]}-{number[4:7]}-{number[7:]}"

if __name__ == '__main__':
    try:
        os.system("git pull")
        if not os.path.exists("Temporary"):
            os.makedirs("Temporary")
        FEATURES()
    except Exception as error:
        Println(
            Panel(f"[bold red]{str(error).title()}!", style="bold bright_black", width=60, title="[bold bright_black]>> [Error] <<")
        )
        sys.exit()
    except KeyboardInterrupt:
        sys.exit()