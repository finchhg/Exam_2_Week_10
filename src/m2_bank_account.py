#  This problem uses a class to create a bank account and simulates some
#  typical banking practices.  Read the instructions carefully and you will be
# successful
def main():
    # when you have initialized your object, use the calls below to test
    run_test_init()
    run_test_withdraw()
    return


class Bank(object):
    """
    A Bank has:
        -- NAME, a string that contains the last name of the bank account holder,
        -- BALANCE, a float that tells the money in the account
        -- ACCOUNT NUMBER, a string that is unique to each account holder.
    """

    def __init__(self, name, initial_deposit, account_number):

        self.name = name
        self.id = initial_deposit
        self.an = account_number
        self.balance = 0

    def __repr__(self):
        value = self.name + '' + self.id + '' + self.an + '' + str(self.withdraw)
        return value

        """
        What comes in:
          -- self
          -- A string that is the name of the account holder
          -- A float that is the initial deposit in the account
          -- A string that is the unique account identifier
        What is returned:
          -- A float that is the current balance in the account
        Side effects:
          -- Stores the name, initial_deposit, account_number
             in the instance variables
          -- Also initializes other instance variables as needed
              by other methods.
        Examples:
          b1 = Bank('Brackin',10000.00, A1)
          #   b1.name is 'Brackin'
          #   b1.balance is 10000.00
          #   b1. account_number is 'A1'

          b2 = Bank('Lovelace',10.15, 'A2')
          #   b2.name is 'Lovelace'
          #   b2.balance is 10.15
          #   b2.account_number is 'A2'

        Type hints:
          :type name: str
          :type balance: float
          :type account_number: str
        """
    # ---------------------------------------------------------------------
    # done: 1. Implement and test instances of this class.
    #     See the testing code (scroll down near bottom) for more examples.
    # ---------------------------------------------------------------------


    def withdraw(self, amount):
        amount = 10
        self.balance = self.id - amount
        """
        What comes in:
        -- self
        -- A float that is the amount to be withdrawn
        What is returned:
        -- An error message if there is not enough money in the account
        -- A float that is the current balance in the account if
           there are sufficient funds
        Side effects:
        -- Updates the balance
        Examples:
          b1.withdraw(8000)
          #   b1.name is 'Brackin'
          #   b1.balance is 2000.00
          #   b1. account_number is 'A1'

          b2.withdraw(50.25)
          #   b2.name is 'Lovelace'
          #   b2.balance is 10.15 (no money is withdrawn)
          #   b2.account_number is 'A2'
          #   an error message is printed because there are insufficient funds
        """
    # ---------------------------------------------------------------------
    # done: 4. Implement and test the withdraw method
    #     Implement your own test code, before you write your method
    #     Insert your test code for withdraw, where indicated
    #     Scroll down near the bottom of this screen
    # ---------------------------------------------------------------------
    #   Put your code for withdraw below
    #
    # ---------------------------------------------------------------------


def run_test_init():
    """ Tests the   __init__   method of the Bank class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   __init__   method of the Bank class.')
    print('-----------------------------------------------------------')

    # Test 1:  Contents fit in the Box easily.
    b1= Bank('Brackin', 10000, 'A1')
    expected_name = 'Brackin'
    expected_balance = 10000
    expected_account_number = 'A1'
    print("Expected:", expected_name, expected_balance, expected_account_number)
    print("Actual:  ", b1.name, b1.id, b1.an)
    if (expected_name == b1.name) and (expected_balance == b1.id) and (expected_account_number == b1.an):
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()
    print()

    b1 = Bank('Jim', 2000000, 'A2')
    expected_name = 'Jim'
    expected_balance = 2000000
    expected_account_number = 'A2'
    print("Expected:", expected_name, expected_balance, expected_account_number)
    print("Actual:  ", b1.name, b1.id, b1.an)
    if (expected_name == b1.name) and (expected_balance == b1.id) and (expected_account_number == b1.an):
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()
    print()

    b1 = Bank('Harry', 20, 'A3')
    expected_name = 'Harry'
    expected_balance = 20
    expected_account_number = 'A3'
    print("Expected:", expected_name, expected_balance, expected_account_number)
    print("Actual:  ", b1.name, b1.id, b1.an)
    if (expected_name == b1.name) and (expected_balance == b1.id) and (expected_account_number == b1.an):
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()
    print()

    # ---------------------------------------------------------------------
    # done: 2. Add two more test cases for your Bank class below.
    # ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# done: 3. Implement your test for the withdraw method below
# ---------------------------------------------------------------------
def run_test_withdraw():
    b1 = Bank('Harry', 20, 'A3')
    expected_name = 'Harry'
    b1.withdraw('Harry')
    expected_balance = 10
    expected_account_number = 'A3'
    print("Expected:", expected_name, expected_balance, expected_account_number)
    print("Actual:  ", b1.name, b1.id, b1.an)
    if (expected_name == b1.name) and (expected_balance == b1.id) and (expected_account_number == b1.an):
        print("Test passed SUCCESSFULLY!")


def print_failure_message():
    print('  *** FAILED the above test. ***')


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ------------------------------------------------------------------------
main()
