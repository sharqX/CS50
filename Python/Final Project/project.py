import re
import sys
import time
import datetime
from pyfiglet import Figlet
from tabulate import tabulate
from playsound import playsound


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

        print("Your timer starts now...")
        work_time = h * 3600 + m * 60 + s
        while work_time > 0:
            work = datetime.timedelta(seconds=work_time)
            print(work, end="\r")
            time.sleep(1)
            work_time -= 1
        playsound("work.wav")

        print("Time to take a break!")
        time.sleep(1)
        rest_time = h1 * 3600 + m1 * 60 + s1
        while rest_time > 0:
            rest = datetime.timedelta(seconds=rest_time)
            print(rest, end="\r")
            time.sleep(1)
            rest_time -= 1
        playsound("break.wav")

        Pomodoro.conti(self)

    def settings(self):
        print("Please enter the time you want to work/study")
        time_prompts = [
            ("Enter the time in hours: "),
            ("Enter the time in minutes: "),
            ("Enter the time in seconds: "),
        ]
        error_prompt = "Input must be a number. Please try again."
        while True:
            try:
                h = input(time_prompts[0])
                if not h or not re.search(r"[0-9]", h):
                    raise ValueError
                break
            except ValueError:
                print(error_prompt)
        while True:
            try:
                m = input(time_prompts[1])
                if not m or not re.search(r"[0-9]", m):
                    raise ValueError
                break
            except ValueError:
                print(error_prompt)
        while True:
            try:
                s = input(time_prompts[2])
                if not s or not re.search(r"[0-9]", s):
                    raise ValueError
                break
            except ValueError:
                print(error_prompt)

        print("Please enter the duration of the break")
        while True:
            try:
                h1 = input(time_prompts[0])
                if not h1 or not re.search(r"[0-9]", h1):
                    raise ValueError
                break
            except ValueError:
                print(error_prompt)
        while True:
            try:
                m1 = input(time_prompts[1])
                if not m1 or not re.search(r"[0-9]", m1):
                    raise ValueError
                break
            except ValueError:
                print(error_prompt)
        while True:
            try:
                s1 = input(time_prompts[2])
                if not s1 or not re.search(r"[0-9]", s1):
                    raise ValueError
                break
            except ValueError:
                print(error_prompt)
        with open("settings.txt") as file:
            data = file.readlines()
            data[1] = h + "\n"
            data[2] = m + "\n"
            data[3] = s + "\n"
            data[5] = h1 + "\n"
            data[6] = m1 + "\n"
            data[7] = s1 + "\n"
        with open("settings.txt", "w") as file:
            for line in data:
                file.write(line)
        Pomodoro.menu(self)
        return h, m, s, h1, m1, s1

    def test_settings(self, h, m, s, h1, m1, s1):
        h = Pomodoro.settings
        m = Pomodoro.settings
        s = Pomodoro.settings
        h1 = Pomodoro.settings
        m1 = Pomodoro.settings
        s1 = Pomodoro.settings
        timer_inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if not h or h not in timer_inputs:
            raise ValueError
        if not m or m not in timer_inputs:
            raise ValueError
        if not s or s not in timer_inputs:
            raise ValueError
        if not h1 or h1 not in timer_inputs:
            raise ValueError
        if not m1 or m1 not in timer_inputs:
            raise ValueError
        if not s1 or s1 not in timer_inputs:
            raise ValueError

    def menu(self):
        table = [["1", "Start Timer"], ["2", "Change Timmer Settings"], ["3", "Exit"]]
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
                elif pressed == 3:
                    sys.exit("See you again!")
                else:
                    print("Not a correct option")
            except ValueError:
                print("Not a correct option")
            return pressed

    def test_menu(self, p):
        p = Pomodoro.menu
        if p == 1:
            print("Starting your timer")
            Pomodoro.timer(self)
        elif p == 2:
            Pomodoro.settings(self)
        elif p == 3:
            sys.exit("See you again!")
        else:
            raise (ValueError)

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

    def test_conti(self, p):
        p = Pomodoro.conti
        if p == 1:
            Pomodoro.timer(self)
        elif p == 2:
            Pomodoro.settings(self)
        elif p == 3:
            sys.exit("See you again!")
        else:
            raise ValueError


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
