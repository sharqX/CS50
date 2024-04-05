def convert(time):
    hours, minutes = map(int, time.split(":"))
    decimal_time = hours + (minutes / 60)
    return decimal_time
    
def main():
    what_time = input("What time is it? ")
    decimal_user_time = convert(what_time)

    breakfast_start = convert("7:00")
    breakfast_end = convert("8:00")
    lunch_start = convert("12:00")
    lunch_end = convert("13:00")
    dinner_start = convert("18:00")
    dinner_end = convert("19:00")

    if breakfast_start <= decimal_user_time <= breakfast_end:
        print("breakfast time")
    elif lunch_start <= decimal_user_time <= lunch_end:
        print("lunch time")
    elif dinner_start <= decimal_user_time <= dinner_end:
        print("dinner time")


if __name__ == "__main__":
    main()
