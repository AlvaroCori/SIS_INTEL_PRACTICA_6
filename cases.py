from Speaker import Speaker
from Speakers import Speakers
from Bactrack import *
from Domain import Domain
def init_domains_day(day, hours,areas):
    domains = []
    for hour in hours:
        for area in areas:
            domains.append(Domain(day, hour, area))
    return domains

#case 1 with a simple hour for each speaker
def case_1():
    s1 = Speaker(domains = init_domains_day("lunes",[9],["Seguridad Informatica"]),is_international=False,name = "Pepe")
    s2 = Speaker(domains = init_domains_day("lunes",[10],["Seguridad Informatica"]),is_international=False,name = "Lettie")
    domains = init_domains_day("lunes",[9,10],["Seguridad Informatica"])
    speakers = Speakers(domains)
    speakers.insert_speaker(s1)
    speakers.insert_speaker(s2)
    return speakers
#case 2 clash of speaker schedules and limits of a hour
def case_2():
    s1 = Speaker(domains = init_domains_day("lunes",[9,10,11],["Seguridad Informatica"]),is_international=False,name = "Pepe")
    s2 = Speaker(domains = init_domains_day("lunes",[10,11],["Seguridad Informatica"]),is_international=False,name = "Lettie")
    domains = init_domains_day("lunes",[9,10,11],["Seguridad Informatica"])
    speakers = Speakers(domains)
    speakers.insert_speaker(s1)
    speakers.insert_speaker(s2)
    return speakers
#case 3 limits of a hour and assign of schedule
def case_3():
    s1 = Speaker(domains = init_domains_day("lunes",[9,10,11,15,16],["Seguridad Informatica"]),is_international=False,name = "Pepe")
    s2 = Speaker(domains = init_domains_day("lunes",[10,17],["Seguridad Informatica"]),is_international=False,name = "Lettie")
    domains = init_domains_day("lunes",[9,10,11,15,16,17],["Seguridad Informatica"])
    speakers = Speakers(domains)
    speakers.insert_speaker(s1)
    speakers.insert_speaker(s2)
    return speakers

#case 4 limit of 5 speeches for each speaker

def case_4():
    domains_monday = init_domains_day("lunes",[9,10,11,15,16,17],["Seguridad Informatica"])
    domains_tuesday = init_domains_day("martes",[9,10,11,15,16,17],["Seguridad Informatica"]) 
    domains_wednesday = init_domains_day("miercoles",[9,10,11,15,16,17],["Seguridad Informatica"])
    s1 = Speaker(domains = domains_monday+ domains_tuesday,is_international=False,name = "Pepe")
    s2 = Speaker(domains = domains_tuesday + domains_wednesday,is_international=False,name = "Lettie")
    speakers = Speakers(domains_monday + domains_tuesday + domains_wednesday)
    speakers.insert_speaker(s1)
    speakers.insert_speaker(s2)
    return speakers
#Speakers of different areas with the same schedule
def case_5():
    s1 = Speaker(domains = init_domains_day("lunes",[9,10,11],["Seguridad Informatica"]),is_international=False,name = "Pepe")
    s2 = Speaker(domains = init_domains_day("lunes",[9,10,11],["Ingenieria de Software"]),is_international=False,name = "Lettie")
    domains = init_domains_day("lunes",[9,10,11],["Seguridad Informatica", "Ingenieria de Software"])
    speakers = Speakers(domains)
    speakers.insert_speaker(s1)
    speakers.insert_speaker(s2)
    return speakers
#7 speakers of different areas 
def case_6():
    s1 = Speaker(domains = init_domains_day("lunes",[9,10,11],["Seguridad Informatica"]),is_international=False,name = "Pepe")
    s2 = Speaker(domains = init_domains_day("lunes",[9,10,11],["Ingenieria de Software"]),is_international=False,name = "Lettie")
    s3 = Speaker(domains = init_domains_day("lunes",[9,10,11],["Inteligencia Artificial"]),is_international=False,name = "Tommy")
    s4 = Speaker(domains = init_domains_day("lunes",[9,10,11],["Seguridad Informatica"]),is_international=False,name = "Aitor")
    s5 = Speaker(domains = init_domains_day("lunes",[9,10,11],["Ingenieria de Software"]),is_international=False,name = "Selene")
    s6 = Speaker(domains = init_domains_day("lunes",[9,10,11],["Inteligencia Artificial"]),is_international=False,name = "Mana")
    s7 = Speaker(domains = init_domains_day("lunes",[9,10,11],["Ingenieria de Software"]),is_international=False,name = "Rico")
    domains = init_domains_day("lunes",[9,10,11],["Seguridad Informatica", "Ingenieria de Software","Inteligencia Artificial"])
    speakers = Speakers(domains)
    speakers.insert_speaker(s1)
    speakers.insert_speaker(s2)
    speakers.insert_speaker(s3)
    speakers.insert_speaker(s4)
    speakers.insert_speaker(s5)
    speakers.insert_speaker(s6)
    speakers.insert_speaker(s7)
    return speakers

def case_7():
    s1 = Speaker(domains = init_domains_day("lunes",[9,10,11],["Seguridad Informatica"]),is_international=False,name = "Pepe")
    s2 = Speaker(domains = init_domains_day("lunes",[9,10,11],["Seguridad Informatica"]),is_international=False,name = "Lettie")
    s3 = Speaker(domains = init_domains_day("lunes",[9,10,11],["Seguridad Informatica"]),is_international=False,name = "Lann")
    domains = init_domains_day("lunes",[9,10,11],["Seguridad Informatica"])
    speakers = Speakers(domains)
    speakers.insert_speaker(s1)
    speakers.insert_speaker(s2)
    speakers.insert_speaker(s3)
    return speakers