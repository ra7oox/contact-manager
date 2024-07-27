#Ra7oox

list_contacts=[]

message="""
hello dear, do you want to add a new contact?
1-yes
2-no
"""
while True:
    contact={}
    
    user_response=int(input(message))
    if user_response==1:
        name=str(input("name:"))
        country=str(input("country:"))
        number=int(input("number:"))
        contact["name"]=name
        contact["country"]=country
        contact["number"]=number
        list_contacts.append(contact)
        print("contact added with success")
    elif user_response==2:
        print("thanks for using our app")
        break
    else:
        print("this choice didn't exist")
if len(list_contacts)>0:
    for i in list_contacts:
        print(f'name: {i["name"]} country: {i["country"]} number {i["number"]}')  
else:
    print("your list of contact is empty")     

        
    
    
    