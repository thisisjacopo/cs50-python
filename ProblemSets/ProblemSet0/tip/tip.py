def main():
    dollars = dollars_to_float(input("How much was the meal? ").strip("$"))
    percent = percent_to_float(input("What percentage would you like to tip? ").strip("%"))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars: str):
    return float(dollars)
    


def percent_to_float(percent: str):
    float_percent = float(percent)
    return float_percent / 100


main()