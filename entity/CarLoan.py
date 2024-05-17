from .Loan import Loan


class CarLoan(Loan):
    def __init__(
        self,
        loan_id,
        customer,
        principal_amount,
        interest_rate,
        loan_term,
        loan_status,
        car_model,
        car_value,
    ):
        super().__init__(
            loan_id,
            customer,
            principal_amount,
            interest_rate,
            loan_term,
            "CarLoan",
            loan_status,
        )
        self.car_model = car_model
        self.car_value = car_value

    def __str__(self):
        return f"{super().__str__()}\nCar Model: {self.car_model}\nCar Value: {self.car_value}"

    # Getter and setter methods for attributes
    def get_car_model(self):
        return self.car_model

    def set_car_model(self, car_model):
        self.car_model = car_model

    def get_car_value(self):
        return self.car_value

    def set_car_value(self, car_value):
        self.car_value = car_value
