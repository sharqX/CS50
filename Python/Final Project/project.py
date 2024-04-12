import time
import datetime
from tabulate import tabulate
from pyfiglet import Figlet
import sys


class Pomodoro:

    def timer(self):
        with open("settings.txt") as file:
            data = file.readlines()
            h = int(data[1])
            m = int(data[2])
            s = int(data[3])
            h1 = int(data[5])
            m1 = int(data[6])
            s1 = int(data[7])

        print("Your timer starts now")
        total_seconds = h * 3600 + m * 60 + s
        while total_seconds > 0:
            work = datetime.timedelta(seconds=total_seconds)
            print(work, end="\r")
            time.sleep(1)
            total_seconds -= 1

        print("Time to take a break!")
        time.sleep(1)
        rest_time = h1 * 3600 + m1 * 60 + s1
        while rest_time > 0:
            rest = datetime.timedelta(seconds=rest_time)
            print(rest, end="\r")
            time.sleep(1)
            rest_time -= 1

        Pomodoro.conti(self)

    def settings(self):
        print("Please enter the time you want to work/study")

        h = input("Enter the time in hours: ")
        m = input("Enter the time in minutes: ")
        s = input("Enter the time in seconds: ")
        with open("settings.txt") as file:
            data = file.readlines()
            data[1] = h + "\n"
            data[2] = m + "\n"
            data[3] = s + "\n"
        with open("settings.txt", "w") as file:
            for line in data:
                file.write(line)

        print("Please enter the duration of the break")

        h1 = input("Enter the time in hours: ")
        m1 = input("Enter the time in minutes: ")
        s1 = input("Enter the time in seconds: ")
        with open("settings.txt") as file:
            data = file.readlines()
            data[5] = h1 + "\n"
            data[6] = m1 + "\n"
            data[7] = s1 + "\n"
        with open("settings.txt", "w") as file:
            for line in data:
                file.write(line)

        Pomodoro.menu(self)

    def menu(self):
        table = [["1", "Start Timer"], ["2", "Change Timmer Settings"]]
        print(tabulate(table, tablefmt="pipe"))
        print("\n")
        while True:
            try:
                pressed = int(input("Select your option: "))
                if pressed == 1:
                    print("Starting your timer")
                    Pomodoro.timer(self)
                elif pressed == 2:
                    Pomodoro.settings(self)
                else:
                    print("Not a correct option")
            except ValueError:
                print("Not a correct option")

    def conti(self):
        table = [["1", "Continue?"], ["2", "Change Timmer Settings"], ["3", "Exit"]]
        print(tabulate(table, tablefmt="pipe"))
        print("\n")
        while True:
            try:
                pressed = int(input("Select your option: "))
                if pressed == 1:
                    Pomodoro.timer(self)
                elif pressed == 2:
                    Pomodoro.settings(self)
                elif pressed == 3:
                    sys.exit("See you again!")
                else:
                    print("Not a correct option")
            except ValueError:
                print("Not a correct option")


def title():
    f = Figlet()
    f.setFont(font="ogre")
    Title = "Your Pomodoro"
    print(f.renderText(Title))


def main():
    title()
    p = Pomodoro()
    p.menu()


if __name__ == "__main__":
    main()
