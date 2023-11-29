

# Chatbot

## Overview

This Python script implements a versatile chatbot using the `python-wechaty` framework. It showcases various functionalities like responding to messages, handling images, managing room members, and interacting with mini-programs and contacts in a WeChat environment.

## Purpose

The script serves as a multi-functional chatbot that can be integrated into WeChat for various purposes such as automated responses, image processing, room management, and more. It's designed to demonstrate the potential of chatbots in streamlining communication and interaction within a messaging platform.

## Features

- **Automated Text Responses:** Responds to specific text commands with predefined messages.
- **Image Handling:** Processes received images and responds with different image formats.
- **Room Member Management:** Manages room members, including adding, removing, and listing members.
- **Mini-Program Interaction:** Handles and responds to mini-program messages.
- **Friendship Management:** Automates the process of adding new friends and joining them into groups.

## Prerequisites

- Python 3.x
- `python-wechaty` package and its dependencies.

### Installation

To install the required dependencies, use the following command:

```shell
pip install -r requirements.txt
```

## How to Run the Script

1. Ensure all dependencies are installed.
2. Run the chatbot script:

   ```python
   python bot.py
   ```

### Chatbot Behavior

- Responds with 'dong' when a user sends 'ding'.
- Handles different message types including text, images, and mini-programs.
- Allows room management through specific commands like adding or removing members.

## Script Structure

- `MyBot` Class: Inherits from `Wechaty` and overrides event-handling methods such as `on_message`, `on_login`, `on_friendship`, and more.
- `main()`: Initializes and starts the chatbot.

### Example Usage

Send a message 'ding' to the chatbot, and it will reply with 'dong'. You can also interact with the bot using other predefined commands or by sending images and mini-programs.

## Author

[wj-Mcat](https://github.com/wj-Mcat), 吴京京, NLP Researcher, Chatbot Lover

