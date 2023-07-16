# Windows Run Ripoff 🪟

This is a Python script using the Tkinter library to create a simple graphical user interface (GUI) application. The application allows the user to enter a program path and run it using the `os.system()` function. The program also includes some custom widgets from a module called `customtkinter`.

## Table of Contents

- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Customization](#-customization)
- [License](#-license)

## Prerequisites

To run this script, you need to have Python installed on your system. The script is compatible with Python 3.

## Installation

1. Clone or download this repository to your local machine.
2. Make sure you have the necessary dependencies installed. You can install them using the following command:

```
pip install customtkinter
```

## Usage

1. Open a terminal or command prompt and navigate to the directory where the script is located.
2. Run the script using the following command:

```
python main.py
```

3. The GUI application window will appear.
4. Enter the path of the program you want to run in the text entry field labeled "Enter program."
5. Click the "Run" button to execute the program.
6. If you don't specify a path in the text entry field, an error message will be displayed in red text below the button.

## Customization

The script uses a custom module called `customtkinter` to create some of the GUI widgets. If you want to modify the appearance or behavior of these widgets, you can edit the `customtkinter.py` file.

You can also customize other aspects of the script, such as the window title, size, and icon. To do this, modify the relevant lines in the main script file.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to use, modify, and distribute the code as per the terms of the license.

---

Please note that the above README assumes the `customtkinter` module and `icon.ico` file are available and correctly implemented. Make sure you have the necessary files in place for the code to work properly.
