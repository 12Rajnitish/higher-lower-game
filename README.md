
# Higher-Lower Game

This is a Python-based Higher-Lower game where you compare the follower counts of various celebrities and brands. 
Your goal is to correctly guess which one has more followers. 
The game continues until you make a wrong guess, and your score is displayed at the end.

## Project Structure

The project includes three main Python files:

1. **`higher_lower.py`**: The main game logic is implemented in this file. It handles the game flow, user input, and score tracking.
2. **`art.py`**: Contains ASCII art used in the game, including the logo and "vs" separator.
3. **`game_data.py`**: Contains the data about celebrities and brands, including their names, follower counts, descriptions, and countries.

## Setup

To run the game, follow these steps:

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/12Rajnitish/higher-lower-game.git
   ```
   
2. Navigate to the project directory:
   ```bash
   cd higher-lower-game
   ```

3. Ensure you have Python installed (preferably Python 3.x).

4. Run the `higher_lower.py` file to start the game:
   ```bash
   python higher_lower.py
   ```

## Gameplay

- The game will display two options: A and B.
- Your task is to guess which option has more followers.
- You can type `a` or `b` to make your guess.
- The game will continue until you make a wrong guess, at which point your final score will be displayed.

## Credits

- The data used in the game is stored in `game_data.py` and consists of celebrity names, follower counts, descriptions, and countries.
- The data used in this game is sourced from Wikipedia and is up-to-date as of November 28, 2024.
- The ASCII art used in the game is stored in `art.py`.

