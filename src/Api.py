import DbConnection
import Entities
import json

class User:
    #DB Entity for this wrapper
    internalData = Entities.User()
        
    #Returns Id of user.
    def __init__(self, id):
        self.internalData = DbConnection.session.query(Entities.User).filter(Entities.User.id == id).first()
        if self.internalData == None:
            raise ValueError
    
    def id(self):
        return self.internalData.id
    
    #Return name of user.
    def name(self):
        return self.internalData.name
    
    #Renames a user if possible. Returns bool.
    def rename(self, name):
        result = False
        validName = len(DbConnection.session.query(Entities.User).filter(Entities.User.name == name).all()) == 0
        if validName == True:
            self.internalData.name = name
            DbConnection.session.commit()
            result = True
        return result
    
    #Validates password for this user.
    def validate(self, passwordHash):
        return passwordHash == self.internalData
    
    #Gets this users group. Returns Group.    
    def group(self):
        return Group(self.internalData.group_id)
     
    #Create a new user and save it to database.  
    @staticmethod
    def Create(name, passwordHash):
        newUser = Entities.User()
        newUser.name = name
        newUser.password = passwordHash

        DbConnection.session.add(newUser)
        DbConnection.session.commit()

        #TODO kéne tudni hogy sikeres volt-e! Commit dob vissza ilyet?
        return True
    
    @staticmethod
    def Delete(id):
        entity = DbConnection.session.query(Entities.Question).get(id);
        if(entity != None and entity.id != None)
            DbConnection.session.delete(entity)
            DbConnection.session.commit()
            
    #Get all users currently stored in the database. Returns List<User>
    @staticmethod
    def All():
        result = []
        entities = DbConnection.session.query(Entities.User).all()
        for entity in entities:
            result.append(User(entity.id))
        return result
    
    #Return a User with the given name, or Nnone if no such user exists
    @staticmethod
    def ByName(name):
        result = None

        entity = DbConnection.session.query(Entities.User).filter(Entities.User.name == name).first()
        if entity != None:
            result = User(entity.id)
        
        return result

class Group:
    #DB Entity for this wrapper
    internalData = Entities.Group()

    #Returns Id of group.
    def __init__(self, id):
        self.internalData = DbConnection.session.query(Entities.Group).filter(Entities.Group.id == id).first()
        if self.internalData == None:
            raise ValueError
    
    def id(self):
        return self.internalData.id
    
    #Return name of group.
    def name(self):
        return self.internalData.name
    
    #Renames a group if possible. Returns bool.
    def rename(self, name):
        result = False
        validName = len(DbConnection.session.query(Entities.Group).all(Entities.Group.name == name)) == 0
        if validName == True:
            self.internalData.name = name
            DbConnection.session.commit()
            result = True
        return result
    
    #Assign user to this group.
    def assign(self, user):
        user.internalData.Group = self.internalData.id
        DbConnection.session.commit()
    
    #Remove user from this group.    
    def remove(self, user):
        user.internalData.Group = None
        DbConnection.session.commit()
           
    #Create a new user and save it to database.  
    @staticmethod
    def Create(name):
        newGroup = Entities.Group()
        newGroup.name = name

        DbConnection.session.add(newGroup)
        DbConnection.session.commit()

        #TODO kéne tudni hogy sikeres volt-e! Commit dob vissza ilyet?
        return True
    
    @staticmethod
    def Delete(id):
        entity = DbConnection.session.query(Entities.Question).get(id);
        if(entity != None and entity.id != None)
            DbConnection.session.delete(entity)
            DbConnection.session.commit()
    
    #Get all users currently stored in the database. Returns List<User>
    @staticmethod
    def All():
        result = []
        entities = DbConnection.session.query(Entities.Group).all()
        for entity in entities:
            result.append(Group(entity.id))
        return result
    
   #Return a Group with the given name, or Nnone if no such user exists
    @staticmethod
    def ByName(name):
        result = None

        entity = DbConnection.session.query(Entities.Group).filter(Entities.Group.name == name).first()
        if entity != None:
            result = Group(entity.id)
        
        return result

class Question:
    #DB Entity for this wrapper
    internalData = Entities.Question()

    #Returns Id of question.
    def __init__(self, id):
        self.internalData = DbConnection.session.query(Entities.Question).filter(Entities.Question.id == id).first()
        if self.internalData == None:
            raise ValueError
    
    def id(self):
        return self.internalData.id
    
    #Return question text of this question.
    def question(self):
        return self.internalData.question

    #Return answer text of this question.
    def answer(self):
        return self.internalData.answer

    #Make a guess with the user provided.
    def guess(self, user, answer):
        return #TODO

    #Provide the hint text to the user provided
    def hint(self, user):
        return #TODO

    #Create a new question and save it to database.  
    @staticmethod
    def Create(id, question, answer, hint, image):
        newQuestion = Entities.Question()
        newQuestion.id = id
        newQuestion.question = question
        newQuestion.answer = answer
        newQuestion.hint = hint
        newQuestion.image = image

        DbConnection.session.add(newQuestion)
        DbConnection.session.commit()

        #TODO kéne tudni hogy sikeres volt-e! Commit dob vissza ilyet?
        return True
    
    @staticmethod
    def Delete(id):
        entity = DbConnection.session.query(Entities.Question).get(id);
        if(entity != None and entity.id != None)
            DbConnection.session.delete(entity)
            DbConnection.session.commit()

    #Get all questions currently stored in the database. Returns List<Question>
    @staticmethod
    def All():
        result = []
        entities = DbConnection.session.query(Entities.Question).all()
        for entity in entities:
            result.append(Question(entity.id))
        return result

class Statistics:
    #Return how many times a group has used a questions hint. Return JSON formatted string.
    @staticmethod
    def ByHints():
        rounds = DbConnection.session.query(Entities.Round).all()
        groups = DbConnection.session.query(Entities.Group).all()

        def list_hint_stat(rounds, group_id):
            g_rounds = [round for round in rounds if round.group_id == group_id]
            question_ids = {round.question_id for round in g_rounds}
            return [
                {
                    'question_id': q_id,
                    'hints_used': len([round
                                       for round
                                       in g_rounds
                                       if round.question_id == q_id and round.hint_used])}
                for q_id in question_ids]

        stat = {group.id: {'name': group.name, 'hints': list_hint_stat(rounds, group.id)} for group in groups}

        return json.dumps(stat)


    #Returns how much time each group ha needed to answer a question. Return JSON formatted string.
    @staticmethod
    def ByHours():
        groups = DbConnection.session.query(Entities.Group).all()
        stat = {group.id: {'name': group.name, 'hints': []} for group in groups}
        return json.dumps(stat)
