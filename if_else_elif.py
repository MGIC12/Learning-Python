#Using if-else
rains = True
temperature = 12
print(f"Rains: {rains}")
print(f"Temperature: {temperature}°C")
if rains == True and temperature < 20:
    print("I'll use an umbrella and a coat")
else:
    print("I don't need an umbrella or a coat")

print("Now I'm going outside")

print("------------------------------------------")

#Using if
puddle = True
print(f"Puddle: {puddle}")
print("Let's start walking")
if puddle == True:
    print("Let's jump on it!")

print("I keep walking")

print("------------------------------------------")

#Using if-else in a better way
rains = True
print(f"Rains: {rains}")
temperature = int(input("Temperature: "))
if temperature < 18:
    if rains == True:
        print("I'll use an umbrella and a coat")
    else:
        print("I'll only use a coat")
else:
    print("I don't need an umbrella or a coat")

print("------------------------------------------")

#Using if-elif-else
rains = False
print(f"Rains: {rains}")
temperature = int(input("Temperature: "))
if temperature < 18 and rains == True:
    print("I'll use an umbrella and a coat")
elif temperature < 18 and rains == False:
    print("I'll only use a coat")
else:
    print("I won't use an umbrella or a coat")