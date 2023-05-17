"""Provides the CreditCard class as an example of a class definition."""

class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance.

        The initial balance is zero.

        customer  the name of the customer (e.g., 'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the acount identifier (e.g., '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank

    def get_account(self):
        """Return the card's identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def charge(self, price):
        """Charge the given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit:    # if charge would exceed limit,
            return False                           # cannot accept charge
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment, which reduces balance."""
        self._balance -= amount

if __name__ == '__main__':
    primary_card = CreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500)
    rewards_card = CreditCard('John Bowman', 'California Federal', '3485 0399 3395 1954', 3500)

    if primary_card.get_bank() != 'California Savings':
        print('Problem with recording of bank')
    if rewards_card.get_bank() != 'California Federal':
        print('Problem with recording of bank')

    if not rewards_card.charge(1000):
        print('Initial charge of $1000 should not be rejected')
    if rewards_card.get_balance() != 1000:
        print('Problem with balance')
    rewards_card.charge(2000)
    if rewards_card.get_balance() != 3000:
        print('Problem with balance')

    # try going over the credit limit
    if rewards_card.charge(1000):
        print('Charge should have been denied')
    if rewards_card.get_balance() != 3000:
        print('Failed charge should not have impacted balance')

    if primary_card.get_balance() != 0:
        print('Problem as primary card should still have zero balance.')
