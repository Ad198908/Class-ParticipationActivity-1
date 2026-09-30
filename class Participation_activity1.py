"""
Program name: class participation activity 1
Author: Adhanet Gebretensay
Purpuse : modifid dictionary to class
Date: 09/30/2026

"""






class participation_Activity:
    def __init__(self):
           
            self.name = "Adhanet"
            self.favorite_color = "pink"
            self.favorite_planet ="Jupiter"
            self.other_fun_fact = "I like listening music"

    def display_information(self):
             information = {
              "name": self.name,
              "favorite_color": self.favorite_color,
              "favorite_planet": self.favorite_planet,
              "other_fun_fact": self.other_fun_fact,
             }

             for key,value in information.items():
                   print(f"{key}: {value}")

activity = participation_Activity()
activity.display_information()