import tkinter as tk
from tkinter import messagebox
import random

# defines a color palette 
bg_color = "#f7f0e8"         
fg_color = "#3c403d"         
button_color = "#a2b595"     
button_hover_color = "#8c9b83" 
entry_bg = "#ffffff"         
disabled_color = "#d5d8d0"   
highlight_color = "#e57373"  
win_color = "#5cb85c"        
font_family = "Georgia"  

target = 0
attempts = 0
max_attempts = 10
name = ""
def start_game():
    global target, attempts, max_attempts
    global name
    # get the player's name from the entry widget
    name = name_entry
    # check if a name was entered
    if not name:
        messagebox.showerror("Error", "Please enter your name to start.")
        return
    # generate the new random number (1 to 20)
    target = random.randint(1, 20)
    attempts = 0
    max_attempts = 10
    welcome_label.config(text=f"Hi, {name}! Guess a number from 1 to 20.", fg=fg_color)
    feedback_label.config(text=f"You have {max_attempts} attempts. Good luck!", fg=fg_color)
    attempts_label.config(text=f"Attempts: {attempts} / {max_attempts}", fg=fg_color)
    # enable the guessing components
    guess_button.config(state=tk.NORMAL, bg=button_color, activebackground=button_hover_color)
    guess_entry.config(state=tk.NORMAL, bg=entry_bg, fg=fg_color, insertbackground=fg_color)
    # disable the start button and name entry
    start_button.config(state=tk.DISABLED, bg=disabled_color) 
    name_entry.config(state=tk.DISABLED, bg=entry_bg)
    guess_entry.focus_set()

def check_guess():
    global attempts, target, max_attempts
    guess_str = guess_entry.strip()
    guess_entry.delete(0, tk.END) 
    #input validation
    if not guess_str.isdigit():
        feedback_label.config(text="Invalid input. Please enter a number (1-20).", fg=highlight_color)
        return
    guess = int(guess_str)
    if not 1 <= guess <= 20:
        feedback_label.config(text="Number must be between 1 and 20.", fg=highlight_color)
        return
    # increment attempt counter
    attempts += 1
    # Check guess
    if guess == target:
        feedback_label.config(text=f"🎉 CORRECT GUESS! YOU WON!! You made {attempts} attempts! 🎉", fg=win_color)
        end_game(win=True)
    elif guess > target:
        # guess is too high
        feedback_label.config(text="Your number was too large. Guess again.", fg=fg_color)
    else:
        # guess is too low
        feedback_label.config(text="Your number was too small. Guess again.", fg=fg_color)

    # check loss condition
    if attempts >= max_attempts:
        if guess != target: 
            feedback_label.config(text=f"❌ YOU LOSE! The number was {target}. ❌", fg=highlight_color)
            end_game(win=False)
    attempts_label.config(text=f"Attempts: {attempts} / {max_attempts}", fg=fg_color)
    guess_entry.focus_set() 

def end_game(win):
    guess_button.config(state=tk.DISABLED, bg=disabled_color, activebackground=disabled_color)
    guess_entry.config(state=tk.DISABLED, bg=entry_bg)
    start_button.config(text="Play Again", command=reset_game, state=tk.NORMAL, bg=button_color, activebackground=button_hover_color)

def reset_game():
    global target, attempts
    target = 0
    attempts = 0
    
    welcome_label.config(text="Welcome to the Number Guessing Game!", fg=fg_color)
    feedback_label.config(text="Enter your name and press Start Game.", fg=fg_color)
    attempts_label.config(text="Attempts: 0 / 10", fg=fg_color)
    guess_entry.delete(0, tk.END)
    
    start_button.config(text="Start Game", command=start_game, state=tk.NORMAL, bg=button_color, activebackground=button_hover_color)
    guess_button.config(state=tk.DISABLED, bg=disabled_color, activebackground=disabled_color)
    guess_entry.config(state=tk.DISABLED, bg=entry_bg)
    name_entry.config(state=tk.NORMAL, bg=entry_bg, fg=fg_color, insertbackground=fg_color)
    name_entry.delete(0, tk.END) 
    name_entry.focus_set()

import tkinter as tk
from tkinter import messagebox
import random

bg_color = "#f7f0e8"         
fg_color = "#3c403d"         
button_color = "#a2b595"     
button_hover_color = "#8c9b83" 
entry_bg = "#ffffff"        
disabled_color = "#d5d8d0"  
highlight_color = "#e57373" 
win_color = "#5cb85c"       
font_family = "Georgia"      

target = 0
attempts = 0
max_attempts = 10
player_name = ""

def start_game():
    global target, attempts, max_attempts
    
    global player_name
    player_name = name_entry.get().strip()
    
    if not player_name:
        messagebox.showerror("Error", "Please enter your name to start.")
        return

    target = random.randint(1, 20)
    attempts = 0
    max_attempts = 10
    
    welcome_label.config(text=f"Hi, {player_name}! Guess a number from 1 to 20.", fg=fg_color)
    feedback_label.config(text=f"You have {max_attempts} attempts. Good luck!", fg=fg_color)
    attempts_label.config(text=f"Attempts: {attempts} / {max_attempts}", fg=fg_color)
    
    guess_button.config(state=tk.NORMAL, bg=button_color, activebackground=button_hover_color)
    guess_entry.config(state=tk.NORMAL, bg=entry_bg, fg=fg_color, insertbackground=fg_color)
    start_button.config(state=tk.DISABLED, bg=disabled_color) 
    name_entry.config(state=tk.DISABLED, bg=entry_bg)
    guess_entry.focus_set()

def check_guess():
    global attempts, target, max_attempts
    
    guess_str = guess_entry.get().strip()
    guess_entry.delete(0, tk.END) 
    
    if not guess_str.isdigit():
        feedback_label.config(text="Invalid input. Please enter a number (1-20).", fg=highlight_color)
        return
        
    guess = int(guess_str)
    
    if not 1 <= guess <= 20:
        feedback_label.config(text="Number must be between 1 and 20.", fg=highlight_color)
        return

    attempts += 1
    
    if guess == target:
        feedback_label.config(text=f"🎉 CORRECT GUESS! YOU WON!! You made {attempts} attempts! 🎉", fg=win_color)
        end_game(win=True)
    elif guess > target:
        feedback_label.config(text="Your number was too large. Guess again.", fg=fg_color)
    else:
        feedback_label.config(text="Your number was too small. Guess again.", fg=fg_color)
    
    if attempts >= max_attempts:
        if guess != target: 
            feedback_label.config(text=f"❌ YOU LOSE! The number was {target}. ❌", fg=highlight_color)
            end_game(win=False)
        
    attempts_label.config(text=f"Attempts: {attempts} / {max_attempts}", fg=fg_color)
    guess_entry.focus_set() 

def end_game(win):
    guess_button.config(state=tk.DISABLED, bg=disabled_color, activebackground=disabled_color)
    guess_entry.config(state=tk.DISABLED, bg=entry_bg)
    start_button.config(text="Play Again", command=reset_game, state=tk.NORMAL, bg=button_color, activebackground=button_hover_color)

def reset_game():
    global target, attempts
    target = 0
    attempts = 0
    
    welcome_label.config(text="Welcome to the Number Guessing Game!", fg=fg_color)
    feedback_label.config(text="Enter your name and press Start Game.", fg=fg_color)
    attempts_label.config(text="Attempts: 0 / 10", fg=fg_color)
    guess_entry.delete(0, tk.END)
    
    start_button.config(text="Start Game", command=start_game, state=tk.NORMAL, bg=button_color, activebackground=button_hover_color)
    guess_button.config(state=tk.DISABLED, bg=disabled_color, activebackground=disabled_color)
    guess_entry.config(state=tk.DISABLED, bg=entry_bg)
    name_entry.config(state=tk.NORMAL, bg=entry_bg, fg=fg_color, insertbackground=fg_color)
    name_entry.delete(0, tk.END) 
    name_entry.focus_set()

root = tk.Tk()
root.title("Guess The Number!")
root.geometry("450x450") 
root.resizable(False, False) 
root.config(bg=bg_color) 
root.columnconfigure(0, weight=1) 

title_label = tk.Label(root, text="Guess The Number!", font=(font_family, 24, "bold"), 
                       bg=bg_color, fg=win_color)
title_label.grid(row=0, column=0, pady=(20, 10))

name_frame = tk.Frame(root, bg=bg_color)
name_frame.grid(row=1, column=0, pady=5) 
tk.Label(name_frame, text="Your Name:", font=(font_family, 12), bg=bg_color, fg=fg_color).pack(side=tk.LEFT, padx=5)
name_entry = tk.Entry(name_frame, width=25, font=(font_family, 12), 
                      bg=entry_bg, fg=fg_color, insertbackground=fg_color, 
                      bd=0, highlightthickness=1, highlightbackground=button_color) 
name_entry.pack(side=tk.LEFT)
name_entry.focus_set() 

start_button = tk.Button(root, text="Start Game", command=start_game, 
                         font=(font_family, 14, "bold"), bg=button_color, fg=fg_color,
                         activebackground=button_hover_color, activeforeground=fg_color,
                         bd=0, padx=20, pady=10, relief=tk.FLAT)
start_button.grid(row=2, column=0, pady=15) 

welcome_label = tk.Label(root, text="Welcome to the Number Guessing Game!", 
                         font=(font_family, 12), bg=bg_color, fg=fg_color, wraplength=400)
welcome_label.grid(row=3, column=0, pady=10) 

guess_frame = tk.Frame(root, bg=bg_color)
guess_frame.grid(row=4, column=0, pady=5) 
tk.Label(guess_frame, text="Your Guess (1-20):", font=(font_family, 12), bg=bg_color, fg=fg_color).pack(side=tk.LEFT, padx=5)
guess_entry = tk.Entry(guess_frame, width=15, font=(font_family, 12), 
                       bg=entry_bg, fg=fg_color, insertbackground=fg_color, 
                       bd=0, highlightthickness=1, highlightbackground=button_color, state=tk.DISABLED)
guess_entry.pack(side=tk.LEFT)

guess_button = tk.Button(root, text="Guess", command=check_guess, 
                         font=(font_family, 12, "bold"), bg=disabled_color, fg=fg_color, 
                         activebackground=button_hover_color, activeforeground=fg_color,
                         bd=0, padx=15, pady=8, relief=tk.FLAT, state=tk.DISABLED)
guess_button.grid(row=5, column=0, pady=10) 

feedback_label = tk.Label(root, text="Enter your name and press Start Game.", 
                          font=(font_family, 13, "italic"), bg=bg_color, fg=fg_color, wraplength=400)
feedback_label.grid(row=6, column=0, pady=10) 

attempts_label = tk.Label(root, text="Attempts: 0 / 10", 
                          font=(font_family, 12, "bold"), bg=bg_color, fg=fg_color)
attempts_label.grid(row=7, column=0, pady=5) 

def on_return_key(event):
    if guess_entry.cget('state') == tk.NORMAL:
        check_guess()

root.bind('<Return>', on_return_key) 

root.mainloop()
