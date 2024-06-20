txtFile = open("Text.txt" , "w")

txtFile.write("Hello")

txtFile.close()

txtFile = open("Text.txt" , "r")

print(txtFile.read())

txtFile.close()


txtFile = open("Text.txt" , "a")

txtFile.write("\nWorld!!!!!")

txtFile.close()

txtFile = open("Text.txt" , "r")

print(txtFile.read())

txtFile.close()


txtFile = open("Text.txt" , "w")

txtFile.write("OOOPPPPSSSS Hellow World overwritten")

txtFile.close()

txtFile = open("Text.txt" , "r")

print(txtFile.read())

txtFile.close()



