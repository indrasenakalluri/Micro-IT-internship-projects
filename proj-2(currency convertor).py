import time

def get_static_exchange_rates():
    # Assuming USD as the base currency for these example rates
    return {
        "USD": 1.0,   # US Dollar (Base)
        "EUR": 0.92,  # Euro
        "GBP": 0.79,  # British Pound
        "JPY": 155.0, # Japanese Yen
        "CAD": 1.37,  # Canadian Dollar
        "AUD": 1.50,  # Australian Dollar
        "CHF": 0.90,  # Swiss Franc
        "CNY": 7.25,  # Chinese Yuan
        "INR": 83.50, # Indian Rupee (Approximate current rate relative to USD)
        "PKR": 278.0, # Pakistani Rupee
        "BDT": 117.0, # Bangladeshi Taka
        "NPR": 133.0, # Nepali Rupee
        "LKR": 300.0, # Sri Lankan Rupee
    }

def display_available_currencies(rates):
    """Prints the list of currencies available for conversion."""
    print("\n--- Available Currencies ---")
    currencies = sorted(rates.keys())
    for currency in currencies:
        print(f"- {currency}")
    print("----------------------------")

def convert_currency():
    """Main function to handle currency conversion."""
    rates = get_static_exchange_rates()
    display_available_currencies(rates)

    while True:
        from_currency = input("Enter the currency you want to convert FROM (e.g., USD): ").upper().strip()
        if from_currency in rates:
            break
        else:
            print("Invalid 'FROM' currency. Please choose from the available list.")

    while True:
        to_currency = input("Enter the currency you want to convert TO (e.g., EUR): ").upper().strip()
        if to_currency in rates:
            break
        else:
            print("Invalid 'TO' currency. Please choose from the available list.")

    while True:
        try:
            amount = float(input(f"Enter the amount in {from_currency}: "))
            if amount >= 0:
                break
            else:
                print("Amount cannot be negative. Please enter a positive number.")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    print(f"\nConverting {amount:.2f} {from_currency} to {to_currency}...")

    # Convert to base currency (USD) first
    amount_in_usd = amount / rates[from_currency]

    # Convert from base currency (USD) to target currency
    converted_amount = amount_in_usd * rates[to_currency]

    print(f"\n{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    print("--- Conversion Complete ---")

# Main application entry point
if __name__ == "__main__":
    print("Welcome to the Simple Currency Converter!")
    print("---------------------------------------")
    print("Note: Exchange rates are static and not real-time.")
    time.sleep(1) # Small delay for better readability

    convert_currency()

    # Option to run again
    while True:
        run_again = input("\nDo you want to perform another conversion? (yes/no): ").lower().strip()
        if run_again == 'yes':
            convert_currency()
        elif run_again == 'no':
            print("Thank you for using the converter. Have a Good Day!")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")