import functions


def main():
    is_playing = True

    while is_playing:
        is_deposit = True

        while is_deposit:
            balance = input("⭐Deposit credits⭐: ")

            try:
                balance = int(balance)
            except ValueError:
                print("⭐Invalid deposit⭐")

                continue

            if balance <= 0:
                print("⭐Deposit can not be less or equal to 0⭐")

                continue

            is_deposit = False

        print("***************")
        print(" Python Slots")
        print("🍒 🍉 🍓 🔔 ⭐")
        print("***************")

        is_slots_playing = True

        while is_slots_playing:
            print(f"YOUR BALANCE IS ${balance}\n")

            bet = input("Place your bet: ")

            if not bet.isdigit():
                print("\n⭐Invalid bet⭐\n")

                continue

            bet = int(bet)

            if bet > balance:
                print("\n⭐Insufficient funds⭐\n")

                continue

            if bet <= 0:
                print("\n⭐You can not bet 0 or less⭐\n")

                continue

            balance -= bet

            row = functions.spin_row()
            functions.print_row(row)
            payout = functions.give_payout(row, bet)
            balance += payout

            if balance == 0:
                is_slots_playing = False
                is_deposit = True

            if payout > 0:
                print(f"\n💲💲💲You won ${payout}!💲💲💲\n")

            print(f"\n⭐Your balance is {balance}⭐")
            play_again = input("⭐Spin again? Y/N⭐: ").upper()
            print("\n************\n")

            if play_again != 'Y':
                is_slots_playing = False
                is_playing = False
                print(f"\nYour final balance is 💲💲💲{balance}💲💲💲\n")
                print("\n🍒 🍉 🍓 🔔 ⭐ GAME OVER ⭐ 🔔 🍓 🍉 🍒\n")


if __name__ == "__main__":
    main()
