import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if time :=  re.search(r"(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM) to (0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)", s, re.IGNORECASE):
        start = in_time(time.group(1),time.group(2), time.group(3))
        end = in_time(time.group(4),time.group(5), time.group(6))
        return f"{start} to {end}"
    else:
         raise ValueError

def in_time(hr, min, ap):
    if hr == "12":
        if ap == "AM":
            hour = "00"
        else:
            hour = "12"
    else:
        if ap == "AM":
            hour = f"{int(hr):02}"
        else:
            hour = f"{int(hr)+12}"
    if min == None:
        minute = "00"
    else:
        minute = f"{int(min):02}"

    return f"{hour}:{minute}"

if __name__ == "__main__":
    main()
