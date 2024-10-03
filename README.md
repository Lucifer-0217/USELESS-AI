```markdown
Useless Version 1 - The Ultimate Desktop Voice Assistant

![Useless Version 1]  
Useful Life Enhancing Software System (Useless)

Overview

Useless Version 1 is a powerful desktop-based voice assistant designed to enhance your productivity and provide hands-free control of your system. Built with cutting-edge AI technology, Useless Version 1 can perform a wide range of tasks including controlling system volume, opening/closing applications, managing windows, interacting with the clipboard, performing Google searches, and even handling basic coding tasks—all via simple voice commands.

This project integrates "OpenAI's GPT-3.5 Turbo" for advanced conversational abilities, allowing the assistant to respond intelligently to both system commands, general inquiries, and coding-related tasks.

Features

Voice-Controlled System Operations

- Open/close applications like Notepad, Calculator, Chrome, etc.
- Manage system volume (mute, unmute, increase, or decrease).
- Open folders (Documents, Downloads).
- Perform system control actions like shutdown, restart, and log off.

Clipboard Interaction
- Copy, paste, and view clipboard content.

Window Management
- Minimize, maximize, and switch between windows.

Google Search Integration
- Perform Google searches directly from voice commands.

Basic Coding Abilities
  - Generate basic Python scripts based on voice commands.
  - The assistant can help write small coding snippets and functions using Python, making it useful for quick coding help.
  - It can assist in debugging or explaining parts of code based on your voice queries.

Conversational Abilities
- Engages in conversations and provides intelligent responses via OpenAI's GPT-3.5.

System Control via PyAutoGUI and PyCaw
  - Desktop interaction with mouse/keyboard control, and audio management using PyCaw.

Installation

Prerequisites

1. Python 3.7 or higher
2. Required dependencies (see below)

Install Required Libraries

Run the following command to install the necessary dependencies:

```bash
pip install -r requirements.txt


```

Alternatively, you can manually install the modules:


```bash
pip install openai pyttsx3 SpeechRecognition pyautogui pyperclip psutil pycaw comtypes
```

Configuration

1. Create a `config.py` file in the root directory and add your OpenAI API key:
   ```python
   apikey = "your_openai_api_key"
   ```

Running the Assistant

To start the voice assistant, simply run the Python script:

```bash
python main.py
```

Upon starting, Useless Version 2 will be ready to listen to your commands!

 Usage

- **Start the assistant**: Once the assistant is running, it will respond to voice commands like:
  - `"Open Notepad"` to open the Notepad application.
  - `"Increase volume"` to adjust system volume.
  - `"Search Google for latest tech news"` to perform a Google search.
  - `"Shut down the system"` to shut down your computer.

- **Coding Assistant**: The AI can help generate basic Python code snippets when you provide instructions via voice commands, like:
  - `"Write a Python function to calculate the factorial of a number."`
  - `"Explain how recursion works in Python."`

- **Conversation**: You can have general conversations with the assistant, ask questions, and interact with it using natural language.

Example Commands

- `"Open Chrome"`
- `"Close Notepad"`
- `"What time is it?"`
- `"Search for Python tutorials"`
- `"Write a Python function to reverse a string"`
- `"Increase volume"`
- `"Mute the volume"`
- `"Tell me about Amit Kasabe"`
- `"Shut down the system"`

Technologies Used

- Python: The core language for building the assistant.
- OpenAI GPT-3.5 Turbo: For natural language processing, conversational abilities, and coding assistance.
- Pyttsx3: For text-to-speech capabilities.
- SpeechRecognition: To recognize and process voice commands.
- PyAutoGUI: For desktop automation (mouse/keyboard interaction).
- PyCaw: For system audio management.
- Psutil: To manage system processes and tasks.
- Pyperclip: To interact with the system clipboard.

Future Improvements

- Add additional application support for popular programs.
- Enhance voice recognition with custom wake words.
- Expand to multi-language support.
- Provide more advanced coding capabilities, such as debugging assistance and integration with IDEs.

License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Contact

Created by **Amit Kasabe** - [LinkedIn](https://www.linkedin.com/in/amit-kasbe-a85896235/)  
For any questions or inquiries, feel free to reach out!

---

Note: This project is for educational and experimental purposes. Feel free to clone, modify, and enhance as needed. Enjoy!

```

Explanation of Changes:
- Basic Coding Abilities: Added a section under features that explains how the assistant can generate simple code snippets and handle coding queries.
- Usage Section: Added examples of how users can interact with the AI to generate basic Python code.
