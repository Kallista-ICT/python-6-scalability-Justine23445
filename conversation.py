import greeting

name = input("What's your name? ")
time = int(input(f"{name}, what time is it now? My clock is not working. (format hh) "))

# Decide which greeting to use
if 5 <= time < 12:
    message = greeting.good_morning(name)
elif 12 <= time < 17:
    message = greeting.good_afternoon(name)
elif 17 <= time < 21:
    message = greeting.good_evening(name)
else:
    message = greeting.hello(name)

print(message + " Thank you for your assistance. Appreciate it.")