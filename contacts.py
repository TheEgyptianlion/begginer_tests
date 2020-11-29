#Making a simple text-based contact list, use Classes for Contacts
#Assume no Identical Full Names
import json
class Contact:
    def __init__(self,name,phone,notes):
        self.name = name
        self.phone = phone
        self.notes = notes
    def details(self):
        print(f'Contact Details:\nName: {self.name}\nPhone: {self.phone}\nNotes: {self.notes}')
def searchcontact(name):
    with open("contactinfo", "r+") as file:
        data = json.loads(file.read())
        for person in data["contacts"]:
            if person["name"].lower() == name.lower():
                return True
        return False
    file.close()
def contactlist():
    print("----------\nContacts:\n----------")
    with open("contactinfo", "r") as file:
        data = json.loads(file.read())
        for person in data["contacts"]:
            globals()[person["name"].lower()] = Contact(person["name"],person["phone"],person["notes"])
            print(person["name"])
    file.close()

def savechange(type,name,phone='',notes=''):
    with open("contactinfo","r") as file:
        data = json.loads(file.read())
        print(data)
        if type == 'add':
            data["contacts"].append({"name":name,"phone":phone,"notes":notes})
        elif type == "delete":
            for contact in data["contacts"]:
                if contact["name"].lower() == name.lower():
                    data["contacts"].remove(contact)
        elif type == "edit":
            point = input("What would you like to edit on the user (name,phone,notes) ")
            if point.lower() in ["name","phone","notes"]:
                for contact in data["contacts"]:
                    if contact["name"].lower() == name.lower():
                        print("Current:"+contact[point])
                        data["contacts"][data["contacts"].index(contact)][point] = input(f"Input new {point}: ")
            else:
                print("Invalid Option")
                return "invalid"
    file.close()
    with open("contactinfo", "w") as file:
        file.write(json.dumps(data,indent = 2))
    file.close()
def add():
    name = input("\nFull Name of the Contact: ")
    phone = input(f"What is {name}'s phone number ")
    notes = input("Notes: ")
    if searchcontact(name):
        print("User already found, try editing instead.")
    else:
        savechange("add",name,phone,notes,)
    return "menu"

def delete():
    contactlist()
    contact = input("\nWhich name would you like to delete: (ENTER if you would like to cancel) ")
    if contact == "":
        return "menu"
    else:
        if searchcontact(contact):
            var = globals()[contact.lower()]
            savechange("delete",var.name,var.phone,var.notes,)
            del var
            print("Contact Deleted")
        else:
            print("Contact not found")
    return "menu"
def view():
    contactlist()
    contact = input("\nWhich name would you like to view: (ENTER if you would like to cancel) ")
    if contact == "":
        return "menu"
    elif searchcontact(contact):
        var = globals()[contact.lower()]
        var.details()
    else:
        print("Contact is not in the list.")
        return "view"
    return 'menu'
def edit():
    contactlist()
    contact = input("\nWhich user would you like to edit: (ENTER if you would like to cancel) ")
    if contact == "":
        return "menu"
    elif searchcontact(contact):
        if savechange("edit",contact) == "invalid":
            return "edit"
    else:
        print("Contact is not in the list.")
        return "edit"
    return 'menu'
#main loop
command = 'menu'
while True:
    if command == 'menu':
        command = input("What would you like to do (add/delete/view/edit) ")
    elif command =='add':
        command = add()
    elif command == "delete":
        command = delete()
    elif command == "view":
        command = view()
    elif command == "edit":
        command = edit()