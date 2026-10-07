from datetime import datetime

# ============================================================
# TOURS & TRAVEL BOOKING MANAGEMENT SYSTEM
# BCS3202 - SYSTEMS PROGRAMMING WITH PYTHON
# ============================================================

FILE_NAME = "bookings.txt"

# Tour choices and their prices per traveller.

TOURS = {
    "1": {"name": "Murchison Falls National Park", "price": 500000},
    "2": {"name": "Queen Elizabeth National Park", "price": 450000},
    "3": {"name": "Bwindi Impenetrable Forest", "price": 600000},
    "4": {"name": "Kidepo Valley National Park", "price": 700000}
}

bookings = []


# ------------------------------------------------------------
# INPUT VALIDATION FUNCTIONS
# ------------------------------------------------------------

def get_customer_name():
    """Ask for and validate the customer's name."""
    while True:
        name = input("Enter customer name: ").strip()

        if not name:
            print("Error: Customer name cannot be empty.")
        elif any(char.isdigit() for char in name):
            print("Error: Customer name should not contain numbers.")
        else:
            return name


def get_travellers():
    """Ask for and validate the number of travellers."""
    while True:
        try:
            travellers = int(input("Enter number of travellers: "))

            if travellers <= 0:
                print("Error: Number of travellers must be greater than 0.")
            else:
                return travellers

        except ValueError:
            print("Error: Please enter a whole number.")


def get_travel_date():
    """Ask for and validate a travel date in YYYY-MM-DD format."""
    while True:
        date_text = input("Enter travel date (YYYY-MM-DD): ").strip()

        try:
            travel_date = datetime.strptime(date_text, "%Y-%m-%d").date()

            if travel_date < datetime.now().date():
                print("Error: Travel date cannot be in the past.")
            else:
                return date_text

        except ValueError:
            print("Error: Invalid date. Use YYYY-MM-DD.")


def get_tour_choice():
    """Display tours and validate the selected tour."""
    print("\nAvailable Tours")
    print("-" * 65)

    for key, tour in TOURS.items(): # loopp over thr TOURS dictionary and value(tour which is another dict) 
        print(
            f"{key}. {tour['name']} - "
            f"UGX {tour['price']:,} per traveller"
        )

    print("-" * 65)

    while True:
        choice = input("Select tour (1-4): ").strip()

        if choice in TOURS:
            return choice

        print("Error: Invalid tour choice. Please select 1, 2, 3 or 4.")


# ------------------------------------------------------------
# BUSINESS RULES AND CALCULATIONS
# ------------------------------------------------------------

def calculate_booking_cost(tour_price, travellers, travel_date):
    """
    Calculate the booking cost using the project's business rules.

    Rule 1: 10% discount for groups of 5 or more.
    Rule 2: 15% surcharge during peak months:
            June, July, August and December.

    Both rules are applied to the base cost when applicable.
    """
    base_cost = tour_price * travellers

    discount = 0
    surcharge = 0

    # Group discount rule
    if travellers >= 5:
        discount = base_cost * 0.10

    discounted_cost = base_cost - discount

    # Peak season surcharge rule
    month = datetime.strptime(travel_date, "%Y-%m-%d").month

    if month in [6, 7, 8, 12]:
        surcharge = discounted_cost * 0.15

    total_cost = discounted_cost + surcharge

    return base_cost, discount, surcharge, total_cost


# ------------------------------------------------------------
# ADD BOOKING
# ------------------------------------------------------------

def add_booking():
    print("\n" + "=" * 65)
    print("ADD NEW BOOKING")
    print("=" * 65)

    customer_name = get_customer_name()
    travellers = get_travellers()
    travel_date = get_travel_date()
    tour_choice = get_tour_choice()

    tour = TOURS[tour_choice]

    base_cost, discount, surcharge, total_cost = calculate_booking_cost(
        tour["price"],
        travellers,
        travel_date
    )

    booking = {
        "customer_name": customer_name,
        "tour": tour["name"],
        "travellers": travellers,
        "travel_date": travel_date,
        "base_cost": base_cost,
        "discount": discount,
        "surcharge": surcharge,
        "total_cost": total_cost
    }

    bookings.append(booking)

    print("\nBooking added successfully!")
    print("-" * 65)
    print(f"Customer:       {customer_name}")
    print(f"Tour:            {tour['name']}")
    print(f"Travellers:      {travellers}")
    print(f"Travel date:     {travel_date}")
    print(f"Base cost:       UGX {base_cost:,.0f}")
    print(f"Group discount:  UGX {discount:,.0f}")
    print(f"Peak surcharge:  UGX {surcharge:,.0f}")
    print(f"TOTAL COST:      UGX {total_cost:,.0f}")
    print("-" * 65)


# ------------------------------------------------------------
# DISPLAY BOOKINGS
# ------------------------------------------------------------

def display_bookings():
    print("\n" + "=" * 100)
    print("ALL STORED BOOKINGS")
    print("=" * 100)

    if not bookings:
        print("No bookings found.")
        return

    print(
        f"{'No.':<5}"
        f"{'Customer':<20}"
        f"{'Tour':<32}"
        f"{'Trav.':<7}"
        f"{'Date':<13}"
        f"{'Total Cost':>15}"
    )
    print("-" * 100)

    for index, booking in enumerate(bookings, start=1):
        tour_name = booking["tour"]

        # Keep the table readable for long tour names.
        if len(tour_name) > 30:
            tour_name = tour_name[:27] + "..."

        print(
            f"{index:<5}"
            f"{booking['customer_name'][:18]:<20}"
            f"{tour_name:<32}"
            f"{booking['travellers']:<7}"
            f"{booking['travel_date']:<13}"
            f"UGX {booking['total_cost']:>10,.0f}"
        )

    print("-" * 100)
    print(f"Total bookings: {len(bookings)}")


# ------------------------------------------------------------
# SEARCH BOOKINGS
# ------------------------------------------------------------

def search_bookings():
    print("\n" + "=" * 65)
    print("SEARCH BOOKINGS")
    print("=" * 65)

    if not bookings:
        print("No bookings available to search.")
        return

    search_term = input(
        "Enter customer name or destination/tour to search: "
    ).strip().lower()

    if not search_term:
        print("Error: Search field cannot be empty.")
        return

    results = []

    for booking in bookings:
        customer = booking["customer_name"].lower()
        tour = booking["tour"].lower()

        if search_term in customer or search_term in tour:
            results.append(booking)

    if not results:
        print("No matching booking was found.")
        return

    print(f"\nFound {len(results)} matching booking(s).")
    print("-" * 100)

    for index, booking in enumerate(results, start=1): # use enumarate so that we can access the index of the record
        print(f"Booking {index}")
        print(f"Customer:       {booking['customer_name']}")
        print(f"Tour:            {booking['tour']}")
        print(f"Travellers:      {booking['travellers']}")
        print(f"Travel date:     {booking['travel_date']}")
        print(f"Base cost:       UGX {booking['base_cost']:,.0f}")
        print(f"Discount:        UGX {booking['discount']:,.0f}")
        print(f"Surcharge:       UGX {booking['surcharge']:,.0f}")
        print(f"Total cost:      UGX {booking['total_cost']:,.0f}")
        print("-" * 100)


# ------------------------------------------------------------
# REVENUE CALCULATION
# ------------------------------------------------------------

def calculate_revenue():
    print("\n" + "=" * 65)
    print("REVENUE SUMMARY")
    print("=" * 65)

    if not bookings:
        print("No bookings available.")
        return

    total_revenue = sum(booking["total_cost"] for booking in bookings)
    total_travellers = sum(
        booking["travellers"] for booking in bookings
    )
    total_discounts = sum(
        booking["discount"] for booking in bookings
    )
    total_surcharges = sum(
        booking["surcharge"] for booking in bookings
    )

    print(f"Number of bookings:     {len(bookings)}")
    print(f"Total travellers:       {total_travellers}")
    print(f"Total discounts given:  UGX {total_discounts:,.0f}")
    print(f"Total peak surcharges:  UGX {total_surcharges:,.0f}")
    print(f"TOTAL REVENUE:          UGX {total_revenue:,.0f}")


# ------------------------------------------------------------
# FILE HANDLING
# ------------------------------------------------------------

def save_bookings():
    """Save all bookings to a text file."""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            for booking in bookings:
                # Use | as a simple field separator.
                line = (
                    f"{booking['customer_name']}|"
                    f"{booking['tour']}|"
                    f"{booking['travellers']}|"
                    f"{booking['travel_date']}|"
                    f"{booking['base_cost']}|"
                    f"{booking['discount']}|"
                    f"{booking['surcharge']}|"
                    f"{booking['total_cost']}\n"
                )
                file.write(line)

        print(f"Bookings saved successfully to {FILE_NAME}.")

    except OSError as error:
        print(f"Error saving bookings: {error}")


def load_bookings():
    """Load previously saved bookings from the text file."""
    try:
        # Clear existing records first to avoid duplicates
        bookings.clear()

        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                fields = line.split("|")

                if len(fields) != 8:
                    print(
                        "Warning: A saved record was skipped "
                        "because it is invalid."
                    )
                    continue

                try:
                    booking = {
                        "customer_name": fields[0],
                        "tour": fields[1],
                        "travellers": int(fields[2]),
                        "travel_date": fields[3],
                        "base_cost": float(fields[4]),
                        "discount": float(fields[5]),
                        "surcharge": float(fields[6]),
                        "total_cost": float(fields[7])
                    }

                    bookings.append(booking)

                except ValueError:
                    print(
                        "Warning: A saved record contained invalid "
                        "data and was skipped."
                    )

        print(f"\n{len(bookings)} booking(s) loaded from {FILE_NAME}.")

        # Display the loaded bookings
        display_bookings()

    except FileNotFoundError:
        # It is normal for the file not to exist the first time
        # the program is run.
        print(
            "No previous booking file found. "
            "Starting with an empty system."
        )

    except OSError as error:
        print(f"Error loading bookings: {error}")


# ------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------

def display_menu():
    print("\n")
    print("=" * 65)
    print("       TOURS & TRAVEL BOOKING MANAGEMENT SYSTEM")
    print("=" * 65)
    print("1. Add a booking")
    print("2. Display all bookings")
    print("3. Search for a booking")
    print("4. Calculate total revenue")
    print("5. Save bookings to file")
    print("6. Load bookings from file")
    print("7. Exit")
    print("=" * 65)


def main():
    print("\nWelcome to the Tours & Travel Booking Management System")

    # Load existing records when the program starts.
    # load_bookings()

    while True:
        display_menu()

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_booking()

        elif choice == "2":
            display_bookings()

        elif choice == "3":
            search_bookings()

        elif choice == "4":
            calculate_revenue()

        elif choice == "5":
            save_bookings()

        elif choice == "6":
            load_bookings()

        elif choice == "7":
            # Save automatically before exiting so that the user
            # does not accidentally lose newly entered bookings.
            save_bookings()
            print("Thank you for using the Tours & Travel Booking Management System.")
            print("Program exited safely.")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 7.")


# Start the program.
if __name__ == "__main__":
    main()
