class Email:
        question = input("do you have account? ")


        if question== "no":
                name=input("Enter your name: ")
                address=input("Enter your address: ")
                age=input("Enter you age:")
                password=input("Enter your password:")
                confirmPassword=input("confirm your password:")
                print(f"Hello{name} you have a successfully created account")

        elif question == "yes":
            name=input("Enter your name:")
            password=input("Enter your password:")
            print(f"Hello,{name} welcome back")

        
        email=input("Enter your Email:").strip()
        username=email[:email.index("@")]
        domain_name=email[email.index("@")+1:]
        print(f"Your username is {username} and domain_name is {domain_name}")


My_email=Email()
