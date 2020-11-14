# coding=utf-8
TICKET_PRICE = 10

tickets_remaining = 100

# Output how many tickets are remaining using the tickets_remaining variable

print("There are {} tickets remaining".format(tickets_remaining))

# Gather the users name and assign it to a new variable

name = input("What is your name?  ")

# Prompt the user by name and ask how many ticket they would like?

number_of_tickets_wanted = input("How many tickets would you like {}?  ".format(name))
number_of_tickets_wanted = int(number_of_tickets_wanted)

# Calculate the price (number of tickets multiplied by the price) and assign it to a variable
print("The total cost of the tickets will be £{}".format(number_of_tickets_wanted * TICKET_PRICE))

# Output the price to the screen
