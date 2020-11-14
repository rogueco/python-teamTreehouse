# coding=utf-8
import math


def split_check(total, number_of_people_to_calculate):
    if number_of_people <= 1:
        raise ValueError("More than 1 person is required to split the check")
    return math.ceil(total / number_of_people_to_calculate)


try:
    total_due = float(input("what is the total?  "))
    number_of_people = int(input("How many people?  "))
    amount_due = split_check(total_due, number_of_people)
except ValueError as error:
    print("Oh no! That's not a valid value. Try again...")
    print("Error: ({})".format(error))
else:
    print("Each person owes £{}".format(amount_due))
