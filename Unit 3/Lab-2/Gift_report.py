def main():
    #counter for the number of cash gifts
    cash_gifts = 0
    #cash gift amount
    cash_gift_amount = 0
    # Open the file in read mode
    f = open("wedding_gifts_copy.txt", "r")
    for line in f.readlines():
        cash_gifts += 1
        line = line.split("\t")
        if line[1]=="Cash" or line[1]=="Both":
            cash_gift_amount += float(line[2])
    f.close()
    print(f"Received {cash_gifts}  gifts including cash of ${cash_gift_amount:,.2f}")

if __name__ == "__main__":
    main()