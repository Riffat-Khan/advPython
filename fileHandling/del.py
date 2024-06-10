import os 

# os.remove("Text.txt")

try:
    os.remove("Text.txt")

except: 
    print("Error : File does not exsit")

    

#remove folder

os.rmdir("foldername")