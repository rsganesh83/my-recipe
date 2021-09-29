import sys
from random import randint


ticket_availability = {
    "1": {"class": "Sitting", "total": 10, "booked": 0},
    "2": {"class": "Sleeper", "total": 10, "booked": 0},
    "3": {"class": "Ac", "total": 10, "booked": 0}
}

booking_info = list()

passenger_info = dict()


def user_prompt():
    user_message = """ ----------------- \n Welcome To Train Ticket Booking Platform  \n 1. Ticket Booking \n 2. Cancel booking \n 3. Ticket Availability \n 4. Booking Info \n 0. Exit \n ----------------- \n Enter option : """
    option = input(user_message)

    if str(option) == '3':
        print('\n Ticket Availability ')
        show_availability()
    elif str(option) == '2':
        cancel_booking()
    elif str(option) == '1':
        book_tickets()
    elif str(option) == '4':
        print('\n Ticket Booking Records ')
        booking_records()
    elif str(option) == '0':
        sys.exit()
    else:
        print(' invalid entry ')

    redo_user_prompt()


def redo_user_prompt():
    ui = input('\n Enter 0 to exit 5 to start over: ')
    if str(ui) == '0':
        sys.exit()
    elif str(ui) == '5':
        user_prompt()
    else:
        print(' invalid entry ')
        redo_user_prompt()


def booking_records():
    print(" {:<10} {:<15} {:<10}".format('PNR', 'Class', 'Passenger Count'))
    for itm in booking_info:
        print(" {:<10} {:<15} {:<10}".format(itm['pnr'], itm['class'], itm['ticket_count']))


def cancel_booking():
    print("cancel booking----")


def book_tickets():
    user_class = input(" Choose Class \n 1. Sitting \n 2. Sleeper \n 3. AC \n : ")
    passenger_count = input(" Enter total number of passenger : ")
    class_info = ticket_availability.get(str(user_class))
    available_ticket = class_info['total']-class_info['booked']
    if int(passenger_count) > available_ticket:
        print(" Available ticket for {0} class is {1}".format(class_info['class'], str(available_ticket)))
        redo_user_prompt()
    else:
        p_info = []
        for itm in range(int(passenger_count)):
            p_name = input(" Enter passenger {} name : ".format(str(itm+1)))
            p_age = input(" Enter passenger {} age : ".format(str(itm + 1)))
            # load passenger info
            p_info.append({'name': p_name, 'age': p_age})

        # generate a random number for pnr
        pnr = str(randint(100000, 999999))

        # generate a booking info
        b_info = {"pnr": pnr, "class": class_info['class'], "ticket_count": int(passenger_count)}

        # save booking info
        booking_info.append(b_info)

        # save passenger info
        passenger_info[pnr] = p_info

        # update current availability
        ticket_availability[str(user_class)]['booked'] = class_info['booked'] + int(passenger_count)

        print(' Ticket booked successfully. Your pnr is {}'.format(pnr))
        redo_user_prompt()


def show_availability():
    print(" {:<15} {:<10}".format('Class', 'Available'))
    for k, v in ticket_availability.items():
        qty = v['total'] - v['booked']
        print(" {:<15} {:<10}".format(v['class'], qty))


if __name__ == "__main__":
    # execute only if run as a script
    user_prompt()
