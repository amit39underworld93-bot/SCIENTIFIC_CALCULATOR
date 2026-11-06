# Scientific Calculator CLI

A light-weight terminal based `Scientific Calculator` with built with Python and NumPy. This application provides a single command-line interface (CLI) to perform fundamental algorithmic, exponential, logarithmic and trigonometric operations quickly and efficiently.

# 🚀 Features

This calculator supports 14 mathematical operations through an interactive menu:

## Basic Arithematic:

- Addition, Subtraction, Multiplication and Division (with `ZeroDivisionError` handling)

## Advanced Mathematics:

- Power calculation and Square Root evaluation (with domain constraints).
- Natural Logarithm (`log`) and Base-10 Logarithm (`log10`), including constraints for non-positive inputs.

## Trigonometry (Evaluates degree via radian conversion):

- Standard trigonometric functions: Sine (`sin`), Cosine (`cosine`), Tangent (`tan`).
- Inverse trigonometric functions: Arcsine (`arcsin`), Arcosine (`arcos`), Arctangent (`arctan`). Includes domain validation ([-1, 1]) for inverse functions to prevent calculation errors.

# 🛠️ Tech Stack

- Language: Python3
- Core Library: NumPy (used for all mathematical evaluations)
- System Operations: `sys` module for graceful exit handaling.

# 💻 How to Run (Installation & Execution)

Follow these steps to run the calculator on a local terminal (e.g.,`Ubuntu`):

1. Clone the repository:
   git clone https://github.com/amit39underworld93-bot/SCIENTIFIC_CALCULATOR.git cd SCIENTIFIC_CALCULATOR

2. Install dependencies (if not already installed):
   This project requires NumPy. Ensure it is installed in your environment.
   `pip install numpy`

3. Execute the script:
   python3 main.py

# 📸 Usage Example

When you run the script, you will see a menu like this:

==== SCIENTIFIC CALCULATOR ====
1. ADDITION
2. SUBTRACTION
3. MULTIPLICATION
4. DIVISION
5. POWER
6. SQUARE ROOT
7. LOGARITHM
8. LOGARITHM WITH BASE 10
9. SIN
10. COS
11. TAN
12. ARCSIN
13. ARCCOS
14. ARCTAN
Enter the choice between 1 to 14:

Simply enter the number corresponding to your desired operation and provide the inputs when prompted.

# 🛡️ Error Handling

The application includes a robust `try-except` blocks to handle:

- Invalid (non-numeric) inputs from the user.

- Domain errors (e.g., negative square roots, logarithm of zero).

- Division by zero errors.
