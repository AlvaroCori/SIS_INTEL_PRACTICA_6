from Domain import Domain
class Speaker:
    def __init__(self, domains,is_international):
        self.domains = domains
        self.isInternational = is_international
        self.same_schedule = []
        self.assigneds = []
    def __lt__(self, other):
        return len(self.domains) < len(other.domains)

    def print_domains(self):
        for d in self.domains:
                print(d.get_format())
    def print_assigneds(self):
        for d in self.assigneds:
                print(d.get_format())
    def exist_domain_context(self, domain):
        request = False
        for d in self.domains:
            if (domain.get_format() == d.get_format()):
                request = True
                return  request
        return request
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

    def disconnect_with_schedule(self, speaker):
        if (self.is_same_schedule(speaker)):
            speaker.same_schedule.remove(self)
            self.same_schedule.remove(speaker)

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
                if (element + 1 == hour or element -1 == hour):
                    return False
                else:
                    element = hour
        return True
    def different_assigneds(self, domain):
        for a in self.assigneds:
            if(domain.get_format() == a.get_format()):
                return False
        return True
    def domain_wasnt_assigned(self, domain):
        request = True
        #print("ssss",self.same_schedule)
        for speaker in self.same_schedule:
            request = False
            if (speaker.different_assigneds(domain)):
                return True
        return request
    def wasnt_assigned(self, value):
        for a in self.assigneds:
            if (a.get_format() == value.get_format()):
                return False
        return True
    def is_consistent(self, value):
        #horario siguiente a uno asignado
        #mismo horario otro speaker
        #print("is_consist", value.get_format())
        #print(self.wasnt_assigned(value) , self.have_cosecutive_hours(self.assigneds+[value]), self.domain_wasnt_assigned(value))
        return self.wasnt_assigned(value) and self.have_cosecutive_hours(self.assigneds+[value])  and self.domain_wasnt_assigned(value)

    def is_assigned_completed(self):
        return self.have_cosecutive_hours(self.assigneds)
    
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