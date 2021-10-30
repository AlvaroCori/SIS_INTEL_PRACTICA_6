from Speaker import Speaker
from Domain import Domain
import numpy as np
import copy
class Speakers:  
    def __init__(self,domains):
        self.speakers = []
        self.domains = domains
    def insert_speaker(self, speaker):
        for s in self.speakers:
            if (s == speaker):
                return
        for s in self.speakers:
            s.connect_with_schedule(speaker)
        self.speakers.append(speaker)
    def pop(self, speaker):
        if speaker in self.speakers:
            self.speakers.remove(speaker)     
            #for s in self.speakers:
            #    s.disconnect_with_schedule(speaker)
            return speaker
        else:
            return None
    def have_cosecutive_hours(self, domains):
        dic = dict()
        for domain in domains:
            if (domain.day not in dic): 
                dic[domain.day] = []
            dic[domain.day].append(domain.hour)
        for day in dic:
            hours = sorted(dic[day])
            element = hours[0]
            for hour in hours[1:]:
                if (element + 1 <= hour):
                    return False
                else:
                    element = hour
        return True
                
    def comprobate_domains(self):
        ls = []
        not_assigneds = []
        for speaker in self.speakers:
            ls = ls + speaker.assigneds    
        for domain in self.domains:
            res = True
            for assign in ls:
                if (assign.get_format() == domain.get_format()):
                    res = False
            if (res):
                not_assigneds.append(domain)
        
        for na in not_assigneds:
            for speaker in self.speakers:
                if (speaker.is_consistent(na)):
                    return True   
        return False
        
    def assigned_complete(self):
            request = True
            if (request == False):
                    return request
            for speaker in self.speakers:
                #request = self.have_cosecutive_hours(speaker.assigneds)
                if (request == False):
                    return request
                request = speaker.assigneds != []
                if (request == False):
                    return request
            #    request = request and speaker.assigned_complete()
            return request
