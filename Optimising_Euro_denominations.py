# this code gives the user the good amount of bills depending on the stock of the currency
# this is not very well documented because it is quite simple and repetitive and i wrote it in my first
# stages of learning python
while True:
    def balance_tape(dic):
        amount_of_money = sum([keys * values for keys, values in dic.items()])
        return amount_of_money


    euro_denomination = {50: 800,
                         100: 200,
                         200: 300,
                         20: 500,
                         10: 500,
                         5: 1000}

    print(f"tape balance of euro is currently: {balance_tape(euro_denomination)} €")
    print(euro_denomination)

    amount_to_sell = int(input("Enter the amount of money: "))
    denomination_decision = str(input("Do you perfer big or varied denominations ?: "))
    if denomination_decision == "big":
        total_sum_of_money = balance_tape(euro_denomination)
        new_sum_of_money = total_sum_of_money - amount_to_sell
        print(f"remaining euro balance is:{new_sum_of_money}€")

        denominations = sorted(euro_denomination.keys(), reverse=True)
        number_of_bills = {d: 0 for d in denominations}

        for d in denominations:
            if amount_to_sell >= d:
                number_of_bills[d] = amount_to_sell // d
                amount_to_sell = amount_to_sell % d

        for d in denominations:
            if number_of_bills[d] > 0:
                print(f"number of {d} € bills given is: {number_of_bills[d]}")

        for d in denominations:
            old_euro_value = euro_denomination.get(d)
            new_euro_value = old_euro_value - number_of_bills[d]
            euro_denomination.update({d: new_euro_value})

        print(f"new tape for euro is: {euro_denomination}")
    elif denomination_decision == "varied":
        if amount_to_sell % 11 != 0 and amount_to_sell >= 200:
            if amount_to_sell % 3 == 0:
                half_1 = amount_to_sell // 6
                half_2 = amount_to_sell // 3
                half_3 = amount_to_sell // 2
                amount_10 = half_1 // 10
                amount_20 = half_2 // 20
                amount_50 = half_3 // 50
                total = half_3 + half_2 + half_1
                print(total)
                print(f"number of 50 € bills given is: {amount_50}")
                print(f"number of 20 € bills given is: {amount_20}")
                print(f"number of 10 € bills given is: {amount_10}")
                old_euro_value_50 = euro_denomination.get(50)
                new_euro_value_50 = old_euro_value_50 - amount_50
                old_euro_value_20 = euro_denomination.get(20)
                new_euro_value_20 = old_euro_value_20 - amount_20
                old_euro_value_10 = euro_denomination.get(10)
                new_euro_value_10 = old_euro_value_10 - amount_10
                euro_denomination.update({50: new_euro_value_50})
                euro_denomination.update({20: new_euro_value_20})
                euro_denomination.update({10: new_euro_value_10})
                print(f"new tape for euro is: {euro_denomination}")

            if amount_to_sell % 2 == 0 and amount_to_sell % 5 != 0 and amount_to_sell % 3 != 0:
                total_sum_of_money = balance_tape(euro_denomination)
                new_sum_of_money = total_sum_of_money - amount_to_sell
                print(f"remaining euro balance is:{new_sum_of_money}€")
                half_1 = (amount_to_sell // 4)
                half_2 = (amount_to_sell // 2)
                half_3 = (amount_to_sell // 4)
                total = half_1 + half_2 + half_3
                number_of_bills_50 = half_1 // 50
                number_of_bills_20 = half_2 // 20
                number_of_bills_10 = half_3 // 10
                print(f"number of 50 € bills given is: {number_of_bills_50}")
                print(f"number of 20 € bills given is: {number_of_bills_20}")
                print(f"number of 10 € bills given is: {number_of_bills_10}")
                old_euro_value_50 = euro_denomination.get(50)
                new_euro_value_50 = old_euro_value_50 - number_of_bills_50
                old_euro_value_20 = euro_denomination.get(20)
                new_euro_value_20 = old_euro_value_20 - number_of_bills_20
                old_euro_value_10 = euro_denomination.get(10)
                new_euro_value_10 = old_euro_value_10 - number_of_bills_10
                euro_denomination.update({50: new_euro_value_50})
                euro_denomination.update({20: new_euro_value_20})
                euro_denomination.update({10: new_euro_value_10})
                print(f"new tape for euro is: {euro_denomination}")
            if amount_to_sell % 5 == 0:
                total_sum_of_money = balance_tape(euro_denomination)
                new_sum_of_money = total_sum_of_money - amount_to_sell
                print(f"remaining euro balance is:{new_sum_of_money}€")
                half_1 = (amount_to_sell * 0.6)
                half_2 = (amount_to_sell * 0.2)
                half_3 = (amount_to_sell * 0.2)
                total = half_1 + half_2 + half_3
                number_of_bills_50 = half_1 // 50
                number_of_bills_20 = half_2 // 20
                number_of_bills_10 = half_3 // 10
                print(f"number of 50 € bills given is: {number_of_bills_50}")
                print(f"number of 20 € bills given is: {number_of_bills_20}")
                print(f"number of 10 € bills given is: {number_of_bills_10}")
                old_euro_value_50 = euro_denomination.get(50)
                new_euro_value_50 = old_euro_value_50 - number_of_bills_50
                old_euro_value_20 = euro_denomination.get(20)
                new_euro_value_20 = old_euro_value_20 - number_of_bills_20
                old_euro_value_10 = euro_denomination.get(10)
                new_euro_value_10 = old_euro_value_10 - number_of_bills_10
                euro_denomination.update({50: new_euro_value_50})
                euro_denomination.update({20: new_euro_value_20})
                euro_denomination.update({10: new_euro_value_10})
                print(f"new tape for euro is: {euro_denomination}")

        if amount_to_sell % 11 == 0 and amount_to_sell >= 200:
            if amount_to_sell % 2 == 0:
                total_sum_of_money = balance_tape(euro_denomination)
                new_sum_of_money = total_sum_of_money - amount_to_sell
                print(f"remaining euro balance is:{new_sum_of_money}€")
                half_1 = (amount_to_sell * 0.454545454545454545)
                half_2 = (amount_to_sell * 0.454545454545454545)
                half_3 = (amount_to_sell * 0.1)
                total = half_1 + half_2 + half_3
                number_of_bills_100 = half_1 // 100
                number_of_bills_50 = half_2 // 50
                number_of_bills_20 = half_3 // 20
                print(f"number of 100 € bills given is: {number_of_bills_100}")
                print(f"number of 50 € bills given is: {number_of_bills_50}")
                print(f"number of 20 € bills given is: {number_of_bills_20}")
                old_euro_value_50 = euro_denomination.get(50)
                new_euro_value_50 = old_euro_value_50 - number_of_bills_50
                old_euro_value_20 = euro_denomination.get(20)
                new_euro_value_20 = old_euro_value_20 - number_of_bills_20
                old_euro_value_100 = euro_denomination.get(100)
                new_euro_value_100 = old_euro_value_100 - number_of_bills_100
                euro_denomination.update({50: new_euro_value_50})
                euro_denomination.update({20: new_euro_value_20})
                euro_denomination.update({100: new_euro_value_100})
                print(f"new tape for euro is: {euro_denomination}")

