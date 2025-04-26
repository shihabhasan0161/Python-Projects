# Pinnocchio's Pizza Ordering System 🍕

## Video Demo
[Click here to watch the demo!](<https://youtu.be/02niIVA6jiU>)

## Description

For my CS50 final project, I created **Pinnocchio's Pizza Ordering System**, a command-line Python application that simulates ordering pizzas at a pizzeria.

The application allows users to:
- View the pizza menu (Regular or Sicilian options)
- Add pizzas to a cart by selecting size and item
- Remove items from the cart if needed
- Checkout to see a bill with the total cost
- Generate and save a PDF invoice with a custom header image

## Technologies Used
- **Python 3**
- **CSV module** – for reading menu data from `regular.csv` and `sicilian.csv`
- **Tabulate** – to format menus and cart cont


ents into neat tables
- **FPDF** – to create a professional invoice PDF with the order summary

## How It Works
1. The user is greeted with a welcome message and options to view the menu, checkout, remove an item, or exit.
2. Upon choosing the menu option, the user selects between Regular and Sicilian pizzas, then adds their desired items to the cart.
3. The user can remove items from their cart or proceed to checkout.
4. At checkout, the application calculates the total price and generates an invoice in PDF format, including a header image.
5. The invoice is saved as `invoice.pdf`.

## Features
- User-friendly command-line interface
- Error handling for invalid inputs and missing files
- Clean display of menus and cart items
- PDF invoice generation with a header image
- Organized and modular code structure

## What I Learned
Through building this project, I gained deeper experience with:
- Working with file I/O and CSV data
- Managing user input validation in a real-world simulation
- Generating PDFs programmatically with layout design
- Structuring larger Python programs into modular, reusable functions

---

Thank you for checking out Pinnocchio's Pizza Ordering System! 🍕
