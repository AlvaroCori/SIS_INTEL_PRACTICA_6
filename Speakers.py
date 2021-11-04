from Speaker import Speaker
from Domain import Domain
import numpy as np
import copy
class Speakers:  
    def __init__(self,domains):
        self.speakers = []
        self.domains = domains
        self.assigneds = [False for i in range(len(domains))]
    def print_domains_and_assigneds(self):
        i = 0
        for domain in self.domains:
            print(domain.get_format(), self.assigneds[i])
            i = i + 1 
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
    def assign_schedule(self, speaker, domain):
        for s in self.speakers:
            if (speaker == s):
                i = 0
                for d in self.domains:
                    if (d.get_format() == domain.get_format()):
                        break
                    i = i + 1
                self.assigneds[i] = True
                return True 
        return False

    def yet_assigned(self,value):
        i = 0
        for domain in self.domains:
             if (domain.get_format() == value.get_format()):
                 return self.assigneds[i]
             i = i + 1   
    
    def international_in_different_schedule(self, value, speaker):
        request = True
        if (speaker.isInternational):
            for s in self.speakers:
                if (s.name == speaker.name):
                    continue
                if (s.isInternational):
                    for domain in s.assigneds:
                        if (domain.get_schedule() == value.get_schedule()):
                            return False
                            
        return request

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
    
    def comprobate_domain_avalaible(self, domain,level):
        count = 0
        
            
        for speaker in self.speakers:
            #if (domain.get_format() == "martes-9-Seguridad Informatica"):
                #speaker.print_assigneds()
                #print("domain", domain.get_format(),speaker.name)
                #print(speaker.exist_domain_context(domain))
                #print(speaker.is_consistent(domain))
            if (speaker.exist_domain_context(domain,level) and speaker.is_consistent(domain)):
                count = count + 1
     
        #if (domain.get_format() == "martes-9-Seguridad Informatica"):
        #    print("Ssssssss", count)
        return count >= 1

    def assigned_complete(self,level):
            request = True
            for speaker in self.speakers:
                if (speaker.is_assigned_completed()):
                    continue
                else:
                    request = False
                    break
            if (request == False):
                return False
            i = 0
            for a in self.assigneds.copy():

                if (a):
                    i = i + 1
                    continue
                else:
                    if (self.comprobate_domain_avalaible(self.domains[i],level)==False):
                        self.assigneds[i] = True
                i = i + 1
            for request in self.assigneds:
                if (request):
                    continue
                else:
                    request = False
                    break
            return request


'''
                #request = self.have_cosecutive_hours(speaker.assigneds)
                if (request == False):
                    return request
                request = speaker.assigneds != []
                if (request == False):
                    return request
            #    request = request and speaker.assigned_complete()
'''
