#Christian Davies
#CBIS 4210
#Assignment 01-01 - Customer Satisfaction survey

def conduct_survey():
    # Greet the user
    print("Welcome to our survey!")

    # Ask about the user's experience
    experience = input("How was your experience (good, fair, poor)? ").strip().lower()

    # Ask if the user would return
    would_return = input("Would you return (yes/no)? ").strip().lower()

    # Display the responses
    print("\nThank you for your feedback!")
    print(f"Your experience was: {experience}")

    # Custom messages based on experience
    if experience == "poor":
        print("We're sorry to hear that. Please reach out to our team for assistance.")
    elif experience == "fair":
        print("Thank you for your feedback. We will work to improve our services")
    elif experience == "good":
        print("Thank you! Have a wonderful day!")
    else:
        print(f"Would you return: {'Yes' if would_return == 'yes' else 'No'}")

# Main function to run the survey
def main():
    conduct_survey()

if __name__ == "__main__":
    main()