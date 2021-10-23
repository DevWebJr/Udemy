class Person:
    def __init__(self,first_name:str, nick_name:str, age:int,gender:bool):
        self.first_name = first_name
        self.nick_name = nick_name
        self.age = age
        self.gender = gender


    def Is_Adult(self):
        return self.age >= 18  #__adult__# or #__child__#
      
      
    # def Is_A_He(self):
    #     return self.gender  
    

    # def Is_A_She(self):
    #     return self.gender


    def Is_Gender(self):
        if self.gender:
            return True  #__male__#
        else:
            return False  #__female__#
        

    def To_Present(self):
        if self.Is_Gender():    
            if self.Is_Adult():
                print(self.first_name, self.nick_name, "est un adulte de", #__man__#
                      int(self.age), "ans.")
            else: 
                print(self.first_name, self.nick_name, "est un enfant de", #__boy__#
                      int(self.age), "ans.")
        else:                   
            if self.Is_Adult():
                      print(self.first_name, self.nick_name, "est une adulte de", #__woman__#
                            int(self.age), "ans.")
            else:
                print(self.first_name, self.nick_name, "est une enfant de", #__girl__#
                      int(self.age), "ans.")
