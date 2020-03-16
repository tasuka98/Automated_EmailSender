#!/usr/bin/python3

import csv
import ezgmail
import os
import time
import sys
from pathlib import Path


def evaluate(choice):
    if choice == 'Y' or choice == 'y' or choice == '':
        return True
    else:
        return False


def main():
    correct_content = False
    correct_attachment = False
    attachment = []
    client_list = open("../client_list.csv")
    dict_reader = csv.DictReader(client_list)

    os.chdir("../content")

    while not correct_content:
        filename = input("Please select the content file that you wish to send: ")
        try:
            fd = open(filename, "r")
            correct_content = True
        except:
            print("file does not exist please try again")
            correct_content = False

    os.chdir("../attachments")

    total_size = 0

    while not correct_attachment:
        usr_input = input("Please select the attachment files that you wish to send: ")
        filename = "../attachments/" + usr_input

        if usr_input == '':
            correct_attachment = True

        else:
            try:
                print("file selected is", Path(filename).stat())
                total_size = total_size + Path(filename).stat().st_size;
                if total_size > 20480000:
                    print("File size exceeds 20mb, please choose another file")
                    correct_attachment = False
                else:
                    attachment.append(filename)
                    correct_attachment = True
            except:
                print("File does not exist!, please choose another attachment!")

        choice = input("Is there another attachment that you want to select?(Y/n): ")
        if evaluate(choice):
            correct_attachment = False
        else:
            correct_attachment = True

    os.chdir("../credentials")

    print("Loading account info please wait.....")
    try:
        ezgmail.init()
    except:
        print("Unable to initialize account, please check your credentials.json")
        exit(-1)

    print("Account is loaded!")

    title = input("Please type in the title of email: ")
    data = fd.read()

    for row in dict_reader:
        if not len(attachment):
            ezgmail.send(row["Email"], title, data)
        else:
            ezgmail.send(row["Email"], title, data, attachment)
        print("Email to", row["ClientName"], "sent!")

    usr_input = input("ALl email sent, do you want to send another one?(Y/n): ")

    if evaluate(usr_input):
        main()
    else:
        print("exiting script now, have a nice day :)")

    fd.close()

if __name__ == "__main__":
    main()
