Adjective1 = input("enter the first adjective: ")
Adjective2 = input("enter the second adjective: ")
Adjective3 = input("enter the third adjective: ")
Adjective4 = input("enter thr fourth adjective: ")
 
if Adjective1 and Adjective2 and Adjective3 and Adjective4:
     story = f"""On a beautiful {Adjective1} day, I went to the zoo. I saw a funny {Adjective2} monkey swinging
            from the trees. Then, I spotted a majestic {Adjective3} lion lounging in the sun.  What a wild 
            and {Adjective4} experience! """
     print("\nYour story:")
     print(story)
else:
    print("not applicable, please try again")

   