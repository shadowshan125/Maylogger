import keyboard
import os

def save_content(content, filename):
    # Check if the file already exists
    if os.path.isfile(filename):
        base_name, extension = os.path.splitext(filename)
        counter = 1
        new_filename = f"{base_name}_{counter}{extension}"

        # Find an available filename by incrementing the counter
        while os.path.isfile(new_filename):
            counter += 1
            new_filename = f"{base_name}_{counter}{extension}"

        filename = new_filename

    # Write content to the file
    with open(filename, 'w') as file:
        file.write(content)

    print(f"File saved as {filename}")

# Define a callback function for key press events
def on_key_press(event):
    # Check if the combination Alt + Shift + Ctrl + Esc is pressed
    if event.name == 'esc' and keyboard.is_pressed('alt') and keyboard.is_pressed('shift') and keyboard.is_pressed('ctrl'):
        keyboard.unhook_all()  # Stop the keyboard listener

        # Save the content to a file
        content = event.name
        filename = "collectedKeys.txt"
        save_content(content, filename)

    # Print the pressed key
    #print(event.name)

# Start the keyboard listener
keyboard.on_press(on_key_press)

# Keep the program running until the Alt + Shift + Ctrl + Esc combination is pressed
while True:
    if keyboard.is_pressed('alt') and keyboard.is_pressed('shift') and keyboard.is_pressed('ctrl') and keyboard.is_pressed('esc'):
        break

# The keyboard listener will stop automatically after the combination is pressed


