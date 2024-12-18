import art  # For displaying the logo
import game_data  # Contains the celebrity data
import random  # For selecting random celebrities

def higher_lower():
    current_score = 0  # Initialize score
    previous_celeb = {}  # Track previous celebrity

    while True:
        print(art.logo)  # Display logo

        # Select random celebrities, ensuring they are different
        celeb1 = previous_celeb if previous_celeb else random.choice(game_data.data)
        celeb2 = random.choice(game_data.data)
        while celeb1 == celeb2:
            celeb2 = random.choice(game_data.data)

        # Display celebrities for comparison
        print(f"Compare A: {celeb1['name']}, {celeb1['description']} from {celeb1['country']}")
        print(art.vs)
        print(f"Against B: {celeb2['name']}, {celeb2['description']} from {celeb2['country']}")

        # Determine correct answer
        answer = 'a' if celeb1["follower_count"] > celeb2["follower_count"] else 'b'

        # Get user input and validate
        user_choice = input("Who has more followers? Press A or B: ").lower()

        if user_choice in ['a', 'b']:
            if user_choice == answer:
                current_score += 1  # Correct answer
                print("\n" * 25)
                print(f"You're right! Current Score: {current_score}")
                previous_celeb = celeb2  # Update previous celeb
            else:
                print("\n" * 25)
                print(art.logo)
                print(f"Sorry, that's wrong. Final score: {current_score}")
                break  # End game on wrong answer
        else:
            print("\n" * 25)
            print("Invalid input. Please enter 'a' or 'b'.")

# Start the game
higher_lower()
