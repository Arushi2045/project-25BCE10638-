Number Guessing Game

Project Statement:
Create a simple, engaging, and user-friendly number guessing game application using the Tkinter library in Python. 
The game must allow a player to guess a randomly selected number within a specific range (1 to 20) and provide immediate feedback on each guess. 
The game should limit the number of attempts and clearly indicate when the player wins or loses.

Scope of project:
The scope of this project is to develop a standalone desktop application with the following boundaries:
Core Game Logic: Implement the randomization of the target number (1-20), tracking of attempts, and the core logic for comparing the player's guess to the target number (too high, too low, or correct).
User Interface (Tkinter): Design a Graphical User Interface (GUI) using Tkinter to handle player input (name and guess) and display game information (welcome message, feedback, and attempts count).
Game Flow Management: Implement functions to start the game, check a guess, and end/reset the game, properly managing the state of GUI elements (e.g., enabling/disabling buttons and entry fields).
Input Validation: Include basic validation to ensure the player enters a valid number within the specified range (1-20).
Aesthetics: Apply simple theming (colors, fonts) to enhance the visual appeal and user experience.

Out of scope:
Saving game scores or high scores.
Advanced difficulty settings or adjustable number ranges.
Networking or multi-player functionality.

Target Users
Casual Users: Individuals looking for a simple, fun, and quick game to play on their desktop.
Beginner Programmers: Individuals who want to see a practical example of GUI development and basic game logic implemented in Python using Tkinter.

High-Level Features
Player Name Input: An initial screen/state allowing the user to enter their name before starting the game.
Random Target Generation: Automatically selects a random whole number between 1 and 20 at the start of each game.
Fixed Attempt Limit: The player is given a fixed limit of **10 attempts** to guess the number.
Guess Input & Submission: A dedicated entry field and button for the player to submit their guess.
Real-time Feedback: Provides immediate feedback after each guess, indicating if the guess was "too large," "too small," or "correct."
Attempt Counter: A clear display showing the current attempt number out of the maximum allowed attempts.
Win/Loss Notification: Clear and prominent messages to notify the player upon winning or losing the game, including revealing the target number upon a loss.
Play Again/Reset Functionality: A button to easily reset the game state and start a new round.
Enter Key Support: Allows the player to submit a guess by pressing the **Enter** key when the guess entry field is active.
