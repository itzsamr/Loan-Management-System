class Loan:
    def __init__(
        self,
        loan_id,
        customer,
        principal_amount,
        interest_rate,
        loan_term,
        loan_type,
        loan_status,
    ):
        self.loan_id = loan_id
        self.customer = customer
        self.principal_amount = principal_amount
        self.interest_rate = interest_rate
        self.loan_term = loan_term
        self.loan_type = loan_type
        self.loan_status = loan_status

    def __str__(self):
        return f"Loan ID: {self.loan_id}\nCustomer: {self.customer}\nPrincipal Amount: {self.principal_amount}\nInterest Rate: {self.interest_rate}\nLoan Term: {self.loan_term}\nLoan Type: {self.loan_type}\nLoan Status: {self.loan_status}"

    # Getter and setter methods for attributes
    def get_loan_id(self):
        return self.loan_id

    def set_loan_id(self, loan_id):
        self.loan_id = loan_id

    def get_customer(self):
        return self.customer

    def set_customer(self, customer):
        self.customer = customer

    def get_principal_amount(self):
        return self.principal_amount

    def set_principal_amount(self, principal_amount):
        self.principal_amount = principal_amount

    def get_interest_rate(self):
        return self.interest_rate

    def set_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate

    def get_loan_term(self):
        return self.loan_term

    def set_loan_term(self, loan_term):
        self.loan_term = loan_term

    def get_loan_type(self):
        return self.loan_type

    def set_loan_type(self, loan_type):
        self.loan_type = loan_type

    def get_loan_status(self):
        return self.loan_status

    def set_loan_status(self, loan_status):
        self.loan_status = loan_status
