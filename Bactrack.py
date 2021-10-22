from queue import PriorityQueue
import copy

def forward_checking(speaker, domain):
    speaker.domain = [domain]
    for neighbor in speaker.same_schedule:
        neighbor.delete_domain(domain)


def MRV(speakers):
    ordered_valuables = PriorityQueue()
    for speaker in speakers:
        ordered_valuables.put(speaker)
    return ordered_valuables.get()

def least_constrained_value(speaker, speakers):
    all_consistent_values = PriorityQueue()
    for v in speaker.domains:
        temp_speakers = copy.deepcopy(speakers)
        forward_checking(speaker, v)
        consist_values = 0
        for n in speaker.same_schedule:
            consist_values += len(n.domains)
        all_consistent_values.put((consist_values,v))
        speakers = temp_speakers
    request = list(map(lambda x: x[1],reversed(all_consistent_values.queue)))
    return request




def backtrack(speakers, weight, domains):
    if (speakers.assigned_complete()):
        return speakers
    return []
    '''
    
    speaker = MRV(speakers.speakers)
    speakers_ordered = least_constrained_value(speaker,speakers)
    delta = 1
    for value in list(speakers_ordered):
        delta *= 1#function_weight(countries)
        if (delta == 0):
            continue
        forward_checking(speaker,value)
        request = backtrack(speakers,weight*delta,domains)
    
    delta = 1
    for value in country.domains:
        #delta *= function_weight(countries)
        if (delta == 0):
            continue
        forward_checking(country,value)
        request = backtrack(countries,weight*delta,domains)
        #restore_values(country,value)
    return request
    '''
    return speakers

'''
countries_name = ["A","B","C","D"]
conexions = [("A","B"),("B","C"),("C","D"),("D","A")]
domains = ["R","G","B"]
countries = variables_class(countries_name,conexions,domains)
backtrack(countries, domains)
'''
#Priority Queue
#https://docs.python.org/3/library/queue.html 

def arc_consistency(country, domain):
    country.domain = [domain]# se queda solo con su color
    for neighbor in country.neighbor:#todos los vecinos
        neighbor.delete_domain(domain)
        if (len(neighbor.domains) == 1):
            arc_consistency(neighbor, neighbor.domains[0])
        if (len(neighbor.domains) == 0):
            return False
    return True