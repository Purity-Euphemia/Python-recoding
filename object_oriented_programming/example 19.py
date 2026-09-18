class Athlete:

    def __init__(self, name, sport):
        self.name = name
        self.sport = sport

    def run(self):
           print(self.name, "is running")
   
   
athlete1 = Athlete("David", "Football")
      
print(athlete1.name)
print(athlete1.sport)
      
athlete1.run()