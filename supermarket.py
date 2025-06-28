import json

def load_vegetables():
    try:
        with open("vegetables.json", "r") as f:
            data = json.load(f)
            return data["vegetables"]
    except FileNotFoundError:
        print("vegetables.json file is missing.")
        return []
    except json.JSONDecodeError:
        print("something wrong in the json file format.")
        return []

def show_menu(vegetables):
    print("\n--- Vegetable Menu ---")
    for i in range(len(vegetables)):
        print(f"{i+1}. {vegetables[i]['name']} ({vegetables[i]['type']}) - Rs.{vegetables[i]['price_per_kg']}/kg")
    print("------------------------")

def buy_item(vegetables):
    try:
        ch = int(input("Enter vegetable number: "))
        if ch >= 1 and ch <= len(vegetables):
            veg = vegetables[ch - 1]
            qty = float(input(f"Enter quantity for {veg['name']} (in kg): "))
            total = qty * veg["price_per_kg"]
            return {
                "name": veg["name"],
                "qty": qty,
                "rate": veg["price_per_kg"],
                "total": total
            }
        else:
            print("Invalid choice.")
    except ValueError:
        print("Enter valid numbers.")
    return None

def print_bill(items):
    print("\n=========== BILL ===========")
    total_amt = 0
    for i in items:
        print(f"{i['name']} - {i['qty']} kg x Rs.{i['rate']} = Rs.{i['total']:.2f}")
        total_amt += i["total"]
    print("----------------------------")
    print(f"Total Payable: Rs.{total_amt:.2f}")
    print("============================")
    return total_amt

def payment(total):
    print("\n--- Payment Method ---")
    print("1. Cash")
    print("2. UPI")
    print("3. Card")
    try:
        mode = int(input("Select option (1/2/3): "))
        if mode == 1:
            print(f"Rs.{total:.2f} received by Cash.")
        elif mode == 2:
            upi = input("Enter UPI ID: ")
            print(f"Payment done via UPI ({upi})")
        elif mode == 3:
            card = input("Enter last 4 digits of card: ")
            print(f"Paid using Card ending with {card}")
        else:
            print("Invalid payment option.")
    except:
        print("Error in payment method.")

def main():
    vegetables = load_vegetables()
    if not vegetables:
        return

    items = []
    while True:
        show_menu(vegetables)
        item = buy_item(vegetables)
        if item:
            items.append(item)
        ask = input("Want to buy more? (yes/no): ").lower()
        if ask != "yes":
            break

    if items:
        total = print_bill(items)
        payment(total)
        print("Thanks for visiting!")
    else:
        print("No item purchased.")

if __name__ == "__main__":
    main()
