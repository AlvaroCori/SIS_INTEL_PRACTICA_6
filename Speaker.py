class Speaker:
    def __init__(self, schedule, areas,is_international):
        self.schedule = schedule
        self.areas = areas
        self.isInternational = is_international
        self.assigneds = []
    
'''
class Speaker:
    def __init__(self, schedule, domains,is_international):
        self.schedule = schedule
        self.domains = domains
        self.isInternational = is_international
        self.same_schedule = []
    def __lt__(self, other):
        return len(self.domains) < len(other.domains)
    def assigned_complete(self):
        return self.same_schedule == []
    def is_same_schedule(self, speaker):
        for dic_ext in speaker.schedule:
            for dic_int in self.schedule:
                if (dic_ext != dic_int):
                    continue
                if (len(list(set(speaker.schedule[dic_ext]) & set(self.schedule[dic_int])))>0):
                    return True
        return False
    def connect_with_schedule(self, speaker):
        if (self.is_same_schedule(speaker)):
            speaker.same_schedule.append(self)
            self.same_schedule.append(speaker)
    def delete_domain(self, domain):
        if (domain in self.domains):
            self.domains.remove(domain)
'''
#Difference between two lists
#https://stackoverflow.com/questions/3462143/get-difference-between-two-lists
#Priority interation
#https://stackoverflow.com/questions/25823905/how-to-iterate-over-a-priority-queue