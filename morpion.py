#!/usr/bin/env python3

from termcolor import colored
from os import system, name
from random import randint
from sys import exit, argv


class Morpion:

    def __init__(self) -> None:

        self.morpion: list = [ [ "   " for _ in range(3)] for i in range(3) ]
        self.lti: dict = {
            "A": 0,
            "B": 1,
            "C": 2,
            0: "A",
            1: "B",
            2: "C",
        }


    def afficher(self) -> None:

        print("     1    2    3\n   +--------------+")

        for i, line in enumerate(self.morpion):
            print(f" {self.lti[i]} ", end="")

            for case in line:
                print(f'|', case, end='')

            print("| \n   +--------------+")


    def ask(self) -> tuple:

        a: list = [ 'z', 8 ]

        while (a[0].upper() not in ["A", "B", "C" ]) or (str(a[1]) not in [ "1" , "2" , "3" ]):
            to_i: str = colored("\n>>> ", "cyan")
            a: list = input(to_i).split(",")

        return self.lti[a[0].upper()], int(a[1]) - 1


    def ajouter(self, case: tuple, symbole: str) -> None:

        if self.morpion[case[0]][case[1]].strip() == "":
            self.morpion[case[0]][case[1]] = symbole
        else:
            raise Exception("Case is not empty")


    def longueur(self, tab: list) -> str:

        for line in tab:
            if line[0] == line[1] == line[2]:
                return line[0].strip()
            else:
                return ""


    def oblique(self) -> str:

        oalasuite: int = 0
        xalasuite: int = 0

        for i in range(len(self.morpion)):
            if "O" in self.morpion[i][i]:
                oalasuite += 1

            elif "X" in self.morpion[i][i]:
                xalasuite += 1


        if oalasuite == 3:
            return "O"

        elif xalasuite == 3:
            return "X"


        oalasuite: int = 0
        xalasuite: int = 0

        for i in range(len(self.morpion)):
            if "O" in self.morpion[i][len(self.morpion)-1-i]:
                oalasuite += 1

            elif "X" in self.morpion[i][len(self.morpion)-1-i]:
                xalasuite += 1


        if oalasuite == 3:
            return "O"

        elif xalasuite == 3:
            return "X"


    def test(self) -> None:

        m: Morpion = self.morpion

        # ----


        lg = self.longueur(m)
        if lg in ["O", "X"]:
            print(lg + " winned")
            exit()


        lr = self.longueur( zip(m[0], m[1], m[2]) )
        if lr in ["O", "X"]:
            print(lg + " winned")
            exit()


        ob = self.oblique()
        if ob in ["O", "X"]:
            print(ob + " winned")
            exit()


def clear() -> None:

    system("cls" if name == "nt" else "clear")


def pvb() -> bool:

    m: Morpion = Morpion()
    a: int = 0

    for i in range(9):
        print(colored(" PVB", "cyan", attrs=["bold"]))
        m.afficher()
        m.test()

        if a % 2 == 0:
            while True:
                try:
                    toadd = m.ask()
                    m.ajouter(toadd, " O ")
                    clear()
                    break
                except:
                    continue

        else:
            symb = " X "

            while True:
                try:
                    toadd: tuple = randint(0, 2), randint(0,2)
                    m.ajouter(toadd, " X ")
                    clear()
                    break
                except:
                    continue
        a: int = a + 1
    return True


def pvp() -> bool:

    m: Morpion = Morpion()
    a: int = 0

    for i in range(9):
        print(colored(" PVP", "cyan", attrs=['bold']))
        m.afficher()
        m.test()

        if a % 2 == 0:
            symb = " O "
        else:
            symb = " X "

        while True:
            try:
                toadd = m.ask()
                m.ajouter(toadd, symb)
                break
            except:
                continue
        clear()

        a: int = a + 1
    return True


def main() -> None:

    if len(argv) == 1:
        print("[" + colored("+", 'blue') + "] Usage: python3 morpion.py ( pvp | pvb )")

    elif argv[1].upper() == "PVP":
        pvp()

    elif argv[1].upper() == "PVB":
        pvb()


if __name__ == "__main__":
    main()
