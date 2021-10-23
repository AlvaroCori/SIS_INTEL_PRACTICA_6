from queue import PriorityQueue
import copy

def forward_checking(speaker,domain):
    speaker.aggregate_assigned(domain)
    for next_speaker in speaker.same_schedule:
        next_speaker.delete_domain(domain)
    return True


def MRV(speakers):
    ordered_valuables = PriorityQueue()
    for speaker in speakers:
        ordered_valuables.put(speaker)

    return ordered_valuables.get()

def least_constrained_value(speaker, speakers):
    all_consistent_values = PriorityQueue()

    for domain in speaker.domains:
            temp_speakers = copy.deepcopy(speakers)
            forward_checking(speaker, domain)
            consist_values = 0
            for n in speaker.same_schedule:
                consist_values += len(n.domains)
            domain.consist_values = consist_values
            all_consistent_values.put(domain)   
            speakers = temp_speakers
    #for i in all_consistent_values.queue:
    #    print(i.consist_values)
    request = reversed(all_consistent_values.queue)
    return list(request)

def order_domains(domains):
    return []
def function_consistent(value, speaker):
    request = speaker.is_consistent(value)
    return request

def backtrack(speakers_assigneds, speakers):
    request = []
    if (speakers_assigneds.assigned_complete() and len(speakers_assigneds.speakers)==2):
        return speakers_assigneds
    speakers_copy = copy.deepcopy(speakers)
    speaker = MRV(speakers_copy.speakers)
    values = least_constrained_value(speaker,speakers_copy)
    speaker = MRV(speakers.speakers)
    for value in values:
        if (function_consistent(value, speaker)):
            speaker = speakers.pop(speaker)
            speakers_assigneds.insert_speaker(speaker)
            
            failure = forward_checking(speaker, value)
            request = backtrack(speakers_assigneds,speakers)
    return request

def backtrack1(speakers, weight, domains):
    request = []
    if (speakers.assigned_complete()):
        return speakers
    speaker = MRV(speakers.speakers)
    speakers_ordered = ordered_values(speaker.domains)#least_constrained_value(speaker,speakers)
    delta = 1
    
    for value in list(speakers_ordered):
        #print(value.day, value.hour)
        delta = delta * function_consistent(value, speaker)
        if (delta == 0):
            continue
        '''
        for i in speakers:
            print(i)
            for j in speakers.domains:
                print(j)
        '''
        forward_checking(speaker,value)
        request = backtrack(speakers,weight*delta,domains)
    return request
    '''
    
    
    
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