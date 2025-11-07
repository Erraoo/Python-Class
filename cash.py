money_list = ["$"]
rows = int(input("Please type the number of rows to print: "))


def dollar_rows(rows):
    for i in range(rows):
        print(" ".join(money_list))
        money_list.append("$")

dollar_rows(rows)