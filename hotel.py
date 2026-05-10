class Hotel:

    def __init__(self):
        self.rooms = {
            101: None,
            102: None,
            103: None,
            104: None
        }

    def show_rooms(self):
        print("\nRoom Status:")
        for room, guest in self.rooms.items():
            if guest is None:
                print(f"Room {room}: Available")
            else:
                print(f"Room {room}: Booked by {guest}")

    def book_room(self, room_no, name):
        if room_no in self.rooms:
            if self.rooms[room_no] is None:
                self.rooms[room_no] = name
                print(f"Room {room_no} booked successfully for {name}")
            else:
                print("Room already booked")
        else:
            print("Invalid room number")

    def checkout(self, room_no):
        if room_no in self.rooms:
            if self.rooms[room_no] is not None:
                print(f"{self.rooms[room_no]} checked out from room {room_no}")
                self.rooms[room_no] = None
            else:
                print("Room already empty")
        else:
            print("Invalid room number")


# Object
hotel = Hotel()

while True:
    print("\n1. Show Rooms\n2. Book Room\n3. Checkout\n4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        hotel.show_rooms()

    elif choice == 2:
        room = int(input("Enter room number: "))
        name = input("Enter customer name: ")
        hotel.book_room(room, name)

    elif choice == 3:
        room = int(input("Enter room number: "))
        hotel.checkout(room)

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")
