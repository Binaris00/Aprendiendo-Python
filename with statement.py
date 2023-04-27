def create_and_write():
   with open("hola.txt", "x") as file:
      file.write("hola")
      file.close()
      
create_and_write()