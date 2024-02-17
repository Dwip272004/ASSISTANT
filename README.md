
# Voice-Controlled Assistant

This Python script is a voice-controlled assistant named "Friday." It allows users to interact with their computer using voice commands for various tasks such as web searching, controlling browser tabs, scrolling, and mouse actions.

## Features
- **Voice Recognition**: Utilizes the `speech_recognition` library to recognize voice commands from the user.
- **Text-to-Speech**: Implements text-to-speech functionality through the `pyttsx3` library, allowing the assistant to provide responses audibly.
- **Web Searching**: Can perform web searches by opening a browser and searching for user-specified queries using the `webbrowser` module.
- **Browser Control**: Supports closing browser tabs, scrolling up and down, and clicking using the `pyautogui` library.
- **Mouse Control**: Offers the option to control the mouse using hand gestures via the `mcont` module (not included in this repository).

## Getting Started
1. Install the required Python libraries:
   ```
   pip install pyttsx3 speech_recognition pyautogui
   ```
2. Clone this repository or copy the script to your local environment.
3. Run the script:
   ```
   python assistant.py
   ```
4. Follow the initialization instructions provided by the assistant.
5. Speak commands to interact with the assistant.

## Usage
- **Search**: Say "search" followed by the query to perform a web search.
- **Close Tab**: Say "close tab" to close the current browser tab.
- **Scroll Up/Down**: Say "scroll up" or "scroll down" to scroll the page.
- **Click**: Say "click" to perform a left-click action.
- **Control the Mouse**: Say "control the mouse using my hand" to activate hand gesture control (requires additional setup).
- **Stop Controlling the Mouse**: Say "stop controlling the mouse" to deactivate hand gesture control.
- **Exit**: Say "exit" to terminate the assistant.

## Notes
- Ensure your system has a working microphone for voice input.
- Adjust microphone settings if the assistant has difficulty recognizing commands.
- Additional setup may be required for controlling the mouse using hand gestures.

## Contributions
Contributions are welcome! Feel free to submit issues, suggestions, or pull requests.

## License
This project is licensed under the [MIT License](LICENSE).

