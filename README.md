# 🧳 Tours & Travel Booking Management System

A **Python command-line application** for managing tour and travel bookings for a Ugandan tour operator.

This project was developed as part of **BCS3202 – Systems Programming with Python, Group Coursework 2**.

The system replaces manual booking records with a simple computerized solution that allows a travel agent to create, view, search, calculate, save, and load customer bookings.

---

## 📌 Project Overview

Many small tour and travel companies still manage customer bookings using paper records or scattered notes. This can lead to:

* Lost or duplicated booking records
* Incorrect tour cost calculations
* Difficulty finding customer bookings
* Errors when applying discounts or peak-season charges
* Difficulty calculating total revenue

This project provides a simple Python-based solution that stores booking information, automatically calculates costs, applies business rules, and saves records permanently in a text file.

---

## 🎯 Project Objectives

The system is designed to:

* Record customer booking information
* Display all stored bookings
* Search for bookings by customer name or tour
* Calculate the total cost of a booking
* Calculate total revenue
* Apply group discounts
* Apply peak-season surcharges
* Validate user input
* Save booking records to a text file
* Load previously saved records
* Exit the application safely

---

## ✨ Features

### 1. Add Booking

The travel agent can create a new booking by entering:

* Customer name
* Number of travellers
* Travel date
* Selected tour

The system automatically calculates the final booking cost.

---

### 2. View Bookings

All stored bookings can be displayed in a clear table containing:

* Booking number
* Customer name
* Tour
* Number of travellers
* Travel date
* Total booking cost

---

### 3. Search Bookings

Bookings can be searched using:

* Customer name
* Tour/destination

The search is case-insensitive, making it easier to find records.

---

### 4. Calculate Revenue

The system calculates:

* Total number of bookings
* Total number of travellers
* Total discounts given
* Total peak-season surcharges
* Total revenue

---

## 💰 Business Rules

The system automatically applies the business rules defined for the project.

### Group Discount

Customers travelling in groups of **5 or more** receive a:

**10% discount**

Example:

```text
Number of travellers = 5
Base cost = UGX 2,500,000

10% discount = UGX 250,000

Cost after discount = UGX 2,250,000
```

### Peak Season Surcharge

Bookings made during the following peak months receive a:

**15% surcharge**

Peak months:

* June
* July
* August
* December

The surcharge is calculated after applying any applicable group discount.

---

## 🗺️ Available Tours

The current system contains four sample tour destinations:

| No. | Tour                          | Price per Traveller |
| --- | ----------------------------- | ------------------: |
| 1   | Murchison Falls National Park |         UGX 500,000 |
| 2   | Queen Elizabeth National Park |         UGX 450,000 |
| 3   | Bwindi Impenetrable Forest    |         UGX 600,000 |
| 4   | Kidepo Valley National Park   |         UGX 700,000 |

> **Note:** These prices are sample implementation values and can be changed in the `TOURS` dictionary in the Python program.

---

## 🖥️ Application Menu

When the program starts, the travel agent is presented with a menu similar to:

```text
===============================================================
       TOURS & TRAVEL BOOKING MANAGEMENT SYSTEM
===============================================================
1. Add a booking
2. Display all bookings
3. Search for a booking
4. Calculate total revenue
5. Save bookings to file
6. Load bookings from file
7. Exit
===============================================================
```

---

## 📂 Project Structure

```text
tours-travel-booking-system/
│
├── tours_travel_booking_system.py
├── bookings.txt
└── README.md
```

### `tours_travel_booking_system.py`

Contains the complete Python application, including:

* User input
* Input validation
* Booking management
* Cost calculation
* Business rules
* Searching
* Revenue calculation
* File handling
* Main menu

### `bookings.txt`

A text file used to permanently store booking records.

The file is automatically created when bookings are saved.

### `README.md`

Documentation explaining the project, its features and how to run it.

---

## 💾 Data Storage

The application uses a simple text file called:

```text
bookings.txt
```

Each booking is stored as a single line with fields separated by `|`.

Example:

```text
John Smith|Murchison Falls National Park|4|2026-11-15|2000000|0|0|2000000
```

The stored fields are:

```text
customer_name
tour
travellers
travel_date
base_cost
discount
surcharge
total_cost
```

This approach demonstrates Python file handling without requiring an external database.

---

## 🔄 Loading Saved Records

When the program starts, it checks whether `bookings.txt` exists.

If previous bookings are available, they are loaded into the application.

The user can also manually select:

```text
6. Load bookings from file
```

The loaded records are then displayed in the booking table.

---

## ✅ Input Validation

The system validates several user inputs to prevent incorrect data from crashing the program.

### Customer Name

The name:

* Cannot be empty
* Cannot contain numbers

### Number of Travellers

The system checks that:

* The input is a valid whole number
* The number is greater than zero

### Travel Date

The system:

* Requires the format `YYYY-MM-DD`
* Rejects invalid dates
* Rejects dates in the past

Example:

```text
Enter travel date (YYYY-MM-DD): 2026-12-15
```

### Tour Selection

The user must select one of the available tour options.

Invalid selections are rejected and the user is asked to try again.

---

## 🛠️ Technologies Used

The project uses **core Python**, including:

* Python functions
* Lists
* Dictionaries
* Conditional statements
* Loops
* Exception handling
* File handling
* `datetime` module
* String processing

No external Python libraries are required.

---

## 🚀 How to Run the Application

### 1. Install Python

Make sure Python 3 is installed.

Check your installation:

```bash
python3 --version
```

or:

```bash
python --version
```

---

### 2. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Move into the project directory:

```bash
cd YOUR-REPOSITORY
```

---

### 3. Run the Program

On macOS/Linux:

```bash
python3 tours_travel_booking_system.py
```

On Windows:

```bash
python tours_travel_booking_system.py
```

---

## 🧪 Example Booking

A travel agent can enter:

```text
Customer name: John Smith
Number of travellers: 5
Travel date: 2026-12-15
Tour: Murchison Falls National Park
```

The system calculates:

```text
Base cost:       UGX 2,500,000
Group discount:  UGX   250,000
Peak surcharge:  UGX   337,500
Total cost:      UGX 2,587,500
```

The booking can then be saved to `bookings.txt`.

---

## 📋 System Requirements Coverage

The project satisfies the required functional requirements for the coursework:

| Requirement                | Status | Implementation                  |
| -------------------------- | ------ | ------------------------------- |
| Add a record               | ✅      | Add booking                     |
| Display stored records     | ✅      | Display all bookings            |
| Search for a record        | ✅      | Search by customer/tour         |
| Calculate meaningful value | ✅      | Booking cost and revenue        |
| Apply decision rule        | ✅      | Discount and surcharge          |
| Save to text file          | ✅      | `bookings.txt`                  |
| Load from text file        | ✅      | File loading function           |
| Exit safely                | ✅      | Automatic save before exit      |
| Validate user input        | ✅      | Name, travellers, date and tour |

---

## 👤 System Actor

The primary actor in the system is the:

**Travel Agent / Staff Member**

The travel agent uses the application to:

```text
Enter Booking
      ↓
Validate Information
      ↓
Calculate Cost
      ↓
Apply Business Rules
      ↓
Store Booking
      ↓
Save to File
      ↓
Display / Search / Calculate Revenue
```

---

## 🔮 Future Improvements

The current application can be extended with additional functionality, such as:

* Booking cancellation
* Booking modification
* Customer contact information
* Payment tracking
* Booking status
* More tour destinations
* More advanced reporting
* Graphical user interface
* Database storage
* User authentication
* Printable booking receipts
* Online booking functionality

---

## 🎓 Academic Context

**Course:** BCS3202 – Systems Programming with Python

**Project:** Group Coursework 2

**Project:** Tours & Travel Booking Management System

**Organization:** Ugandan Tour Operator

**Application Type:** Python Command-Line Application

---

## 👥 Group Members

Add the names and registration numbers of all group members below:

```text
1. Name - Registration Number
2. Name - Registration Number
3. Name - Registration Number
4. Name - Registration Number
```

---

## 🎥 Project Demonstration

**YouTube Demo:**
[https://youtu.be/TTXZMczJzps]

The demonstration video shows the main functionality of the system, including:

* Adding bookings
* Viewing bookings
* Searching bookings
* Calculating revenue
* Applying business rules
* Saving records
* Loading records
* Input validation
* Safely exiting the application

---

## 📸 Project Thumbnail

The project demonstration uses a visual theme representing a Python command-line application for tours and travel management.

---

## 📄 License

This project was developed for academic purposes as part of the BCS3202 Systems Programming with Python coursework.
