def main():
    
    while True:
        try:
            books = int(input("Number of books purchased this month: "))
            if books < 0:
                print("Number of books cannot be negative. Please enter a valid number.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    if books == 0:
        points = 0
    elif books >= 2 and books < 4:
        points = 5
    elif books >= 4 and books < 6:
        points = 15
    elif books >= 6 and books < 8:
        points = 30
    elif books > 8:
        points = 60
    else:
        points = 0

    print("\n--------------------------")
    print(f"Points awarded: {points}")
    print("--------------------------\n")

if __name__ == "__main__":
    main()
