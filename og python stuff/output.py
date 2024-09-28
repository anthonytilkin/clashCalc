type_input = input("Enter the name or HP of the cog: ")


# Initializing employeeHP
employeeHP = 0

try:
    type_input = int(type_input)
    employeeHP = type_input
except ValueError:
    # If it's not an integer, treat it as a cog name
    level = int(input("What level is the cog? "))
    employeeHP = (level + 1) * (level + 2) 
    

#gag = input(str("What gag track(s) are you trying to use?"))
#if gag == "Sound":
#    from sound.soundGags import kazoo, horn, whistle, bugle, aoogah, trunk, fog, opera
#else:
#    pass #Temporary add other tracks later

print(employeeHP)
