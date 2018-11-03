from dataBase import *


class operationsOnCoachTable():

    def insertCoach(self, id, name, surname):
        session.add(Coach(id, name, surname))
        session.commit()

    def selectCoach(self, id):
        for instance in session.query(Coach).order_by(Coach.id):
            if(instance.id == int(id)):
                return instance
        return None

    def updateCoach(self, id, idNew = None, name = None, surname = None):
        for instance in session.query(Coach).order_by(Coach.id):
            if(instance.id == int(id)):
                if(not(idNew is None or idNew == "")):
                    instance.id = idNew
                if (not (name is None or name == "")):
                    instance.name = name
                if (not (surname is None or surname == "")):
                    instance.surname = surname

    def deleteCoach(self, id):
        for instance in session.query(Coach).order_by(Coach.id):
            if(instance.id == int(id)):
                session.delete(instance)
                session.commit()


class operationsOnClientTable():

    def insertClient(self, id, name, surname, sex, age):
        session.add(Client(id, name, surname, sex, age))
        session.commit()

    def selectClient(self, id):
        for instance in session.query(Client).order_by(Client.id):
            if(instance.id == int(id)):
                return instance
        return None

    def updateClient(self, id, idNew = None, name = None, surname = None, sex = None, age = None):
        for instance in session.query(Client).order_by(Client.id):
            if(instance.id == int(id)):
                if(not(idNew is None or idNew == "")):
                    instance.id = idNew
                if (not (name is None or name == "")):
                    instance.name = name
                if (not (surname is None or surname == "")):
                    instance.surname = surname
                if (not (sex is None or sex == "")):
                    instance.sex = sex
                if (not (age is None or age == "")):
                    instance.age = age

    def deleteClient(self, id):
        for instance in session.query(Client).order_by(Client.id):
            if(instance.id == int(id)):
                session.delete(instance)
                session.commit()


class operationsOnGymTable():

    def insertGym(self, name, address, roomsQuantity):
        session.add(Gym(name, address, roomsQuantity))
        session.commit()

    def selectGym(self, address):
        for instance in session.query(Gym).order_by(Gym.id):
            if(instance.address == address): #to check!!
                return instance
        return None

    def updateGym(self, address = None, name = None, addressNew = None, roomsQuantity = None):
        for instance in session.query(Gym).order_by(Gym.id):
            if(instance.address == address):
                if(not(name is None or name == "")):
                    instance.name = name
                if (not (addressNew is None or addressNew == "")):
                    instance.address = addressNew
                if (not (roomsQuantity is None or roomsQuantity == "")):
                    instance.roomsQuantity = roomsQuantity

    def deleteGym(self, address):
        for instance in session.query(Gym).order_by(Gym.id):
            if(instance.address == address):
                session.delete(instance)
                session.commit()


class operationsOnGroupClassTable():

    def insertGroupClass(self, className, maxSeats):
        session.add(GroupClass(className, maxSeats))
        session.commit()

    def selectGroupClass(self, className):
        for instance in session.query(GroupClass).order_by(GroupClass.id):
            if(instance.className == className):
                return instance
        return None

    def updateGroupClass(self, className = None, classNameNew = None, maxSeats = None):
        for instance in session.query(GroupClass).order_by(GroupClass.id):
            if(instance.className == className):
                if(not(classNameNew is None or classNameNew == "")):
                    instance.className = classNameNew
                if (not (maxSeats is None or maxSeats == "")):
                    instance.maxSeats = maxSeats

    def deleteGroupClass(self, className):
        for instance in session.query(GroupClass).order_by(GroupClass.id):
            if(instance.className == className):
                session.delete(instance)
                session.commit()

    def assignGym(self, className, gymID):
        for instance in session.query(GroupClass).order_by(GroupClass.id):
            if(instance.className == className):
                instance.gymID = gymID

    def assignCoach(self, className, coachID):
        for instance in session.query(GroupClass).order_by(GroupClass.id):
            if(instance.className == className):
                instance.coachID = coachID


class operationsOnTermTable():

    def insertTerm(self, classDate, duration):
        session.add(Term(classDate, duration))
        session.commit()

    def selectTerm(self, classDate):
        for instance in session.query(Term).order_by(Term.id):
            if(instance.classDate == classDate):
                return instance
        return None

    def updateTerm(self, classDate = None, classDateNew = None, duration = None):
        for instance in session.query(Term).order_by(Term.id):
            if(instance.classDate == classDate):
                if(not(classDateNew is None or classDateNew == "")):
                    instance.className = classDateNew
                if (not (duration is None or duration == "")):
                    instance.duration = duration

    def deleteTerm(self, classDate):
        for instance in session.query(Term).order_by(Term.id):
            if(instance.classDate == classDate):
                session.delete(instance)
                session.commit()


class operationsOnEnrollmentTable():

    def insertEnrollment(self, clientID, termID):
        session.add(Enrollment(clientID, termID))
        session.commit()

    def selectEnrollment(self, clientID, termID):
        for instance in session.query(Enrollment).order_by(Enrollment.id):
            if ((instance.termID == termID) and (instance.clientID == clientID)):
                return instance
        return None

    def updateEnrollment(self, termID = None, clientID = None, termIDNew = None, clientIDNew = None):
        for instance in session.query(Enrollment).order_by(Enrollment.id):
            if ((instance.termID == termID) and (instance.clientID == clientID)):
                if(not(termIDNew is None or termIDNew == "")):
                    instance.termID = termIDNew
                if (not (clientIDNew is None or clientIDNew == "")):
                    instance.clientID = clientIDNew

    def deleteEnrollment(self, clientID, termID):
        for instance in session.query(Enrollment).order_by(Enrollment.id):
            if((instance.termID == termID) and (instance.clientID == clientID)):
                session.delete(instance)
                session.commit()