months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Date: ").strip()
    try:
        month, day, year = (date.split("/"))
        if 1 < int(month) < 12 and 1 < int(day) < 31:
            print(f"{year}-{int(month):02}-{int(day):02}")
            break
    except:
        try:
            old_month, old_day, year = (date.split(" "))
            if old_day.endswith(",") == True:
                day = old_day.strip(",")
                if old_month in months:
                    month = months.index(old_month)+1
                    if 1 < int(month) < 12 and 1 < int(day) < 31:
                        print(f"{year}-{int(month):02}-{int(day):02}")
                        break
        except:
            print()
            pass
