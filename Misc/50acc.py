from FinalReview import Account
def main():

    user_deposit = int(input(f'Enter an amount which you would like to deposit in all the accounts'))
    accounts = []
    for index in range(0, 50):
        account = Account()
        accounts.append(Account())
        account.deposit(user_deposit)
    return accounts



main()