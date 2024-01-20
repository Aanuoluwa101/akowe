from officiator import Officiator
from service import Service

friday = Service("weekday", "12-01-2023")
sunday = Service("sunday", "14-01-2023")

conductor1 = Officiator(name="John", 
                        rank=1, 
                        can_conduct=True,
                        can_read=True, 
                        can_preach=True, 
                        on_weekday=True,
                        on_sunday=True, 
                        enforcements=[])

conductor2 = Officiator(name="Mercy", 
                        rank=2, 
                        can_conduct=True,
                        can_read=True, 
                        can_preach=True, 
                        on_weekday=True,
                        on_sunday=True, 
                        enforcements=[])

conductor3 = Officiator(name="Jude", 
                        rank=3, 
                        can_conduct=True,
                        can_read=True, 
                        can_preach=True, 
                        on_weekday=True,
                        on_sunday=True, 
                        enforcements=[])

conductor4= Officiator(name="Joshua", 
                        rank=4, 
                        can_conduct=True,
                        can_read=True, 
                        can_preach=True, 
                        on_weekday=True,
                        on_sunday=True, 
                        enforcements=[])

#["Jerry", "Ayo", "Wisdom", "King", "Femi", "Ola", "Ini"]
all = [conductor1, conductor2, conductor3, conductor4]
conductors = [condcutor for condcutor in all if condcutor.can_conduct]
readers = [reader for reader in all if reader.can_read]
preachers = [preacher for preacher in all if preacher.can_preach]

    # conduct_weekday = []
    # conduct_all = []

    # read_sunday = []
    # read_weekday = []
    # read_all = []

    # preach_sunday = []
    # preach_weekday = []
    # preach_all = []

if __name__ == "__main__":
    print(conductor1)

   

    