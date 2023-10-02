def main():
    hour = input('please enter the time: ')
    time = convert(hour)
    if time  >= 7 and time  <= 8:
        print('breakfast time')
    elif time  >= 12 and time  <= 13:
        print('lunch time')
    elif time  >= 18 and time  <= 19:
        print('dinner time')

def convert(time):
    hours, minutes = time.split(":")
    decimal_minutes = int(minutes) / 60
    time = int(hours) + decimal_minutes 
    return time 


if __name__ == "__main__":
    main()
