def check_pass_fail(score):
    passing_threshold = 60

    has_passed = score >= passing_threshold

    if has_passed:
        print(f"Score: {score}. Result: Passed!")
    else:
        print(f"Score: {score}. Result: Failed.")


print("--- Score Checker Program ---")

while True:
    try:
        user_input = input("Enter a student's score (or type 'quit' to exit): ")

        if user_input.lower() == 'quit':
            print("Exiting program. Goodbye!")
            break

        score = int(user_input)

        if 0 <= score <= 100:
            check_pass_fail(score)
        else:
            print("Error: Score must be between 0 and 100. Please try again.")

    except ValueError:
        print("Error: Invalid input. Please enter a valid number or 'quit'.")

print("--- Program ended ---")
