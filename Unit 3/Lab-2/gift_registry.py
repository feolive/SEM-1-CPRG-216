def user_input():
    gift_sender = input("Who is the gift from? ")
    gift_type = input("Enter gift type (Cash, Gift, Both): ")
    if gift_type.upper() == "CASH":
        cash_amount = input("Enter amount of cash gift: ")
        gift_desc = ""
    elif gift_type.upper() == "BOTH":
        cash_amount = input("Enter amount of cash gift: ")
        gift_desc = input("Enter description of gift: ")
    else:
        cash_amount = 0
        gift_desc = input("Enter description of gift: ")
    gift_type = gift_type.capitalize()
    return gift_sender, gift_type,cash_amount, gift_desc

def write_gift(gift_sender, gift_type, cash_amount, gift_desc):
    f = open("wedding_gifts_copy.txt", "a")
    f.write(f"{gift_sender}\t{gift_type}\t{cash_amount}\t{gift_desc}\n")
    f.close()

def main():
    print("Gift Registry")
    while True:
        another_gift = input("Another gift? (Y/N): ")
        if another_gift.upper() == "N":
            print("File successfully written")
            break
        else:
            gift_sender, gift_type, cash_amount, gift_desc = user_input()
            write_gift(gift_sender, gift_type, cash_amount, gift_desc)

if __name__ == "__main__":
    main()