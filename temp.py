import os
import time
import pyautogui

def send_whatsapp_message(phone_number, message):
    # Open WhatsApp Desktop with the specified phone number
    whatsapp_command = f'whatsapp://send?phone={phone_number}'
    os.system(f'start {whatsapp_command}')

    # Wait for WhatsApp to open
    time.sleep(5)  # Adjust based on system speed

    # Type and send the message
    pyautogui.typewrite(message)
    pyautogui.press("enter")

# Example usage
phone_number = "+918989807989"  # Replace with recipient's phone number (with country code)
message = "Hello, this is an automated message from Python!"
send_whatsapp_message(phone_number, message)
