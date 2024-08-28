# Design a console based application for Converting different currency. You are required to ask
# user to choose input which currency you want to convert and then ask the amount. After that
# ask in which currency you want to convert. Then convert that currency into desired one...
# (Currency should includ Euro , Dollar, PkR, INR , and yen)

def main():

    rates = {
        'PKR': 1,  
        'USD': 287,   
        'EUR': 314,    
        'INR': 3.46,      
        'YEN': 1.9       
    }

    currency = input("Which currency you want to convert(Euro , Dollar, PkR, INR ,Yen): ").upper()
    amount = int(input("Amount: "))
    convert_currency = input("In which currency you want to convert(Euro , Dollar, PkR, INR ,Yen): ").upper()

    if currency not in rates or convert_currency not in rates:
        print("Choose from the given options.")
        exit()


    converted_amount = convert_currency(amount, currency, convert_currency, rates)
    print(f"{amount} {currency} is equal to {converted_amount: } {convert_currency}")


def convert_currency(amount, from_currency, to_currency, rates):
    # Convert from 'from_currency' to PKR first
    amount_in_pkr = amount * rates[from_currency]
    # Convert from PKR to 'to_currency'
    converted_amount = amount_in_pkr / rates[to_currency]

    return converted_amount


main()





