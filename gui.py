#!/usr/bin/python3

import tkinter as tk # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
from tkinter import messagebox
from RolesFunc import *
from dataBase import *
from rbac import *

currentLogin = None
currentRole = None
#GUI

def login():
    for widget in frame.winfo_children():
        widget.destroy()

    emailLabel = tk.Label(frame, text="Enter email")
    emailField = tk.Entry(frame, bd=5)
    emailLabel.pack()
    emailField.pack()

    passwordLabel=tk.Label(frame, text="Enter password")
    passwordField = tk.Entry(frame, bd=5, show="*")
    passwordLabel.pack()
    passwordField.pack()

    slogan = tk.Button(frame, text='Log me', command=lambda: logging(emailField.get(), passwordField.get()))
    slogan.pack()

    registerButton = tk.Button(frame,
                       text="Register me",
                       command=register)
    registerButton.pack()


def chooseRole():
    for widget in frame.winfo_children():
        widget.destroy()

    roleLabel = tk.Label(frame, text="Choose role")
    roleLabel.pack()

    rolesList = tk.Listbox(frame)
    x = 0
    for role in rbac.get_user_roles(currentLogin):
        rolesList.insert(x, role)
        x+=1
    rolesList.pack()

    slogan = tk.Button(frame, text='Confirm choosed role', command=lambda: assignChoosedRole(rolesList.get(rolesList.curselection())))
    slogan.pack()

    slogan = tk.Button(frame, text='Log out',
                       command=lambda: login())
    slogan.pack()

def assignChoosedRole(choosedRole):
    global currentRole
    currentRole = choosedRole
    loggedMenu(currentRole)


def register():
    for widget in frame.winfo_children():
        widget.destroy()

    emailLabel = tk.Label(frame, text="Enter email")
    emailField = tk.Entry(frame, bd=5)
    emailLabel.pack()
    emailField.pack()

    passwordLabel = tk.Label(frame, text="Enter password")
    passwordField = tk.Entry(frame, show="*", bd=5)
    passwordLabel.pack()
    passwordField.pack()

    passwordAgainLabel = tk.Label(frame, text="Enter password again")
    passwordAgainField = tk.Entry(frame, show="*", bd=5)
    passwordAgainLabel.pack()
    passwordAgainField.pack()

    nameLabel = tk.Label(frame, text="Enter name")
    nameField = tk.Entry(frame, bd=5)
    nameLabel.pack()
    nameField.pack()

    surnameLabel = tk.Label(frame, text="Enter surname")
    surnameField = tk.Entry(frame, bd=5)
    surnameLabel.pack()
    surnameField.pack()

    ageLabel = tk.Label(frame, text="Enter age")
    ageField = tk.Entry(frame, bd=5)
    ageLabel.pack()
    ageField.pack()

    sexLabel = tk.Label(frame, text="Enter sex")
    sexField = tk.Entry(frame, bd=5)
    sexLabel.pack()
    sexField.pack()

    pinLabel = tk.Label(frame, text="Enter PIN")
    pinField = tk.Entry(frame, bd=5)
    pinLabel.pack()
    pinField.pack()

    slogan = tk.Button(frame, text='Register me',
                       command=lambda: registering(emailField.get(), passwordField.get(), passwordAgainField.get(),
                                                   nameField.get(), surnameField.get(), ageField.get(), sexField.get(),
                                                   pinField.get()))
    slogan.pack()

def loggedMenu(role):
    for widget in frame.winfo_children():
        widget.destroy()

# Client operations
    if(role == "clientCreator"):
        slogan = tk.Button(frame, text='Insert new client',
                           command=lambda: clientMenu("New"))
        slogan.pack()
    if (role == "clientEditor"):
        slogan = tk.Button(frame, text='Update client',
                           command=lambda: clientMenu("Update"))
        slogan.pack()
    if (role == "clientSelector"):
        slogan = tk.Button(frame, text='Select client',
                           command=lambda: clientMenu("Select"))
        slogan.pack()
    if (role == "clientDeleter"):
        slogan = tk.Button(frame, text='Delete client',
                           command=lambda: clientMenu("Delete"))
        slogan.pack()

# Gym operations
    if (role == "gymCreator"):
        slogan = tk.Button(frame, text='Insert new gym',
                           command=lambda: gymMenu("New"))
        slogan.pack()
    if (role == "gymEditor"):
        slogan = tk.Button(frame, text='Update gym info',
                           command=lambda: gymMenu("Update"))
        slogan.pack()
    if (role == "gymSelector"):
        slogan = tk.Button(frame, text='Show gym info',
                           command=lambda: gymMenu("Select"))
        slogan.pack()
    if (role == "gymDeleter"):
        slogan = tk.Button(frame, text='Delete gym',
                           command=lambda: gymMenu("Delete"))
        slogan.pack()

# Coach operations
    if (role == "coachCreator"):
        slogan = tk.Button(frame, text='Insert new coach',
                           command=lambda: coachMenu("New"))
        slogan.pack()
    if (role == "coachEditor"):
        slogan = tk.Button(frame, text='Update coach info',
                           command=lambda: coachMenu("Update"))
        slogan.pack()
    if (role == "coachSelector"):
        slogan = tk.Button(frame, text='Show coach info',
                           command=lambda: coachMenu("Select"))
        slogan.pack()
    if (role == "coachDeleter"):
        slogan = tk.Button(frame, text='Delete coach',
                           command=lambda: coachMenu("Delete"))
        slogan.pack()

# Term operations
    if (role == "termCreator"):
        slogan = tk.Button(frame, text='Insert new term',
                           command=lambda: termMenu("New"))
        slogan.pack()
    if (role == "termEditor"):
        slogan = tk.Button(frame, text='Update term info',
                           command=lambda: termMenu("Update"))
        slogan.pack()
    if (role == "termSelector"):
        slogan = tk.Button(frame, text='Show term info',
                           command=lambda: termMenu("Select"))
        slogan.pack()
    if (role == "termDeleter"):
        slogan = tk.Button(frame, text='Delete term',
                           command=lambda: termMenu("Delete"))
        slogan.pack()

# Group class operations
    if (role == "groupClassCreator"):
        slogan = tk.Button(frame, text='Insert new group class',
                           command=lambda: groupClassMenu("New"))
        slogan.pack()
        slogan = tk.Button(frame, text='Assign group class to gym',
                           command=lambda: groupClassMenu("assignGym"))
        slogan.pack()
        slogan = tk.Button(frame, text='Assign coach to group class',
                           command=lambda: groupClassMenu("assignCoach"))
        slogan.pack()
    if (role == "groupClassEditor"):
        slogan = tk.Button(frame, text='Update group class',
                           command=lambda: groupClassMenu("Update"))
        slogan.pack()
    if (role == "groupClassSelector"):
        slogan = tk.Button(frame, text='Show group class info',
                           command=lambda: groupClassMenu("Select"))
        slogan.pack()
    if (role == "groupClassDeleter"):
        slogan = tk.Button(frame, text='Delete group class',
                           command=lambda: groupClassMenu("Delete"))
        slogan.pack()

# Enrollment operations
    if (role == "enrollmentCreator"):
        slogan = tk.Button(frame, text='Insert new group class',
                               command=lambda: groupClassMenu("New"))

    if (role == "enrollmentEditor"):
        slogan = tk.Button(frame, text='Update group class',
                               command=lambda: groupClassMenu("Update"))
        slogan.pack()
    if (role == "enrollmentSelector"):
        slogan = tk.Button(frame, text='Show group class info',
                               command=lambda: groupClassMenu("Select"))
        slogan.pack()
    if (role == "enrollmentDeleter"):
        slogan = tk.Button(frame, text='Delete group class',
                               command=lambda: groupClassMenu("Delete"))
        slogan.pack()

    slogan = tk.Button(frame, text='Choose another role',
                       command=lambda: chooseRole())
    slogan.pack()

    slogan = tk.Button(frame, text='Log out',
                       command=lambda: login())
    slogan.pack()

def clientMenu(operationType):
    for widget in frame.winfo_children():
        widget.destroy()

    if(operationType == "New"):
        nameLabel = tk.Label(frame, text="Enter name")
        nameField = tk.Entry(frame, bd=5)
        nameLabel.pack()
        nameField.pack()

        surnameLabel = tk.Label(frame, text="Enter surname")
        surnameField = tk.Entry(frame, bd=5)
        surnameLabel.pack()
        surnameField.pack()

        ageLabel = tk.Label(frame, text="Enter age")
        ageField = tk.Entry(frame, bd=5)
        ageLabel.pack()
        ageField.pack()

        sexLabel = tk.Label(frame, text="Enter sex")
        sexField = tk.Entry(frame, bd=5)
        sexLabel.pack()
        sexField.pack()

        pinLabel = tk.Label(frame, text="Enter PIN")
        pinField = tk.Entry(frame, bd=5)
        pinLabel.pack()
        pinField.pack()

        slogan = tk.Button(frame, text='Insert new client',
                           command=lambda: operationsOnClientTable().insertClient(id=pinField.get(), name=nameField.get(),
                                                                                  surname=surnameField.get(), age=ageField.get(), sex=sexField.get()))
        slogan.pack()

    if (operationType == "Update"):
        idSelectLabel = tk.Label(frame, text="Enter Client ID to update")
        idSelectField = tk.Entry(frame, bd=5)
        idSelectLabel.pack()
        idSelectField.pack()

        nameLabel = tk.Label(frame, text="Enter name")
        nameField = tk.Entry(frame, bd=5)
        nameLabel.pack()
        nameField.pack()

        surnameLabel = tk.Label(frame, text="Enter surname")
        surnameField = tk.Entry(frame, bd=5)
        surnameLabel.pack()
        surnameField.pack()

        ageLabel = tk.Label(frame, text="Enter age")
        ageField = tk.Entry(frame, bd=5)
        ageLabel.pack()
        ageField.pack()

        sexLabel = tk.Label(frame, text="Enter sex")
        sexField = tk.Entry(frame, bd=5)
        sexLabel.pack()
        sexField.pack()

        pinLabel = tk.Label(frame, text="Enter new PIN")
        pinField = tk.Entry(frame, bd=5)
        pinLabel.pack()
        pinField.pack()

        slogan = tk.Button(frame, text='Update Client',
                           command=lambda: operationsOnClientTable().updateClient(id = idSelectField.get(),
                                                                                  idNew=pinField.get(), name=nameField.get(),
                                                                                  surname=surnameField.get(), age=ageField.get(), sex=sexField.get()))
        slogan.pack()

    if (operationType == "Select"):

        pinLabel = tk.Label(frame, text="Enter client PIN")
        pinField = tk.Entry(frame, bd=5)
        pinLabel.pack()
        pinField.pack()

        slogan = tk.Button(frame, text='Show Client',
                           command=lambda: showTable("Client", pinField.get()))
        slogan.pack()

    if (operationType == "Delete"):
        pinLabel = tk.Label(frame, text="Enter client PIN")
        pinField = tk.Entry(frame, bd=5)
        pinLabel.pack()
        pinField.pack()

        slogan = tk.Button(frame, text='Delete Client',
                           command=lambda: operationsOnClientTable().deleteClient(id=pinField.get()))
        slogan.pack()

    slogan = tk.Button(frame, text='Go back',
                           command=lambda: loggedMenu(currentRole))
    slogan.pack()


def coachMenu(operationType):
    for widget in frame.winfo_children():
        widget.destroy()

    if(operationType == "New"):
        nameLabel = tk.Label(frame, text="Enter name")
        nameField = tk.Entry(frame, bd=5)
        nameLabel.pack()
        nameField.pack()

        surnameLabel = tk.Label(frame, text="Enter surname")
        surnameField = tk.Entry(frame, bd=5)
        surnameLabel.pack()
        surnameField.pack()

        pinLabel = tk.Label(frame, text="Enter PIN")
        pinField = tk.Entry(frame, bd=5)
        pinLabel.pack()
        pinField.pack()

        slogan = tk.Button(frame, text='Insert new coach',
                           command=lambda: operationsOnCoachTable().insertCoach(id=pinField.get(),
                                                                                name=nameField.get(),
                                                                                surname=surnameField.get()))
        slogan.pack()

    if (operationType == "Update"):
        idSelectLabel = tk.Label(frame, text="Enter Coach ID to update")
        idSelectField = tk.Entry(frame, bd=5)
        idSelectLabel.pack()
        idSelectField.pack()

        nameLabel = tk.Label(frame, text="Enter name")
        nameField = tk.Entry(frame, bd=5)
        nameLabel.pack()
        nameField.pack()

        surnameLabel = tk.Label(frame, text="Enter surname")
        surnameField = tk.Entry(frame, bd=5)
        surnameLabel.pack()
        surnameField.pack()

        pinLabel = tk.Label(frame, text="Enter new PIN")
        pinField = tk.Entry(frame, bd=5)
        pinLabel.pack()
        pinField.pack()

        slogan = tk.Button(frame, text='Update Coach info',
                           command=lambda: operationsOnCoachTable().updateCoach(id = idSelectField.get(),
                                                                                idNew=pinField.get(),
                                                                                name=nameField.get(),
                                                                                surname=surnameField.get()))
        slogan.pack()

    if (operationType == "Select"):

        pinLabel = tk.Label(frame, text="Enter coach PIN")
        pinField = tk.Entry(frame, bd=5)
        pinLabel.pack()
        pinField.pack()

        slogan = tk.Button(frame, text='Show coach info',
                           command=lambda: showTable("Coach", pinField.get()))
        slogan.pack()

    if (operationType == "Delete"):
        pinLabel = tk.Label(frame, text="Enter coach PIN")
        pinField = tk.Entry(frame, bd=5)
        pinLabel.pack()
        pinField.pack()

        slogan = tk.Button(frame, text='Delete coach',
                           command=lambda: operationsOnCoachTable().deleteCoach(id=pinField.get()))
        slogan.pack()

    slogan = tk.Button(frame, text='Go back',
                           command=lambda: loggedMenu(currentRole))
    slogan.pack()

def gymMenu(operationType):
    for widget in frame.winfo_children():
        widget.destroy()

    if(operationType == "New"):
        nameLabel = tk.Label(frame, text="Enter name")
        nameField = tk.Entry(frame, bd=5)
        nameLabel.pack()
        nameField.pack()

        addressLabel = tk.Label(frame, text="Enter address")
        addressField = tk.Entry(frame, bd=5)
        addressLabel.pack()
        addressField.pack()

        quantityLabel = tk.Label(frame, text="Enter rooms quantity")
        quantityField = tk.Entry(frame, bd=5)
        quantityLabel.pack()
        quantityField.pack()

        slogan = tk.Button(frame, text='Insert new gym',
                           command=lambda: operationsOnGymTable().insertGym(name=nameField.get(),
                                                                            address=addressField.get(),
                                                                            roomsQuantity=quantityField.get()))
        slogan.pack()

    if (operationType == "Update"):
        addressSelectLabel = tk.Label(frame, text="Enter gym address to update")
        addressSelectField = tk.Entry(frame, bd=5)
        addressSelectLabel.pack()
        addressSelectField.pack()

        nameLabel = tk.Label(frame, text="Enter new name")
        nameField = tk.Entry(frame, bd=5)
        nameLabel.pack()
        nameField.pack()

        addressNewLabel = tk.Label(frame, text="Enter new address")
        addressNewField = tk.Entry(frame, bd=5)
        addressNewLabel.pack()
        addressNewField.pack()

        quantityLabel = tk.Label(frame, text="Enter new rooms quantity")
        quantityField = tk.Entry(frame, bd=5)
        quantityLabel.pack()
        quantityField.pack()

        slogan = tk.Button(frame, text='Update gym info',
                           command=lambda: operationsOnGymTable().updateGym(address = addressSelectField.get(),
                                                                            name = nameField.get(),
                                                                            addressNew=addressNewField.get(),
                                                                            roomsQuantity=quantityField.get()))
        slogan.pack()

    if (operationType == "Select"):
        addressLabel = tk.Label(frame, text="Enter gym address")
        addressField = tk.Entry(frame, bd=5)
        addressLabel.pack()
        addressField.pack()

        slogan = tk.Button(frame, text='Show gym',
                           command=lambda: showTable("Gym", addressField.get()))
        slogan.pack()

    if (operationType == "Delete"):
        addressLabel = tk.Label(frame, text="Enter gym address")
        addressField = tk.Entry(frame, bd=5)
        addressLabel.pack()
        addressField.pack()

        slogan = tk.Button(frame, text='Delete gym',
                           command=lambda: operationsOnGymTable().deleteGym(address=addressField.get()))
        slogan.pack()

    slogan = tk.Button(frame, text='Go back',
                           command=lambda: loggedMenu(currentRole))
    slogan.pack()


def groupClassMenu(operationType):
    for widget in frame.winfo_children():
        widget.destroy()

    if(operationType == "New"):
        nameLabel = tk.Label(frame, text="Enter name")
        nameField = tk.Entry(frame, bd=5)
        nameLabel.pack()
        nameField.pack()

        maxSeatsLabel = tk.Label(frame, text="Enter max seats number")
        maxSeatsField = tk.Entry(frame, bd=5)
        maxSeatsLabel.pack()
        maxSeatsField.pack()

        slogan = tk.Button(frame, text='Insert new group class',
                           command=lambda: operationsOnGroupClassTable().insertGroupClass(className=nameField.get(),
                                                                                          maxSeats=maxSeatsField.get()))
        slogan.pack()

    if (operationType == "Update"):
        nameLabel = tk.Label(frame, text="Enter group class name to update")
        nameField = tk.Entry(frame, bd=5)
        nameLabel.pack()
        nameField.pack()

        nameNewLabel = tk.Label(frame, text="Enter new name")
        nameNewField = tk.Entry(frame, bd=5)
        nameNewLabel.pack()
        nameNewField.pack()

        maxSeatsLabel = tk.Label(frame, text="Enter new max seats number")
        maxSeatsField = tk.Entry(frame, bd=5)
        maxSeatsLabel.pack()
        maxSeatsField.pack()

        slogan = tk.Button(frame, text='Update group class info',
                           command=lambda: operationsOnGroupClassTable().updateGroupClass(className = nameField.get(),
                                                                                          classNameNew = nameNewField.get(),
                                                                                          maxSeats=maxSeatsField.get()))
        slogan.pack()

    if (operationType == "Select"):
        nameLabel = tk.Label(frame, text="Enter group class name")
        nameField = tk.Entry(frame, bd=5)
        nameLabel.pack()
        nameField.pack()

        slogan = tk.Button(frame, text='Show group class info',
                           command=lambda: showTable("GroupClass", nameField.get()))
        slogan.pack()

    if (operationType == "Delete"):
        nameLabel = tk.Label(frame, text="Enter group class name")
        nameField = tk.Entry(frame, bd=5)
        nameLabel.pack()
        nameField.pack()

        slogan = tk.Button(frame, text='Delete group class',
                           command=lambda: operationsOnGroupClassTable().deleteGroupClass(className=nameField.get()))
        slogan.pack()

    if (operationType == "assignGym"):
        gyms = []
        groupClasses = []

        for gym in session.query(Gym).order_by(Gym.id):
            gyms.append(gym.name)
        for groupClass in session.query(GroupClass).order_by(GroupClass.id):
            groupClasses.append(groupClass.className)

        gymList = tk.Listbox(frame, exportselection = 0)
        x = 0
        for gym in gyms:
            gymList.insert(x, gym)
            x += 1
        gymList.pack(side = tk.LEFT)

        groupClassList = tk.Listbox(frame, exportselection = 0)
        x = 0
        for groupClass in groupClasses:
            groupClassList.insert(x, groupClass)
            x += 1
        groupClassList.pack(side = tk.LEFT)

        slogan = tk.Button(frame, text='Assign',
                           command=lambda: operationsOnGroupClassTable().assignGym(className = groupClassList.get(groupClassList.curselection()),
                                                                                   gymID=gymList.get(gymList.curselection())))
        slogan.pack(side=tk.BOTTOM)

    if (operationType == "assignCoach"):
        coaches = []
        groupClasses = []

        for coach in session.query(Coach).order_by(Coach.id):
            coaches.append(coach.id)
        for groupClass in session.query(GroupClass).order_by(GroupClass.id):
            groupClasses.append(groupClass.className)

        coachList = tk.Listbox(frame, exportselection = 0)
        x = 0
        for coach in coaches:
            coachList.insert(x, coach)
            x += 1
        coachList.pack(side = tk.LEFT)

        groupClassList = tk.Listbox(frame, exportselection = 0)
        x = 0
        for groupClass in groupClasses:
            groupClassList.insert(x, groupClass)
            x += 1
        groupClassList.pack(side = tk.LEFT)

        slogan = tk.Button(frame, text='Assign',
                           command=lambda: operationsOnGroupClassTable().assignCoach(className=groupClassList.get(groupClassList.curselection()),
                                                                                     coachID=coachList.get(coachList.curselection())))
        slogan.pack(side=tk.BOTTOM)

    slogan = tk.Button(frame, text='Go back',
                           command=lambda: loggedMenu(currentRole))
    slogan.pack(side = tk.BOTTOM)


def termMenu(operationType):
    for widget in frame.winfo_children():
        widget.destroy()

    if(operationType == "New"):
        dateLabel = tk.Label(frame, text="Enter date")
        dateField = tk.Entry(frame, bd=5)
        dateLabel.pack()
        dateField.pack()

        durationLabel = tk.Label(frame, text="Enter duration")
        durationField = tk.Entry(frame, bd=5)
        durationLabel.pack()
        durationField.pack()

        slogan = tk.Button(frame, text='Insert new term',
                           command=lambda: operationsOnTermTable().insertTerm(classDate=dateField.get(),
                                                                              duration=durationField.get()))
        slogan.pack()

    if (operationType == "Update"):
        dateLabel = tk.Label(frame, text="Enter term date to update")
        dateField = tk.Entry(frame, bd=5)
        dateLabel.pack()
        dateField.pack()

        dateNewLabel = tk.Label(frame, text="Enter new date")
        dateNewField = tk.Entry(frame, bd=5)
        dateNewLabel.pack()
        dateNewField.pack()

        durationLabel = tk.Label(frame, text="Enter new duration")
        durationField = tk.Entry(frame, bd=5)
        durationLabel.pack()
        durationField.pack()

        slogan = tk.Button(frame, text='Update term info',
                           command=lambda: operationsOnTermTable().updateTerm(classDate=dateField.get(),
                                                                              classDateNew=dateNewField.get(),
                                                                              duration=durationField.get()))
        slogan.pack()

    if (operationType == "Select"):
        dateLabel = tk.Label(frame, text="Enter term date")
        dateField = tk.Entry(frame, bd=5)
        dateLabel.pack()
        dateField.pack()

        slogan = tk.Button(frame, text='Show term info',
                           command=lambda: showTable("Term", dateField.get()))
        slogan.pack()

    if (operationType == "Delete"):
        dateLabel = tk.Label(frame, text="Enter term date")
        dateField = tk.Entry(frame, bd=5)
        dateLabel.pack()
        dateField.pack()

        slogan = tk.Button(frame, text='Delete term',
                           command=lambda: operationsOnTermTable().deleteTerm(classDate=dateField.get()))
        slogan.pack()

        slogan = tk.Button(frame, text='Delete term',
                           command=lambda: operationsOnTermTable().deleteTerm(classDate=dateField.get()))
        slogan.pack()

    slogan = tk.Button(frame, text='Go back',
                           command=lambda: loggedMenu(currentRole))
    slogan.pack()


def enrollmentTable(operationType):
    for widget in frame.winfo_children():
        widget.destroy()

    if (operationType == "Insert"):
        terms = []
        clients = []
        for term in session.query(Term).order_by(Term.id):
            terms.append(term.classDate)
        for client in session.query(Client).order_by(Client.id):
            clients.append(client.id)

        termList = tk.Listbox(frame, exportselection = 0)
        x = 0
        for term in terms:
            termList.insert(x, term)
            x += 1
        termList.pack(side = tk.LEFT)

        clientList = tk.Listbox(frame, exportselection=0)
        x = 0
        for client in clients:
            clientList.insert(x, client)
            x += 1
            clientList.pack(side=tk.LEFT)

        slogan = tk.Button(frame, text='Enroll client',
                           command=lambda: operationsOnEnrollmentTable().insertEnrollment(clientID=clientList.get(clientList.curselection()),
                                                                                     termID=termList.get(termList.curselection())))
        slogan.pack(side=tk.BOTTOM)

    if (operationType == "Update"):
        terms = []
        clients = []
        for term in session.query(Term).order_by(Term.id):
            terms.append(term.classDate)
        for client in session.query(Client).order_by(Client.id):
            clients.append(client.id)

        termList = tk.Listbox(frame, exportselection=0)
        x = 0
        for term in terms:
            termList.insert(x, term)
            x += 1
        termList.pack(side=tk.LEFT)

        clientList = tk.Listbox(frame, exportselection=0)
        x = 0
        for client in clients:
            clientList.insert(x, client)
            x += 1
            clientList.pack(side=tk.LEFT)

        newClientIDLabel = tk.Label(frame, text="Enter term date")
        newClientIDField = tk.Entry(frame, bd=5)
        newClientIDLabel.pack()
        newClientIDField.pack()

        newTermIDLabel = tk.Label(frame, text="Enter term date")
        newTermIDField = tk.Entry(frame, bd=5)
        newTermIDLabel.pack()
        newTermIDField.pack()

        slogan = tk.Button(frame, text='Enroll client',
                           command=lambda: operationsOnEnrollmentTable().updateEnrollment(
                               clientID=clientList.get(clientList.curselection()),
                               termID=termList.get(termList.curselection()),
                               clientIDNew=newClientIDField.get(),
                               termIDNew=newTermIDField.get()))
        slogan.pack(side=tk.BOTTOM)

    if (operationType == "Delete"):
        terms = []
        clients = []
        for term in session.query(Term).order_by(Term.id):
            terms.append(term.classDate)
        for client in session.query(Client).order_by(Client.id):
            clients.append(client.id)

        termList = tk.Listbox(frame, exportselection=0)
        x = 0
        for term in terms:
            termList.insert(x, term)
            x += 1
        termList.pack(side=tk.LEFT)

        clientList = tk.Listbox(frame, exportselection=0)
        x = 0
        for client in clients:
            clientList.insert(x, client)
            x += 1
            clientList.pack(side=tk.LEFT)

        slogan = tk.Button(frame, text='Delete enrollment',
                           command=lambda: operationsOnEnrollmentTable().deleteEnrollment(
                               clientID=clientList.get(clientList.curselection()),
                               termID=termList.get(termList.curselection())))
        slogan.pack(side=tk.BOTTOM)

    slogan = tk.Button(frame, text='Go back',
                           command=lambda: loggedMenu(currentRole))
    slogan.pack()


def showTable(tableName, objectId):
    if(tableName == "Client"):
        client = operationsOnClientTable().selectClient(id=objectId)
        if(not(client is None)):
            clientInfo = "ID: "+str(client.id)+"\nName: "+client.name+"\nSurname: "+client.surname+"\nSex: "+client.sex+"\nAge: "+str(client.age)
            tk.messagebox.showinfo("Client info", clientInfo)
        else:
            tk.messagebox.showinfo("Client info", "Client not found")
        return

    elif(tableName == "Coach"):
        coach = operationsOnCoachTable().selectCoach(id=objectId)
        if (not(coach is None)):
            coachInfo = "ID: " + str(coach.id) + "\nName: " + coach.name + "\nSurname: " + coach.surname
            tk.messagebox.showinfo("coach info", coachInfo)
        else:
            tk.messagebox.showinfo("coach info", "Coach not found")
        return

    elif(tableName == "Gym"):
        gym = operationsOnGymTable().selectGym(address=objectId)
        if (not (gym is None)):
            gymInfo = "ID: " + str(gym.id) + "\nName: " + gym.name + "\nAddress: " + gym.address +"\nRoom Quantity:" + str(gym.roomsQuantity)
            tk.messagebox.showinfo("Gym info", gymInfo)
        else:
            tk.messagebox.showinfo("Gym info", "Gym not found")
        return

    elif(tableName == "GroupClass"):
        groupClass = operationsOnGroupClassTable().selectGroupClass(className=objectId)
        if (not (groupClass is None)):
            gymID = groupClass.gymID
            if(gymID is None):
                gymID = "Not assigned"

            coachID = groupClass.coachID
            if(coachID is None):
                coachID = "Not assigned"

            groupClassInfo = "ID: " + str(groupClass.id) + "\nClass name: " + groupClass.className + "\nMax seats: " + str(groupClass.maxSeats)\
                             + "\nGym ID: " + str(gymID) + "\nCoach ID: " + str(coachID)
            tk.messagebox.showinfo("Group class info", groupClassInfo)
        else:
            tk.messagebox.showinfo("Group class info", "Group class not found")
        return

    elif(tableName == "Term"):
        term = operationsOnTermTable().selectTerm(classDate=objectId)
        if (not (term is None)):
            termInfo = "ID: " + str(term.id) + "\nDate: " + str(term.classDate) + "\nDuration: " + str(term.duration)
            tk.messagebox.showinfo("Term info", termInfo)
        else:
            tk.messagebox.showinfo("Term info", "Term not found")
        return

#BACKEND
def logging(loginUsr, password):
    global currentLogin
    if (check_errors(loginUsr, password)!= -1):
        try:
            if rbac.users[loginUsr]['password'] == password:
                currentLogin = loginUsr
                chooseRole()
            else:
                tk.messagebox.showerror("Error message", "Login or password not correct")
        except:
            tk.messagebox.showerror("Error message", "Login not found in database")



def registering(email, password, passwordAgain, name, surname, sex, age, PIN):
    if(check_errors(email = email, password = password, passwordAgain = passwordAgain, name = name, surname = surname, sex = sex, age = age, PIN = PIN)!=-1):
        print("Implement")


def check_errors(email = -1, password = -1, passwordAgain = -1, name = -1, surname = -1, sex = -1, age = -1, PIN = -1):

    if (email is None or email == ""):
       tk.messagebox.showerror("Error message", "Please enter email")
       return -1

    elif (password is None or password == ""):
         tk.messagebox.showerror("Error message", "Please enter password")
         return -1

    elif (passwordAgain is None or passwordAgain == ""):
         tk.messagebox.showerror("Error message", "Please confirm your password")
         return -1

    elif (passwordAgain != -1 and (password != passwordAgain)):
         tk.messagebox.showerror("Error message", "Passwords does not match")
         return -1

    elif (name is None or name == ""):
         tk.messagebox.showerror("Error message", "Please enter name")
         return -1

    elif (surname is None or surname == ""):
         tk.messagebox.showerror("Error message", "Please enter surname")
         return -1

    elif (sex is None or sex == ""):
         tk.messagebox.showerror("Error message", "Please enter sex")
         return -1

    elif (age is None or age == ""):
         tk.messagebox.showerror("Error message", "Please enter age")
         return -1

    elif (PIN is None or PIN == ""):
         tk.messagebox.showerror("Error message", "Please enter PIN")
         return -1

root = tk.Tk()
root.geometry('600x600')
root.resizable(0, 0)

frame = tk.Frame(root)
frame.pack()

login()

root.mainloop()