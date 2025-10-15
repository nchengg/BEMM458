#######################################################################
# Week 4 – Activity 3: User Input & while Loops
#
# What you're expected to do
# 1. Build a simple menu loop using while True + break to let a user:
#    - Add an item to a basket
#    - View basket
#    - Checkout (quit)
# 2. Validate input: if the user enters an empty item name, 'continue'.
# 3. When checking out, show basket size and whether it's an even or odd
#    number using the modulo operator (%).
#
# Notes
# - Use input() with clear prompts.
# - Convert numeric input with int() (when needed).
# - Use a 'flag' variable OR while True + break to control the loop.
#######################################################################

basket = []
running = True  # flag example (you can also use while True)

while running:
    print("\nMenu: [1] Add item  [2] View basket  [3] Checkout")
    choice = input("Choose an option (1/2/3): ").strip()

    if choice == "1":
        item = input("Enter item name: ").strip()
        if not item:
            print("Empty item ignored.")
            continue  # go back to menu
        basket.append(item)
        print(f"Added: {item}. Basket size: {len(basket)}")  # OUTPUT:

    elif choice == "2":
        if not basket:
            print("Basket is empty.")  # OUTPUT:
        else:
            print("Basket items:")
            for i, it in enumerate(basket, start=1):
                print(f" {i}. {it}")  # OUTPUT:

    elif choice == "3":
        count = len(basket)
        parity = "even" if count % 2 == 0 else "odd"
        print(f"Checking out... Items: {count} (which is {parity}).")  # OUTPUT:
        running = False  # or use break
    else:
        print("Please choose 1, 2, or 3.")  # OUTPUT:
