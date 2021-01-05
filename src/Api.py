
class User
    #DB Entity for this wrapper
    internalData

    #Returns Id of user.
    def __init__(self, id):
        #TODO query
        internalData = QUERY
    
    def id():
        return internalData.Id
    
    #Return name of user.
    def name():
        return internalData.Name
    
    #Renames a user if possible. Returns bool.
    def rename(name)
        return false //TODO
    
    #Validates password for this user.
    def validate(passwordHash)
        return passwordHash = internalData;
    
    #Gets this users group. Returns Group.    
    def group():
        return Group(internalData.GroupId)
     
    #Create a new user and save it to database.  
    @staticmethod
    def Create(name, passwordHash)
        return #TODO
    
    #Get all users currently stored in the database. Returns List<User>
    @staticmethod
    def All()
        return #TODO
    
    #??? TODO
    @staticmethod
    def ByName()
        return  #TODO

class Group
    #DB Entity for this wrapper
    internalData

    #Returns Id of group.
    def __init__(self, id):
        #TODO query
        internalData = QUERY
    
    def id():
        return internalData.Id
    
    #Return name of group.
    def name():
        return internalData.Name
    
    #Renames a group if possible. Returns bool.
    def rename(name)
        return false //TODO
    
    #Assign user to this group.
    def assign(user):
        user.internalData.Group = internalData.Id
        user.save #TODO
    
    #Remove user from this group.    
    def remove(user):
        user.internalData.Group = null
        user.save #TODO
           
    #Create a new user and save it to database.  
    @staticmethod
    def Create(name, passwordHash)
        return #TODO
    
    #Get all users currently stored in the database. Returns List<User>
    @staticmethod
    def All()
        return #TODO
    
    #??? TODO
    @staticmethod
    def ByName()
        return  #TODO

class Question
    #DB Entity for this wrapper
    internalData

    #Returns Id of question.
    def __init__(self, id):
        #TODO query
        internalData = QUERY
    
    def id():
        return internalData.Id
    
    #Return question text of this question.
    def question():
        return internalData.Question

    #Return answer text of this question.
    def answer():
        return internalData.Answer

    #Make a guess with the user provided.
    def guess(user, answer):
        return #TODO

    #Provide the hint text to the user provided
    def hint(user):
        return #TODO

    #Create a new question and save it to database.  
    @staticmethod
    def Create(id, question, answer, hint, image)
        return #TODO
    
    #Get all questions currently stored in the database. Returns List<Question>
    @staticmethod
    def All()
        return #TODO

class Statistics
    #Return how many times a group has used a questions hint. Return JSON formatted string.
    @staticmethod
    def ByHints()
        return #TODO

    #Returns how much time each group ha needed to answer a question. Return JSON formatted string.
    @staticmethod
    def ByHours()
        return #TODO
