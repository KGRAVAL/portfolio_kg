
# Terminal Portfolio Application (Python CLI)

- A structured, terminal-based portfolio application built with Python.
- This project demonstrates strong fundamentals in Python programming, modular design, file handling, and PDF generation directly from a command-line interface.
- The application allows users to navigate through different portfolio sections interactively and export the complete portfolio as a PDF file from within the terminal.

## Overview

- This project simulates a professional portfolio system that runs entirely in the terminal. It provides a clean menu-driven interface and demonstrates the ability to:
    - Design structured CLI applications
    - Implement modular programming practices
    - Handle user input and validation
    - Generate PDF documents programmatically
    - Organize content in a maintainable format

## Features
- Interactive command-line menu
- Dedicated sections:
    -  BIO
    - EDUCATIONAL QUALIFICATION
    - SKILLS
    - CONTACT
- Export full portfolio to PDF
- Clean and readable terminal output
- Simple and extendable architecture

## Application Menu

```bash
1. BIO
2. EDUCATIONAL QUALIFICATION
3. SKILLS
4. CONTACT
5. EXIT
```
Users select an option by entering the corresponding number.

- Technologies Used
  - Python 3.x
  - Object-Oriented Programming (if implemented)
  - File Handling
  - PDF Generation Library (FPDF or ReportLab)
  - Command Line Interface (CLI)

## Installation & Setup
1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

2. Install Dependencies
  - If using FPDF:
    ```bash
    pip install fpdf
  - If using ReportLab:
    ```bash
    pip install reportlab

3. Run the Application
```bash
    python portfolio.py
```

## PDF Export Functionality
  
- The application allows users to generate a PDF version of the portfolio directly from the terminal.

  - The generated file:
    -  Is automatically saved in the project directory
    -  Contains structured portfolio content
    -  Can be shared as a professional document
   
## Project Structure
```bash
├── portfolio.py
├── requirements.txt (optional)
├── README.md
├── generated_portfolio.pdf (after export)
```

