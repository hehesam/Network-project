import random
from random import randint

class student:

    def get_ID(self):
        return str(randint(900000000, 999999999))

    def get_name(self):
        first_name = ["Liam", "Emma", "Charlotte", "Oliver", "Elijah", "James", "Benjamin", "Harper", "Levi",
                      "Elizabeth", "Daniel", "Sofia", "Mason", "Logan", "Layla", "John", "Joseph", "Lily", "Violet",
                      "Riley", "Isaac", "Stella", "Victoria", "Piper", "Peyton", "Sadie"]
        last_name = ["Levin", "Kennedy", "James", "Hayley", "Hayden", "Greer", "Everly", "Darcy", "Colby", "Alexander",
                     "Anderson", "Alder", "Bentley", "Beck", "Birk", "Blake", "Byron", "Carson", "Emerson", "Finley",
                     "Griffin", "Holden", "Hudson", "Jackson", "Kiefer", "Kingsley", "Landon", "Logan", "Marshall",
                     "Mercer", "Miller"]

        return random.choice(tuple(first_name)) + " " + random.choice(tuple(last_name))
    def get_score(self):
        return randint(13, 20)


