class Train:
    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare

    def book_ticket(self):
        if self.seats > 0:
            self.seats -= 1
            print("Ticket booked successfully!")
        else:
            print("Sorry, no seats availbale.")

    def get_status(self):
        print(f"Seats available: {self.seats}")

    def get_fare_info(self):
        print(f"Fare for the train {self.name} is ₹{self.fare}")


rajdhani = Train("Rajdhani Express", 5, 120)

rajdhani.get_status()
rajdhani.book_ticket()
rajdhani.get_fare_info()
