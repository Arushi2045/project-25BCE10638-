Guess The Number!

Overview:
"Guess The Number!" is a simple, classic desktop game implemented in Python using the tkinter library.
The application provides a friendly, graphical user interface (GUI) where the player attempts to guess a randomly selected target number within a defined range and a limited number of attempts.
The project demonstrates basic GUI development, event handling, user input validation, and game logic implementation in Python.

Features:
Customizable Player Name: Players must enter their name to start the game.
Random Target Generation: The game randomly selects a secret number between 1 and 20 for the player to guess.
Limited Attempts: Players have a maximum of 10 attempts to guess the correct number.
Guess Feedback: The game provides immediate feedback after each guess, indicating whether the guess was "too large" or "too small."
Win/Loss Condition: The game ends upon a correct guess (Win) or when the maximum attempts are reached (Loss).
Play Again: A "Play Again" button appears after the game concludes, allowing for immediate reset and replay.
Input Validation: Ensures the user enters a valid number within the 1-20 range.
Themed Interface: Features a clean, rustic color palette using the Georgia font for improved aesthetics.

Technologies/Tools Used:
Python 3: The primary programming language used.
Tkinter: Python's standard GUI (Graphical User Interface) library, used for building the desktop application interface.
Random Module: Used to generate the secret target number.

Installation & Execution:
Install Python 3 on your system.
Save the Code: Ensure the Python code is saved in a file named 'project.py'
Run from Terminal/Command Prompt: Navigate to the directory where project.py is saved and execute the command: python project.py
Start Playing: The GUI window will open. Enter your name and click the 'Start Game' button to begin.

Instructions for Testing:

Initial State =>
Verify the title is 'Guess The Number!'
Verify the Guess button and the guess input field are disabled.
Verify the 'Start Game' button is enabled.

Starting a Game =>
Enter a name (e.g., 'Tester 1')
Click 'Start Game'
Verify the 'Guess' button and the guess input field are now enabled, and the 'Start Game' button is disabled.
Attempt counter should show Attempts: 0 / 10
<img width="329" height="356" alt="image" src="https://github.com/user-attachments/assets/380f0057-1c53-4670-ad27-2ba4c15d325c" />

Input Validation Test =>
Enter text (e.g., 'hello') and click Guess.
Expected Result: Feedback should show "Invalid input. Please enter a number (1-20)." Attempts counter should not increase.
Enter an out-of-range number (e.g., '50') and click Guess.
Expected Result: Feedback should show "Number must be between 1 and 20." Attempts counter should not increase.
<img width="327" height="356" alt="image" src="https://github.com/user-attachments/assets/1d158521-a623-4f88-93f2-d2a9263bb234" />

Guessing Logic Test =>
Make a guess (e.g., '10')
If the feedback is "too large," try a smaller number.
If the feedback is "too small," try a larger number.
Check that the Attempts counter increments by 1 after every valid guess.
<img width="327" height="358" alt="image" src="https://github.com/user-attachments/assets/929a78f0-b01a-46dc-a854-92f864454872" />

Win Condition Test =>
Continue guessing until you find the correct number.
Expected Result: Feedback should show the 'CORRECT GUESS' win message. The 'Guess' button is disabled. A 'Play Again' button appears.
<img width="329" height="354" alt="image" src="https://github.com/user-attachments/assets/31e1df3a-db75-4592-bac1-a723e08efdd8" />

Loss Condition Test =>
Start a new game.
Deliberately make 10 incorrect guesses.
Expected Result: After the 10th guess, feedback should show the 'YOU LOSE' message, revealing the target number. The 'Guess' button is disabled. A 'Play Again' button appears.
<img width="332" height="358" alt="image" src="https://github.com/user-attachments/assets/5bc0d339-0d9c-4792-bc54-38b874367ace" />

Play Again Test =>.
Click the 'Play Again' button
Expected Result: The interface should revert to the initial state (Step 1), ready for a new player or game.
<img width="329" height="359" alt="image" src="https://github.com/user-attachments/assets/9f149835-5b89-466d-bb91-84c53ecb629e" />
