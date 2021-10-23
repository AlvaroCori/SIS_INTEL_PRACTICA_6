from Domain import Domain
class Speaker:
    def __init__(self, domains,is_international):
        self.domains = domains
        self.isInternational = is_international
        self.same_schedule = []
        self.assigneds = []
    def __lt__(self, other):
        return len(self.domains) < len(other.domains)
    def is_same_schedule(self, speaker):
        for ext in speaker.domains:
            for int in self.domains:
                if (ext.get_format() == int.get_format()):
                    return True
        return False
    def connect_with_schedule(self, speaker):
        if (self.is_same_schedule(speaker)):
            speaker.same_schedule.append(self)
            self.same_schedule.append(speaker)
    
    def aggregate_assigned(self, domain):
        self.assigneds.append(domain)

    def delete_domain(self, domain):
        if (domain in self.domains):
            self.domains.remove(domain)

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

    def is_consistent(self, value):
        #print(self.have_cosecutive_hours(self.assigneds+[value]))
        #print(value.get_format())
        return self.have_cosecutive_hours(self.assigneds+[value])
    
    
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