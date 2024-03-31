import datetime
import json


class Activity:

    def __init__(self, type):
        self.type = type
        self.date = datetime.datetime.today()

    def to_dict(self):
        return {
            "activity": {
                "type": self.type,
                "date": self.date.isoformat(),
            }
        }

    def saveActivity(self):
        with open("data/data/activity.json", 'r') as mon_fichier:
            activity_data = json.load(mon_fichier)

        activity_data.append(self.to_dict())
        file_path = f"data/data/activity.json"
        with open(file_path, 'w') as file:
            json.dump(activity_data, file)
