import json
import urllib.request


def main():
    while True:
        command = input("Enter a command:\n"
                        "sign_in\n"
                        "log_in\n"
                        "delete_account\n"
                        "search\n"
                        "add\n"
                        "check_cart\n"
                        "buy\n"
                        "cancel\n")

        if "sign_in" in command:
            arguments = input("Enter the arguments: FirstName LastName Email Password\n").split()
            url = f"http://server:5000/sign_in?fN=${arguments[0]}&lN={arguments[1]}" \
                  f"&e={arguments[2]}&p={arguments[3]}"

            response = urllib.request.urlopen(url)
            data = json.loads(response.read().decode())

            if "exists" in data['sign_in']:
                print("This email already exists")
            if data['sign_in'][0] is True:
                print("You have successfully registered.\n")

        if "log_in" in command:
            arguments = input("Enter the arguments: Email Password\n").split()
            url = f"http://server:5000/log_in?e={arguments[0]}&p={arguments[1]}"
            response = urllib.request.urlopen(url)
            data = json.loads(response.read().decode())

            if data['log_in'] is True:
                print("Correct password\n")
            elif data['log_in'] is False:
                print("Incorrect password\n")

        if "delete_account" in command:
            arguments = input("Enter the arguments: Email Password\n").split()
            url = f"http://server:5000/delete_account?e={arguments[0]}&p={arguments[1]}"
            response = urllib.request.urlopen(url)
            data = json.loads(response.read().decode())

            if data['delete_account']:
                print("You have successfully deleted your account.\n")

        if "search" in command:
            arguments = input("Enter the arguments: Source Destination DayOfLeaving\n").split()
            url = f"http://server:5000/search?src={arguments[0]}&dest={arguments[1]}&day={int(arguments[2])}"
            response = urllib.request.urlopen(url)
            trips = json.loads(response.read().decode())

            [print(
                f"Source: {trip[0]} | Destination: {trip[1]} | Day: {trip[2]} | LeaveHour: {trip[3]}"
                f"| ArriveHour: {trip[4]} | AvailableSeats: {trip[5]} | Price: {trip[6]} | TripId: {trip[7]}")
                for trip in trips['trips']
            ]

        if "add" in command:
            arguments = input("Enter the arguments: Email TripId\n").split()
            url = f"http://server:5000/add_to_cart?e={arguments[0]}&&id={int(arguments[1])}"
            response = urllib.request.urlopen(url)
            trips = json.loads(response.read().decode())

            if (trips["ticket"] != None):
                print("Your ticket has been successfully reserved.\n")
                [print(
                    f"TripId: {trip[0]} | TicketType: {trip[1]}")
                    for trip in trips['ticket']
                ]
            else:
                print("You cannot reserve the ticket.\n")

        if "check" in command:
            arguments = input("Enter the arguments: Email\n").split()
            url = f"http://server:5000/check_cart?e={arguments[0]}"
            response = urllib.request.urlopen(url)
            trips = json.loads(response.read().decode())

            if (trips["ticket"] != None):
                [print(
                    f"TripId: {trip[0]} | TicketType: {trip[1]}")
                    for trip in trips['ticket']
                ]
            else:
                print("Your cart is empty.\n")

        if "buy" in command:
            arguments = input("Enter the arguments: Email TripId\n").split()
            url = f"http://server:5000/buy_ticket?e={arguments[0]}&&id={int(arguments[1])}"
            response = urllib.request.urlopen(url)
            trips = json.loads(response.read().decode())

            if (trips["ticket"] != None):
                print("Your ticket has been successfully bought.\n")
                [print(
                    f"TripId: {trip[0]} | TicketType: {trip[1]}")
                    for trip in trips['ticket']
                ]
            else:
                print("You cannot buy the ticket.\n")

        if "cancel" in command:
            arguments = input("Enter the arguments: Email TripId\n").split()
            url = f"http://server:5000/delete_from_cart?e={arguments[0]}&&id={int(arguments[1])}"
            response = urllib.request.urlopen(url)
            trips = json.loads(response.read().decode())

            if "reserved" in trips['ticket'][0]:
                print("No reserved ticket")
            elif "bought" in trips['ticket'][0]:
                print("The ticket has been already bought")
            else:
                print("Your ticket has been successfully canceled.\n")
                [print(
                    f"TripId: {trip[0]} | TicketType: {trip[1]}")
                    for trip in trips['ticket']
                ]


if __name__ == '__main__':
    main()
