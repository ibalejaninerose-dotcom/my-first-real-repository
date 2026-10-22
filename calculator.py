# Simple Grade Calculator
# Name: [Isulat imong Pangalan]
# Section: IT3R10

def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():
    print("Welcome to the Grade Calculator!")
    try:
        score = float(input("Enter your score (0-100): "))
        if 0 <= score <= 100:
            grade = calculate_grade(score)
            print(f"Your grade is: {grade}")
        else:
            print("Please enter a valid score between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()  
