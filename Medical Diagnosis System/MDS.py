userFever = input("Do you have a fever (y/n): ")


userRash = input("Do you have a rash (y/n): ")

userEar = input("Does your ear hurt (y/n): ")


userNose = input("Do you have a stuffy nose (y/n): ")




if userFever == 'n' and userNose == 'n':
    print("Diagnosis: You are Hypchondriac")
elif userFever == 'n' and userNose == 'y':
    print("Diagnosis: You have a Head Cold")
elif userFever == 'y' and userRash == 'n' and userEar == 'y':
    print("Diagnosis: You have an ear infection")
elif userFever == 'y' and userRash == 'n' and userEar == 'n':
    print("Diagnosis: You have the flu")
elif userFever == 'y' and userRash == 'y':
    print("Diagnosis: You have the measles")
