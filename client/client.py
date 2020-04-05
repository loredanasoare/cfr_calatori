import json
import urllib.request


def main():
    while True:
        command = input("Enter a command: ")
        arguments = input("Enter the arguments: ").split()

        if "sign_in" in command:
            url = "http://server:5000/sign_in?fN={arguments[0]}&lN={arguments[1]}&e={arguments[2]}&t={arguments[3]}&p={arguments[4]}"
            oUrl = urllib.request.urlopen(url)
            oUrl.read().decode()
            print("Success")

        if "log_in" in command:
            url = "http://server:5000/log_in?e={arguments[0]}&p={arguments[1]}"
            oUrl = urllib.request.urlopen(url)
            oUrl.read().decode()

            print("Success")

        if "search" in command:
            url = f"http://server:5000/get_trip?src={arguments[0]}&dest={arguments[1]}&day={arguments[2]}"
            oUrl = urllib.request.urlopen(url)
            trips = json.loads(oUrl.read().decode())

            if trips['res'] is None:
                print("There are no available seats")
            else:
                [print(f"Source: {trip[0]} | Destination: {trip[1]} | Day: {trip[2]} | LeaveHour: {trip[3]} | ArriveHour: {trip[4]} | AvailableSeats: {trip[5]}")
                        for trip in trips['res']]
            
        if "buy" in command:
            url = f"http://server:5000/buy_ticket?id={arguments[0]}"
            oUrl = urllib.request.urlopen(url)
            trips = json.loads(oUrl.read().decode())

            print(trips['res'])
            print("Your ticket has been bought")


        if "cancel" in command:
            url = "http://server:5000/cancel_ticket?id={arguments[0]}"
            oUrl = urllib.request.urlopen(url)
            trips = json.loads(oUrl.read().decode())

            print(trips['res'])
            print("You has canceled the ticket")


if __name__ == '__main__':
    main()
