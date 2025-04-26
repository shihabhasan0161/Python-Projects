import csv
from tabulate import tabulate
from fpdf import FPDF

cart = [] # Global cart list to store selected items across the session

def main():
    welcome_message = f"""
    ════════════════════════════════════════════════════
          Welcome to Pinnocchio's Pizza & Subs 😀
    ════════════════════════════════════════════════════
          We're happy to serve you hot & fresh 🍕

      Options:
      1. Menu     - See the full menu
      2. Checkout - Place your order
      3. Remove   - Remove an item from your cart
      4. Exit     - Leave the pizzeria
    ════════════════════════════════════════════════════
    """
    print(welcome_message)
    menu()

def menu():

     # Display and handle main menu options in a loop
    while True:
        user_input = input("Enter an option from (1-4): ").strip().lower()
        if user_input == '4' or user_input == 'exit':
            print('Thanks for coming. Have a nice day!')
            break
        elif user_input == '1' or user_input == 'menu':
            # Prompt user to choose between Regular or Sicilian menu
            print(f"""
                Options:
                  1. Regular
                  2. Sicilian
                  3. Exit
            """)
            choose_pizza = input("Which pizza would you like to order? ").strip().lower()
            if choose_pizza == '1' or choose_pizza == 'regular':
                file = "regular.csv"
            elif choose_pizza == '2' or choose_pizza == 'sicilian':
                file = "sicilian.csv"
            elif choose_pizza == '3' or choose_pizza == 'exit':
                continue
            else:
                print("Invalid Option")
                continue

            # Load menu and pass data to cart function
            menu_table = showmenu(file)
            if menu_table:
                add_to_cart(menu_table, file.split('.')[0].capitalize())

        elif user_input == '2' or user_input == 'Checkout':
            checkout()
            break
        elif user_input == '3' or user_input == 'Remove':
            remove_item()
        else:
            print("Invalid Option")

def showmenu(file):
    # Load menu from CSV file and display as a formatted table
    try:
        with open(file, newline='') as f:
            reader = csv.reader(f)
            headers = next(reader)
            table = [row for row in reader] #store the rows into a table
            print("\n" + tabulate(table, headers, tablefmt="fancy_grid"))
            return table
    except FileNotFoundError:
        print("File Not Found")
        return None

def add_to_cart(menu_table, pizza_type):
    # Add selected pizza to the cart
    option = input("Enter option number: ").strip()
    size = input("Enter size (Small or Large): ").strip().capitalize()

    for row in menu_table:
        if row[0] == option:
            if size == "Small":
                price = row[2]
            elif size == "Large":
                price = row[3]
            else:
                print("Invalid Size")
                return

            item = [pizza_type, row[1], price, size]
            cart.append(item)
            print(f"✅ Added {row[1]} {size} size Pizza to your cart. Price is {price}.")
            return

    print("Invalid Option or Size")

def remove_item():
    # Remove a selected item from the cart
    if not cart:
        print("Cart is empty")
    else:
        print("\nItems in the cart: ")

    for i, item in enumerate(cart, 1):
        print(f"{i}. {item[1]} ({item[3]}) - {item[2]}")

    if cart:

        number = input("Enter the number of the item to remove: ").strip()

        try:
            remove = cart.pop(int(number) - 1)
            print(f"❌ Removed {remove[1]} ({remove[3]})")
        except:
            print("Invalid Option")

def checkout():
    # Finalize order, print summary, and save invoice
    if not cart:
        print("Your cart is empty.")
        menu()

    print("\n🧾 Your Order:")
    print(tabulate(cart, headers=["Pizza Type", "Item", "Price", "Size"], tablefmt="grid"))

    total = sum(float(item[2].replace('$', '')) for item in cart)
    print(f"\n💰 Total: ${total:.2f}")

    save_pdf_invoice(cart, total)
    print("📄 Invoice saved as invoice.pdf")
    print("Thank you for ordering!")


def save_pdf_invoice(cart, total):
    #Use the FPDF Library to design the invoice PDF file and export it as "invoice.pdf"
    pdf = FPDF()
    pdf.add_page()

    #Add the image to the header
    pdf.image("project.png", x=0, y=0, w=210)
    pdf.set_y(40)

    pdf.set_font("helvetica", size=16)
    pdf.ln(10)

    pdf.set_font("helvetica", size=12)
    pdf.set_fill_color(240, 240, 240)
    pdf.cell(50, 10, "Pizza Type", 1, 0, "C", True)
    pdf.cell(60, 10, "Item", 1, 0, "C", True)
    pdf.cell(30, 10, "Price", 1, 0, "C", True)
    pdf.cell(30, 10, "Size", 1, 1, "C", True)

    # Add items from cart to the PDF
    for row in cart:
        pdf.cell(50, 10, row[0], 1)
        pdf.cell(60, 10, row[1], 1)
        pdf.cell(30, 10, row[2], 1)
        pdf.cell(30, 10, row[3], 1)
        pdf.ln()

    pdf.ln(5)
    pdf.set_font("helvetica", "B", 12)
    pdf.cell(0, 10, f"Total: ${total:.2f}", ln=True, align="R")

    pdf.output("invoice.pdf")


if __name__ == "__main__":
    main()
