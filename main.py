from Speaker import Speaker
from Speakers import Speakers
from Bactrack import *
from Domain import Domain
domains = []

def init_domains_day(day, hours,areas):
    domains = []
    for hour in hours:
        for area in areas:
            domains.append(Domain(day, hour, area))
    return domains
domains = init_domains_day("lunes",[9,10,15,18,19,24],["Seguridad Informatica"])#init_domains_day("lunes",[9,10,11,15,16,17],["Seguridad Informatica"])
s1 = Speaker(init_domains_day("lunes",[9,15],["Seguridad Informatica"]), True, "CJ")
s2 = Speaker(init_domains_day("lunes",[9,10,18],["Seguridad Informatica"]), False, "AJ")
speakers = Speakers(domains)
speakers.insert_speaker(s1)
speakers.insert_speaker(s2)
request = backtrack(speakers, 0)



if (request == []):
    print(request)
else: 
    for i in request.speakers:
        print("==================")
        print(f"nombre: {i.name}")
        for j in i.domains:
            print(j.get_format())
        print("-----asignados---------")
        for j in i.assigneds:
            print(j.get_format())

'''
schedule = {
                "lunes":[9,10, 11,15,16,17], 
                "martes":[9,10, 11,15,16,17],
                "miercoles":[9,10, 11,15,16,17],
                "jueves":[9,10, 11,15,16,17],
                "viernes":[9,10, 11,15,16,17]
            }
areas = ["Seguridad Informatica","Ingenieria de Software","Inteligencia Artificial"]
is_international = True
s1 = Speaker(schedule,areas,is_international)
s2 = Speaker(schedule,areas,is_international)
s3 = Speaker(schedule,areas,is_international)
s4 = Speaker(schedule,areas,is_international)
s5 = Speaker(schedule,areas,is_international)
s6 = Speaker(schedule,areas,is_international)
domains = ["Seguridad Informatica","Ingenieria de Software","Inteligencia Artificial"]

speakers = Speakers()


speakers.insert_speaker(s1)
speakers.insert_speaker(s2)
speakers.insert_speaker(s2)
speakers.insert_speaker(s3)
speakers.insert_speaker(s4)
speakers.insert_speaker(s5)
speakers.insert_speaker(s6)
request = backtrack(speakers, 1, domains)

for speaker in request.speakers:
    print(speaker.domains)
'''
