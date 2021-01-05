import DbConnection
import Entities

class User:
    #DB Entity for this wrapper
    internalData = Entities.User()

    def __init__(self):
        return
        
    #Returns Id of user.
    def __init__(self, id):
        internalData = DbConnection.session.query(Entities.User).filter_by(Entites.User.id == id).first()
        if internalData == None:
            raise ValueError
    
    def id():
        return internalData.Id
    
    #Return name of user.
    def name():
        return internalData.Name
    
    #Renames a user if possible. Returns bool.
    def rename(name):
        result = False
        validName = len(DbConnection.session.query(Entities.User).filter_by(Entities.User.name == name).all()) == 0;
        if validName == True:
            internalData.name = name
            DbConnection.session.commit()
            result = True
        return result
    
    #Validates password for this user.
    def validate(passwordHash):
        return passwordHash == internalData
    
    #Gets this users group. Returns Group.    
    def group():
        return Group(internalData.GroupId)
     
    #Create a new user and save it to database.  
    @staticmethod
    def Create(name, passwordHash):
        newUser = Entities.User();
        newUser.name = name
        newUser.password = passwordHash

        DbConnection.session.add(newUser);
        DbConnection.session.commit();

        #TODO kéne tudni hogy sikeres volt-e! Commit dob vissza ilyet?
        return True
    
    #Get all users currently stored in the database. Returns List<User>
    @staticmethod
    def All():
        entities = DbConnection.session.query(Entities.User).any();
    
    #Return a User with the given name, or Nnone if no such user exists
    @staticmethod
    def ByName(name):
        result = None

        entity = DbConnection.session.query(Entities.User).filter_by(Entities.User.name == name).first()
        if entity != None:
            result = User(entity.id)
        
        return result;

class Group:
    #DB Entity for this wrapper
    internalData = Entities.Group()

    #Returns Id of group.
    def __init__(self, id):
        internalData = DbConnection.session.query(Entities.Group).filter_by(Entites.Group.id).first()
        if internalData == None:
            raise ValueError
    
    def id():
        return internalData.Id
    
    #Return name of group.
    def name():
        return internalData.Name
    
    #Renames a group if possible. Returns bool.
    def rename(name):
        result = False
        validName = len(DbConnection.session.query(Entities.Group).all(Entities.Group.name == name)) == 0;
        if validName == True:
            internalData.name = name
            session.commit()
            result = True
        return result
    
    #Assign user to this group.
    def assign(user):
        user.internalData.Group = internalData.Id
        DbConnection.session.commit();
    
    #Remove user from this group.    
    def remove(user):
        user.internalData.Group = None
        DbConnection.session.commit();
           
    #Create a new user and save it to database.  
    @staticmethod
    def Create(name):
        newGroup = Entities.Group();
        newGroup.name = name

        DbConnection.session.add(newGroup);
        DbConnection.session.commit();

        #TODO kéne tudni hogy sikeres volt-e! Commit dob vissza ilyet?
        return True
    
    #Get all users currently stored in the database. Returns List<User>
    @staticmethod
    def All():
        return #TODO
    
   #Return a Group with the given name, or Nnone if no such user exists
    @staticmethod
    def ByName(name):
        result = None

        entity = DbConnection.session.query(Entities.Group).filter_by(Entities.Group.name == name).first()
        if entity != None:
            result = Group(entity.id)
        
        return result;

class Question:
    #DB Entity for this wrapper
    internalData = Entities.Question()

    #Returns Id of question.
    def __init__(self, id):
        internalData = DbConnection.session.query(Entities.Question).filter_by(Entites.Question.id==id).first()
        if internalData == None:
            raise ValueError
    
    def id():
        return internalData.Id
    
    #Return question text of this question.
    def question():
        return internalData.question

    #Return answer text of this question.
    def answer():
        return internalData.answer

    #Make a guess with the user provided.
    def guess(user, answer):
        return #TODO

    #Provide the hint text to the user provided
    def hint(user):
        return #TODO

    #Create a new question and save it to database.  
    @staticmethod
    def Create(id, question, answer, hint, image):
        return #TODO
    
    #Get all questions currently stored in the database. Returns List<Question>
    @staticmethod
    def All():
        return #TODO

class Statistics:
    #Return how many times a group has used a questions hint. Return JSON formatted string.
    @staticmethod
    def ByHints():
        return #TODO

    #Returns how much time each group ha needed to answer a question. Return JSON formatted string.
    @staticmethod
    def ByHours():
        return #TODO
