def main():
    months_list = [
"January", "February", "March", "April", "May", "June",
"July", "August", "September", "October", "November", "December"
    ]
    while True:
        date = input("Date: ").strip()
        try:
            month, day, year = date.split("/")
            month = int(month.replace(" ", ""))
            day = int(day)
            year = int(year.replace(" ", ""))
            if (int(month) > 0 and int(month) < 13) and (int(day) > 0 and int(day) < 32):
                if year >= 1000 and year <= 9999:
                    print(year, f"{month:02}", f"{day:02}", sep="-")
                    break
        except:
            try:
                if "," not in date:
                    raise SyntaxError
                else:
                    month, day, year = date.split(" ")
                    day = day.replace(",", "")
                    day = int(day)
                    year = int(year)
                if month in months_list and (int(day) > 0 and int(day) < 32):
                    if year >= 1000 and year <= 9999:
                        month = (months_list.index(month)+1)
                    print(year, f"{month:02}", f"{day:02}", sep="-")
                    break
            except:
                pass
main()