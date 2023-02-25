from database import telephone
def add_items():
    code=int(input("\nEnter phone number : "))
    if code not in telephone.keys():
        name=input("Enter new name : ")
        gender=input("Enter gender of person : ")
        age=int(input("Enter age of person  : "))        
        telephone.update({code:[name,gender,age]})
    else:
        print("Number already exists")
