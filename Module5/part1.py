def main():
    
    # Get number of years
    while True:
        try:
            years = int(input("Enter the number of years: "))
            if years < 1:
                print("Number of years must be at least 1.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    total_rainfall = 0.0
    total_months = years * 12

    # Collect rainfall data
    for year in range(1, years + 1):
        print(f"\nYear {year}:")
        for month in range(1, 13):
            while True:
                try:
                    rainfall = float(input(f"  Enter rainfall for month {month} (in inches): "))
                    if rainfall < 0:
                        print("  Rainfall cannot be negative. Please enter a valid amount.")
                        continue
                    total_rainfall += rainfall
                    break
                except ValueError:
                    print("  Please enter a valid number.")

    average_rainfall = total_rainfall / total_months

    print("\n----------------------------------------------")
    print(f"Number of months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")
    print("----------------------------------------------\n")

if __name__ == "__main__":
    main() 