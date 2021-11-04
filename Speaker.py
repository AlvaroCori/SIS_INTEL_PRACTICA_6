from Domain import Domain
class Speaker:
    def __init__(self, domains,is_international, name):
        self.domains = domains
        self.isInternational = is_international
        self.name = name
        self.same_schedule = []
        self.assigneds = []
    def __lt__(self, other):
        return len(self.assigneds) < len(other.assigneds)

    def print_domains(self):
        for d in self.domains:
                print(d.get_format())
    def print_assigneds(self):
        for d in self.assigneds:
                print(d.get_format())
    def exist_domain_context(self, domain,level):
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
    def limit_speeches(self, domains):
        return len(domains) <= 5
    def is_consistent(self, value):
        #horario siguiente a uno asignado
        #mismo horario otro speaker
        #print("is_consist", value.get_format())
        #print(self.wasnt_assigned(value) , self.have_cosecutive_hours(self.assigneds+[value]), self.domain_wasnt_assigned(value))
        return self.wasnt_assigned(value) and self.have_cosecutive_hours(self.assigneds+[value])  and self.domain_wasnt_assigned(value) and self.limit_speeches(self.assigneds+[value])

    def is_assigned_completed(self):
        return self.have_cosecutive_hours(self.assigneds) and self.limit_speeches(self.assigneds)

