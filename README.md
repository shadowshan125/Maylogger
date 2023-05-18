# Maylogger

## JUST Another Key Logger

This code implements a simple key logger that captures and saves key presses to a file. The key logger listens for key press events and records the pressed keys in a text file named "collectedKeys.txt". It also provides a way to stop the key logger by pressing the Alt + Shift + Ctrl + Esc combination.

## Prerequisites

To run this code, you need to have the following libraries installed:

- `keyboard`: Used for listening to key press events.

You can install the required libraries by running the following command:

```
pip install keyboard
```

## How it works

The code consists of the following main parts:

1. Importing necessary libraries:
   - `keyboard`: Used for keyboard event handling.
   - `os`: Used for file operations.

2. Defining the callback function for key press events:
   - The `on_key_press` function is called whenever a key is pressed.
   - It checks if the combination Alt + Shift + Ctrl + Esc is pressed to stop the key logger.
   - It prints the pressed key and saves it to the file.

3. Defining the function to save content to a file:
   - The `save_content` function takes the content to be saved and the filename as input.
   - It opens the file in append mode (`'a'`) and writes the content to it.
   - It prints a message indicating the successful save operation.

4. Creating the file to store the pressed keys:
   - The code creates a file named "collectedKeys.txt" or clears the existing content if the file already exists.

5. Starting the keyboard listener:
   - The `keyboard.on_press` method is used to register the `on_key_press` function as the callback for key press events.

6. Keeping the program running:
   - The code enters a `while` loop and continuously checks if the Alt + Shift + Ctrl + Esc combination is pressed.
   - If the combination is detected, the loop breaks, and the program stops.

## Usage

1. Install the required libraries by running `pip install keyboard`.

2. Run the code in a Python environment.

3. The program will start listening for key presses and saving them to the "collectedKeys.txt" file.

4. Press the Alt + Shift + Ctrl + Esc combination to stop the key logger and exit the program.

## Note

- Make sure to use this code responsibly and respect the privacy of others. Key logging without proper authorization is illegal in many jurisdictions.

- Remember to check and comply with the laws and regulations of your country or region regarding the use of key loggers.