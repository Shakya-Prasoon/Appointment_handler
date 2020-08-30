# Prasoon Shakya
# Class - CS 301 (Data Structure And Algorithms)
# Assignment #2
# Date : 03/12/2020
# Creating a program for doctors office that allows to manage the schedule for the day

from linked_list import *


# finds the equivalent of short code
def check_code(cde):
    for x in range(12):
        if cde == code[x][0]:
            return x
    return -1


# Displays the list of all the speciality code
def display_code():
    print("\nList of Speciality code:")
    for j in range(12):
        print(code[j][0] + " --> " + code[j][1])
    print("\n")


# Finds the doctor that has the shortest waiting list
def find_short_wait():
    short = 2000000000000000000
    place = 0
    for z in range(20):
        if room[z][0] != "!":
            if room[z][2] == "!":
                return z
            if waiting_room[z].get_length() < short:
                short = waiting_room[z].get_length()
                place = z
    return place


# Find the equivalent short speciality code equivalent
def find_short(cde):
    for p in range(12):
        if cde == code[p][1]:
            return p
    return -1


# Finds the doctor of particular speciality with lowest waiting list
def find_lower(code_s, room_1):
    short = 2000000000000000000
    place = 0
    for c in range(20):
        if room_1[c][1] == code[check_code(code_s)][1]:
            if room_1[c][2] == "!":
                return c
            if waiting_room[c].get_length() < short:
                short = waiting_room[c].get_length()
                place = c
    return place


# Process to check out a doctor
def doctor_check_out(room_d, room_num_d, waiting_room_d, doc_count_d, waiting_age_d, waiting_indication_d, code_d,
                     file_d):
    print("Good Bye! Dr. " + room_d[room_num_d][0] + ", you have been Checked Out.")
    file_d.write("Good Bye! Dr. " + room_d[room_num_d][0] + ", you have been Checked Out.\n")
    print("Room #" + str(room_num_d + 1) + " is now available.")
    file_d.write("\tRoom #" + str(room_num_d + 1) + " is now available.\n")

    # Mark Doctor as empty
    room_d[room_num_d][0] = "!"
    # Check if doctor has people in the waiting list
    if waiting_room_d[room_num_d].get_length() > 0:
        # if there are people in the waiting list
        if doc_count_d <= 1:
            print("Sorry, there is no doctors currently available.\nAll the appointments that were "
                  "booked are being cancelled.")
            file_d.write("Sorry, there is no doctors currently available.\n\tAll the appointments that were "
                         "booked are being cancelled.\n")
            # Gets the number of people in the waiting list
            loop = waiting_room_d[room_num_d].get_length()
            # Clears the waiting list
            for i in range(loop):
                waiting_room_d[room_num_d].remove(1)

        # If there is no one in the waiting list
        else:
            loop = waiting_room_d[room_num_d].get_length()
            for i in range(loop):
                print("Customer '" + waiting_room_d[room_num_d].get(1) +
                      "' has now been moved into waiting list of Dr." + room_d[find_short_wait()][
                          0] + ".")
                file_d.write("Customer '" + waiting_room_d[room_num_d].get(1) +
                             "' has now been moved into waiting list of Dr." + room_d[find_short_wait()][
                                 0] + ".\n")
                # Transfer the info of a patient from one doctor list to another
                waiting_room_d[find_short_wait()].append(waiting_room_d[room_num_d].get(1))
                waiting_age_d[find_short_wait()].append(waiting_age_d[room_num_d].get(1))
                waiting_indication_d[find_short_wait()].append(waiting_indication_d[room_num_d].get(1))
                waiting_room_d[room_num_d].remove(1)
                waiting_age_d[room_num_d].remove(1)
                waiting_indication_d[room_num_d].remove(1)
    # Marks the room as empty
    doc_count_d -= 1
    code_d[find_short(room_d[room_num_d][1])][2] -= 1
    room_d[room_num_d][1] = "!"
    room_d[room_num_d][2] = "!"
    room_d[room_num_d][3] = "!"
    room_d[room_num_d][4] = "!"


# Process to check in a customer
def customer_fill_up(room_c, location_c, name_c, age_c, emergency_c, waiting_r, waiting_a, waiting_ind, file):
    # Checks if the doctor already have a customer
    if room_c[location_c][2] == "!":
        room_c[location_c][2] = name_c
        room_c[location_c][3] = age_c
        if emergency_c == 'Y' or emergency_c == 'y':
            room_c[location_c][4] = "Emergency Case"
        else:
            room_c[location_c][4] = "Not an Emergency"
        print("'" + name_c + "', age: " + str(room_c[location_c][3]) + " will be EXAMINED by Dr. " +
              room_c[location_c][0] + " (" + room_c[location_c][1] + ") at room #" + str(location_c + 1) + " - (" +
              room_c[location_c][4] + ").")
        file.write("'" + name_c + "', age: " + str(room_c[location_c][3]) + " will be EXAMINED by Dr. " +
                   room_c[location_c][0] + " (" + room_c[location_c][1] + ") at room #" + str(location_c + 1) + " - (" +
                   room_c[location_c][4] + ").\n")
    # If no one is being examined by doctor then do this --> wait list
    else:
        waiting_r[location_c].append(name_c)
        waiting_a[location_c].append(age_c)
        if emergency_c == 'Y' or emergency_c == 'y':
            waiting_ind[location_c].append("Emergency Case")
        else:
            waiting_ind[location_c].append("Not an Emergency")
        print("Sorry! '" + name_c + "' has been WAIT LISTED for Dr. " + room_c[location_c][0] + " at room #" +
              str(location_c + 1) + ".")
        file.write("Sorry! '" + name_c + "' has been WAIT LISTED for Dr. " + room_c[location_c][0] + " at room #" +
                   str(location_c + 1) + ".\n")


# Opens a file name "trans_out.txt"
trans_out = open("trans_out.txt", "a")
# Creates list of needed variables, objects and classes
waiting_room = [linked_list() for _ in range(20)]
waiting_indication = [linked_list() for _ in range(20)]
waiting_age = [linked_list() for _ in range(20)]
room = [["!"] * 5 for _ in range(20)]
code = [["PED", "Pediatrics", 0], ["GEN", "General practice", 0], ["INT", "Internal medicine", 0],
        ["CAR", "Cardiology", 0], ["SUR", "Surgeon", 0], ["OBS", "Obstetrics", 0], ["PSY", "Psychiatry", 0],
        ["NEU", "Neurology", 0], ["ORT", "Orthopedic", 0], ["DET", "Dermatology", 0], ["OPT", "Ophthalmology", 0],
        ["ENT", "Ear, Nose, and Throat", 0]]
doc_count = 0

# Prompt
inp = input("\nEnter D / P:\n\t 'D' for Doctor \n\t 'P' for Patient\n:")
while inp != 'D' and inp != 'd' and inp != 'P' and inp != 'p':
    inp = input("\nEnter D / P:\n\t 'D' for Doctor \n\t 'P' for Patient\n:")

# main loop for the whole program
while inp == 'D' or inp == 'P' or inp == 'd' or inp == 'p':
    # Loop for Doctors
    if inp == 'D' or inp == 'd':
        inp = input("\nEnter I / O:\n\t'I' for Check In\n\t'O' for Check Out\n:")
        while inp != 'I' and inp != 'o' and inp != 'i' and inp != 'O':
            inp = input("\nEnter I / O:\n\t'I' for Check In\n\t'O' for Check Out\n:")

        # Doctor Check In
        if inp == 'i' or inp == 'I':
            name = input("Name :")
            room_num = input("Room #(1-20) :")
            # Checks if the input number is digit or not
            while not room_num.isdigit():
                room_num = input("Room #(1-20) :")
            room_num = int(room_num)
            room_num -= 1
            display_code()
            speciality = input("Speciality Code :")
            # Checks if the entered speciality code is valid or not
            while check_code(speciality) == -1:
                speciality = input("Speciality Code :")
            # Checks if there is already another doctor in that room
            if room[room_num][0] == "!":
                room[room_num][0] = name
                room[room_num][1] = code[check_code(speciality)][1]
                code[check_code(speciality)][2] += 1
                doc_count += 1
                print("Dr. " + room[room_num][0] + "(" + room[room_num][1] + ") has been checked into the room #" +
                      str(room_num + 1) + ".")
                trans_out.write("Dr. " + room[room_num][0] + "(" + room[room_num][1] +
                                ") has been checked into the room #" + str(room_num + 1) + ".\n")
            # if there is already some other doctor in the room, give the error message
            else:
                print("Sorry! The room is being used by Dr. " + room[room_num][0] + ".\nPlease try again later.")
                trans_out.write("Sorry! The room is being used by Dr. " + room[room_num][0] +
                                ".\n\tPlease try again later.\n")
        # Doctor Check Out
        else:
            name = input("Name :")
            room_num = input("Room #(1-20) :")
            # Checks if the input is digit or not
            while not room_num.isdigit():
                room_num = input("Room #(1-20) :")
            room_num = int(room_num)
            room_num -= 1

            # Checks if that doctor is available in that room or not
            if name != room[room_num][0]:
                print("Sorry! Dr. " + name + " is not available in that room.")
            # If so then do this
            else:
                if room[room_num][2] != "!":
                    print("Sorry! There is currently a patient waiting in the doctor's office. Please complete "
                          "checking out the current customer before checking-out.")
                else:
                    doctor_check_out(room, room_num, waiting_room, doc_count, waiting_age, waiting_indication, code,
                                     trans_out)
    # Loop for Customer
    else:
        # Asks user for whether they are here for input or output
        inp = input("\nEnter I / O:\n\t'I' for Check In\n\t'O' for Check Out\n:")
        while inp != 'I' and inp != 'o' and inp != 'i' and inp != 'O':
            inp = input("\nEnter I / O:\n\t'I' for Check In\n\t'O' for Check Out\n:")
        # Patient Check In
        if inp == 'i' or inp == 'I':
            if doc_count > 0:
                name = input("Name : ")
                age = input("Age : ")
                # Checks if the entered input is a number or not
                while not age.isdigit():
                    age = input("Age : ")
                age = int(age)
                # Patients Under 16
                if age < 16:
                    speciality = "PED"
                    emergency = input("Is it an emergency?\n\t'Y' for Yes\n\t'N' for No\n:")
                    while emergency != 'Y' and emergency != 'y' and emergency != 'n' and emergency != 'N':
                        emergency = input("Is it an emergency?\n\t'Y' for Yes\n\t'N' for No\n:")
                    # Checking if the specific doctor is available
                    if code[check_code(speciality)][2] > 0:
                        location = find_lower(speciality, room)
                        # Checking if doctor is currently seeing anyone
                        customer_fill_up(room, location, name, age, emergency, waiting_room, waiting_age,
                                         waiting_indication, trans_out)
                    # If no specific doctor found look for General Practice
                    elif code[check_code("GEN")][2] > 0:
                        location = find_lower("GEN", room)
                        # Checking if doctor is currently seeing anyone
                        customer_fill_up(room, location, name, age, emergency, waiting_room, waiting_age,
                                         waiting_indication, trans_out)
                    # If no General Practice and Pediatrician
                    else:
                        location = find_short_wait()
                        # Checking if doctor is currently seeing anyone
                        customer_fill_up(room, location, name, age, emergency, waiting_room, waiting_age,
                                         waiting_indication, trans_out)
                # Patients 16 and over
                else:
                    speciality = input("Speciality Code :")
                    while check_code(speciality) == -1:
                        speciality = input("Speciality Code :")
                    emergency = input("Is it an emergency?\n\t'Y' for Yes\n\t'N' for No\n:")
                    while emergency != 'Y' and emergency != 'y' and emergency != 'n' and emergency != 'N':
                        emergency = input("Is it an emergency?\n\t'Y' for Yes\n\t'N' for No\n:")
                    # Checking if the specific doctor is available
                    if code[check_code(speciality)][2] > 0:
                        location = find_lower(speciality, room)
                        # Checking if doctor is currently seeing anyone
                        customer_fill_up(room, location, name, age, emergency, waiting_room, waiting_age,
                                         waiting_indication, trans_out)
                    # If no specific doctor found look for General Practice
                    elif code[check_code("GEN")][2] > 0:
                        location = find_lower("GEN", room)
                        # Checking if doctor is currently seeing anyone
                        customer_fill_up(room, location, name, age, emergency, waiting_room, waiting_age,
                                         waiting_indication, trans_out)
                    # If no General Practice and Pediatrician
                    else:
                        location = find_short_wait()
                        # Checking if doctor is currently seeing anyone
                        customer_fill_up(room, location, name, age, emergency, waiting_room, waiting_age,
                                         waiting_indication, trans_out)
            else:
                print("Sorry! There are no doctors that are currently available in the facility.")
                trans_out.write("Sorry! There are no doctors that are currently available in the facility.\n")
        # Patient Check Out
        else:
            name = input("Name :")
            room_num = input("Room #(1-20) :")
            while not room_num.isdigit():
                room_num = input("Room #(1-20) :")
            room_num = int(room_num)
            room_num -= 1
            if name != room[room_num][2]:
                print("Sorry! Patient '" + name + "' was not available in that room.")
            else:
                room[room_num][2] = "!"
                room[room_num][3] = "!"
                room[room_num][4] = "!"
                print("Good Bye! " + name + ". You have been checked out.")
                trans_out.write("Good Bye! " + name + ". You have been checked out.\n")

                doc_cont = input("Is doctor still checking in patients?\nEnter :-\n\t'Y' for yes\n\t'N' for No\n:")
                while doc_cont != 'Y' and doc_cont != 'y' and doc_cont != 'n' and doc_cont != 'N':
                    doc_cont = input("Enter :-\n\t'Y' for yes\n\t'N' for No\n:")

                # If doctor still wants to check in patients
                if doc_cont == 'Y' or doc_cont == 'y':
                    # Check if there is someone on the wait list
                    if waiting_room[room_num].get_length() > 0:
                        room[room_num][2] = waiting_room[room_num].get(1)
                        room[room_num][3] = waiting_age[room_num].get(1)
                        room[room_num][4] = waiting_indication[room_num].get(1)
                        waiting_room[room_num].remove(1)
                        waiting_age[room_num].remove(1)
                        waiting_indication[room_num].remove(1)
                        print("'" + room[room_num][2] + "', age " + str(room[room_num][3]) +
                              " will now be examined by Dr. " + room[room_num][0] + " at room #" + str(room_num + 1) +
                              " - (" + room[room_num][4] + ").")
                        trans_out.write("'" + room[room_num][2] + "', age " + str(room[room_num][3]) +
                                        " will now be examined by Dr. " + room[room_num][0] + " at room #" +
                                        str(room_num + 1) + " - (" + room[room_num][4] + ").\n")
                # If doctor wants to check out
                else:
                    doctor_check_out(room, room_num, waiting_room, doc_count, waiting_age, waiting_indication, code,
                                     trans_out)

    # End of loop... ask the user for next instruction
    inp = input("\nEnter D / P:\n\t 'D' for Doctor \n\t 'P' for Patient\n\t 'Q' to Quit\n:")
    while inp != 'D' and inp != 'd' and inp != 'P' and inp != 'p' and inp != 'q' and inp != 'Q':
        inp = input("\nEnter D / P:\n\t 'D' for Doctor \n\t 'P' for Patient\n\t 'Q' to Quit\n:")
    if inp == 'q' or inp == 'Q':
        break
trans_out.close()
