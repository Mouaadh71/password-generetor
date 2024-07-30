import random
while True :
     upper = "ABCDEFGHIGKLMNOPQRSTUVWXYZ"
     lower= upper.lower()
     num = "1234567890"
     sym = "!@#$%^&*()_+[]-=|"

     the_password_is_for = input("the password is for : ")

     up = int( input("do you want uppercase letter in your in your password length 1 if you want 0 if not : ") )
     if 1 < up :
          print ("invalid")
          break
     low = int( input("do you want lowercase in your password length 1 if you want 0 if not : ") )
     if 1 < low :
          print ("invalid")
          break

     numb = int( input("do you want numbers in your password length 1 if you want 0 if not : ") )
     if 1 < numb  :
          print ("invalid")
          break

     symb = int( input("do you want symbols in your password length  1 if you want 0 if not: ") )
     if 1 < symb :
          print ("invalid")
          break


     len = int( input("your password length : ") )

     all = ""
     if not 0 == up :
          all += upper
     if not  0== low :
          all += lower
     if not 0== numb  :
          all += num
     if not 0== symb :
          all += sym
     if 1 < up or low or numb or symb :
          print ("invalid")
          break

     password = ""

     length = len
     for i in range(length) :
          password  += "".join(random.choice(all))
     print(password)
     two =  the_password_is_for+ ":" + password + "\n"
     with open("passwords.txt","a") as p :
          p.seek(0)
          p .write(two)
