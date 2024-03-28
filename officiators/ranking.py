#database only contains officiators, user details
#there's gonna be a general ranking that will contain rankings for all
#then each user will have a ranking file in their directory
#all ranks should be stored in the database but rankings of a particular user should be in files

ranks = [
            {"name": "Superior Evangelist", "Abbreviation": "Sup Evang", "weight": 10},
            {"name": "Senior Evangelist", "Abbreviation": "Snr. Evang", "weight": 8}
        ]  #this is what the frontend sends
import json

class Ranking:
    def __init__(self, user_id, ranks):
        self.user = user_id
        self.ranks = ranks

    def save(self):
        ranking_file = f"data/{self.user}/ranking.json"
        with open(ranking_file, "w") as json_file:
            json.dump(self.ranks, json_file, indent=2)
        
    #when we have created a ranking for a user and they have edited (or not), all we do is create this object and save it. 
            
if __name__ == "__main__":
    ranking = Ranking("asdfjkl", ranks)
    ranking.save()