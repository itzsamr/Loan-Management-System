from dao.ILoanRepositoryImpl import ILoanRepositoryImpl


class MainModule:
    @staticmethod
    def main():
        loan_repository = ILoanRepositoryImpl()
        # Implement menu-driven operations


if __name__ == "__main__":
    MainModule.main()
