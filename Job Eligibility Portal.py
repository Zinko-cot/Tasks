print("Welcome to Job Eligibility Portal")

is_python_dev = input("Do you know Python? (Yes / No): ").strip().lower()

experience = float(input("How many years of experience or projects do you have?: "))

has_degree = input("Do you have a university degree or completed a training program? (Yes / No): ").strip().lower()

if is_python_dev == "yes" and (experience >= 2 or has_degree == "yes"):
    
    print("Congratulations! You've moved to the next interview stage.")
else:
    print("Sorry, your current qualifications do not meet the job requirements.")
