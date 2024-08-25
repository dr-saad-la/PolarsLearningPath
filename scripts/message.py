import time

def typewrite_message(message, delay=0.01):
    """
    Print a message to the screen, typewriter style.

    Args:
    - message (str): The message to be printed.
    - delay (float): The delay in seconds between each character.
    """
    for char in message:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

MESSAGE = (
    "\nBefore proceeding, please ensure that you have activated the appropriate "
    "virtual environment for this project.\n"
    "This step is crucial to maintain consistent dependencies and project settings."
)

if __name__ == "__main__":
    typewrite_message("." * 20)
    typewrite_message("Important Reminder:")
    typewrite_message("." * 20)
    typewrite_message(MESSAGE)
    typewrite_message("." * 79)
