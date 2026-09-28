# Friendship Compatibility Analyzer

## Overview
A simple desktop application that calculates friendship compatibility between two people based on their names.  
It uses **Python lists (arrays)** to process letters, removes common characters, and generates a fun percentage score with a message.

This project is designed for Semester-1 students and follows modular programming practices.

## Features
- Clean Tkinter GUI
- Input validation
- Compatibility calculation using lists
- Result display with friendly messages
- History of previous checks
- Clear / Reset functionality

## Technologies Used
- Python 3
- Tkinter (built-in GUI library)
- Standard Python lists and file handling

## How to Run
1. Make sure Python 3 is installed on your system.
2. Open a terminal / command prompt in this folder.
3. Run the following command:

```bash
python main.py
```

or

```bash
python3 main.py
```

## Project Structure
```
Friendship_Compatibility_Analyzer/
├── main.py                  # Entry point
├── gui.py                   # GUI code
├── validator.py             # Input validation
├── calculator.py            # Core calculation logic (lists)
├── history_manager.py       # History management
├── utils.py                 # Helper functions
├── statement.md             # Project statement
└── README.md                # This file
```

## Testing
- Enter two valid names and click "Check Compatibility"
- Try empty fields or numbers to test validation
- Check the History section after a few calculations
- Use Clear button to reset

## Author
Semester-1 Student Project – VITyarthi
