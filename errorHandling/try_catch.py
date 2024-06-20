try:

    for x in [4, 33, 56, -5, 78, 5]:
        try:
            if x%2 == 0 :  print("Even")

        except: 
            print("Invalid :)")

        else:
            print("Odd")

except:
    print("Ooops! something is wrong")

finally: 
            print("Done!!!!!!")

