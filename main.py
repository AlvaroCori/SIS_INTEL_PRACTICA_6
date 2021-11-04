from Speaker import Speaker
from Speakers import Speakers
from Bactrack import *
from Domain import Domain
from cases import *
domains = []


speakers = case_6()

request = backtrack(speakers, 0)



if (request == []):
    print(request)
else: 
    for i in request.speakers:
        print("=============================")
        print(f"nombre: {i.name}")
        print(f"horario:")
        for j in i.domains:
            print(j.get_format(),end=", ")
        print("-")
        print("-----asignados---------")
        for j in i.assigneds:
            print(j.get_format())
