username = input("Enter your username: ")

if len(username) > 12: 
    print("username must not be long than 12 characters")
elif not username.find(" ") == -1 : 
    print("username must not have any spaces")
elif not username.isalpha():
    print("username must have only alpbhabets")
else: 
    print(f"hello {username}!")