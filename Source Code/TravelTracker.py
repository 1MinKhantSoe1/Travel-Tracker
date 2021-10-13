"""
Name: Min Khant Soe
Date started:
GitHub URL:
"""

from operator import itemgetter


def main():
    """Main Function"""

    print("Travel Tracker 1.0 - by <Min Khant Soe>")
    print("3 places loaded from places.csv")

    temp_data = []

    read_file = open("places.csv", "r")  # read csv file
    new_data = add_places_into_new_array(read_file)
    read_file.close()

    for data in new_data:  # add read file data to temp memory list

        temp_data.append(data)

    display_menu()
    user = input(">>> ")

    while user == "":  # user input is empty

        print("Input can not be blank")

        user = input(">>> ")

    while user != "":

        if user.upper() == "L":

            display_places(temp_data)
            display_menu()
            user = input(">>> ")

        elif user.upper() == "A":

            add_new_place(temp_data)
            display_menu()
            user = input(">>> ")

        elif user.upper() == "M":

            place_visited(temp_data)
            display_menu()
            user = input(">>> ")

        elif user.upper() == "Q":

            save_and_quit(temp_data)
            break
        else:

            print("Invalid menu choice")
            display_menu()
            user = input(">>> ")

    return user


def display_menu():
    """Display Menu"""

    print("\nMenu")
    print("L - List places")
    print("A - Add new place")
    print("M - Mark a place as visited")
    print("Q - Quit")


def add_places_into_new_array(read_file):
    """List of places"""

    new_data = []

    for line in read_file:
        line = line.strip()  # Remove \n
        parts = line.split(',')  # Separate data
        parts[2] = int(parts[2])  # Convert integer
        new_data.append(parts)

    return new_data


def display_places(temp_data):
    """Show all the list of places"""

    place_count = 0

    temp_data.sort(key=itemgetter(3, 2))  # sorted by unvisited place

    for i, data in enumerate(temp_data):

        if data[3] == "n":
            place_count += 1

        i += 1

        print(data[3].replace("n", "*").replace("v", " "), "{0}. {1:15} in {2:15} priority {3:5}".format(i, *data))

    if place_count == 0:  # there is no unvisited place

        print(len(temp_data), "Places, No places left to visit. Why not add a new place?")

    else:

        print(len(temp_data), "Places, You still want to visit", place_count, "places.")


def add_new_place(temp_data):
    """add new unvisited place"""

    place_name = input("Name: ")

    while place_name == "":  # name is empty

        print("Input can not be blank")

        place_name = input("Name: ")

    while place_name != "":  # name is not empty

        country = input("Country: ")

        while country == "":  # country is empty

            print("Input can not be blank")

            country = input("Country: ")

        while country != "":  # country is not empty

            try:

                priority = int(input("Priority: "))

                if priority < 0:  # priority is less than 0

                    print("Number must be > 0")
                    priority = int(input("Priority: "))

                unvisited = "n"  # sign for unvisited
                print(place_name, "in", country, "(Priority", priority, ")", "added to Travel Tracker")
                new_place = [str(place_name), str(country), int(priority), str(unvisited)]
                temp_data.insert(0, new_place)  # insert into first place

                return new_place

            except ValueError:

                print("Invalid input; enter a valid number")

        return country

    return place_name


def place_visited(temp_data):
    """Mark unvisited place to visited"""

    count = 0

    for unvisited in temp_data:  # counting unvisited place

        if unvisited[3] == "n":
            count += 1

    if count != 0:

        while True:

            display_places(temp_data)

            try:

                mark_place = int(input("Enter the number of a place to mark as visited \n>>>"))

                while mark_place <= 0:
                    print("Place number must be greater than 0")

                    mark_place = int(input("Enter the number of a place to mark as visited \n>>>"))

                while mark_place > len(temp_data):
                    print("No place number found !")

                    mark_place = int(input("Enter the number of a place to mark as visited \n>>>"))

                while len(temp_data) >= mark_place > 0:

                    for i, data in enumerate(temp_data):

                        i += 1

                        if i == mark_place:

                            if data[3] == "n":

                                data[3] = "v"
                                print(data[0], "in", data[1], "is visited")

                            else:

                                print("Place is already visited")

                            return temp_data

                return mark_place

            except ValueError:

                print("\nPlease, Enter place number only !!\n")
    else:

        print("No unvisited places")


def save_and_quit(temp_data):
    """Save all the places into csv file and stop the program"""

    output_file = open("places.csv", "w", newline="")

    for data in temp_data:
        data[2] = str(data[2])  # Convert into string
        write = ','.join(data)
        print(write, file=output_file)  # write data into csv

    output_file.close()

    print(len(temp_data), "places saved to places.csv")
    print("Have a nice day : )")


if __name__ == '__main__':
    main()

    print("")

    print("Created By Min Khant Soe (HakHak)")

    input("")
