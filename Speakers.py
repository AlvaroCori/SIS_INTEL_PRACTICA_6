from Speaker import Speaker
from Domain import Domain
import numpy as np

class Speakers:  
    def __init__(self):
        self.speakers = np.array([])
    def insert_speaker(self, speaker):
        #for s in self.speakers:
        #    s.connect_with_schedule(speaker)
        self.speakers = np.append(self.speakers, speaker)
    def have_cosecutive_hours(self, domains):
        dic = dict()
        for domain in domains:
            if (domain.day not in dic): 
                dic[domain.day] = []
            dic[domain.day].append(domains.hour)
        for day in dic:
            hours = sorted(dic[day])
            element = hours[0]
            for hour in hours[1:]:
                if (element + 1 <= hour):
                    return False
                else:
                    element = hour
        return True

                       
    def assigned_complete(self):
            request = True
            for speaker in self.speakers:
                request = self.have_cosecutive_hours(speaker.assigneds)
                request = speaker.assigneds != []
                if (request == False):
                    return request
            #    request = request and speaker.assigned_complete()
            return request
