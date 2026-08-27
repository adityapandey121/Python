class Customer:
    def __init__(self, customer_id, name, email, licence_number):
        fields = {
            "Customer ID": customer_id,
            "Name": name,
            "Email": email,
            "Driving licence number": licence_number,
        }

        for field_name, value in fields.items():
            if not value or not str(value).strip():
                raise ValueError(f"{field_name} cannot be empty.")

        self.__customer_id = customer_id
        self.__name = name
        self.__email = email
        self.__licence_number = licence_number
        self.__rental_history = []

    @property
    def customer_id(self):
        return self.__customer_id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def licence_number(self):
        return self.__licence_number

    @property
    def rental_history(self):
        return tuple(self.__rental_history)

    def add_rental(self, rental):
        self.__rental_history.append(rental)

    def display_details(self):
        return (
            f"{self.customer_id} | {self.name} | "
            f"{self.email} | Licence: {self.licence_number} | "
            f"Rentals: {len(self.__rental_history)}"
        )
