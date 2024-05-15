class InvalidLoanException(Exception):
    """Exception raised for invalid loan operations."""

    def __init__(self, message="Invalid loan operation"):
        self.message = message
        super().__init__(self.message)
