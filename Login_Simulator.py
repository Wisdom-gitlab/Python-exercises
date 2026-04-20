def login ():
     saved={"name":"Wisdom","password":"Wisdom01"}
     
     name=input("enter your username :")
     password=input("enter your password :")

     if name ==saved["name"] and password==saved["password"]:
          print (f"  Hello {saved['name']} \n Your login has been successful!")
     else:
          print("Wrong username or password")


login()
          