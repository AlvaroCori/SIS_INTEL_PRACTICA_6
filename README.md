# SIS_INTEL_PRACTICA_6
## Alvaro Bryan Cori Sanchez
## Practice 6 - PSSR - Search of Backtracking with constraints.

PSSR
## Description Of Problem

In this PSSR we use algorithms of backtracking search, we will search a combination of variables with domains that satisfy a Serie of constraining’s, the algorithm is util when the nodes must to obedience some conditions and the conjunct of conditions make the graph a system of constraining that need be verified with care because we can get a Serie of conditions with bad results because some nodes cannot get a domain.
The career of Systems Engineering of the Bolivian Catholic University organizes every year an event that
lasts a whole week where he invites national and international speakers to give talks on topics
interesting and relevant in the area of informatics.
The areas are: 
_ Computer Security (Seguridad Informatica)
 _ Software Engineering (Ingenieria De Software)
 _ Artificial Intelligence (Inteligencia Artificial)
The talks in the three areas are held in parallel.
The talks are from Monday to Friday, from 9 to 12 and from 15 to 18 hours.
The Conditions are:
_ The speakers chose his schedules.
_ Two speakers can’t take the same hour and day for an area but they can if the area is different In the same hour and day.
_ A speaker only can give 5 speeches.
_ Not always
_ Two international speakers can’t talk the same time although they give different areas.
## Description Of the Solution


## Graph Solution
![model_graph](https://github.com/AlvaroCori/SIS_INTEL_PRACTICA_6/blob/main/img/modelo_grafo.png)
## Own Elaboration
The problem can solve with a graph of speakers where the speakers are nodes and the edge are the clash of hour and day into two speakers.
I choose this form because many conditions need to know who speaker schedule fall in inconsistency by other schedule speaker.


#### Classes used in this practice.
## Domain Solution
![domain](https://github.com/AlvaroCori/SIS_INTEL_PRACTICA_6/blob/main/img/domain.png)
#### Own Elaboration
The domain is like a number or an identity for every speech. If we see a speech like a 3D the vectors are (hour, day, area). Well, if we reunite these values, we can assign at the variables the values that they will take in the week of the event. 
_ If we compare the hour, day and area like a unique value we can compare this in the schedule of week and the schedule of a speaker.
_ The form of a domain could be a dictionary but I need an intelligent object that have method to compare the attributes.
## Variable Solution, Speaker
![speaker](https://github.com/AlvaroCori/SIS_INTEL_PRACTICA_6/blob/main/img/speaker.png)
#### Own Elaboration
The speaker have a name for identify who will realize the speech, the speaker have his domains because the speaker choose what days can adjust his times, also they have a Boolean if the speaker came from another country, also every speaker have a array of reference to other speakers that have at least one hour in both schedules in the same day (see the Graph Solution) and every speaker have a array of domains assigned that contain the hour, day and area that the speaker will realize, this values are unique and cannot be replied in other speaker.
## Manager of the graph, speakers and domains
![speakers](https://github.com/AlvaroCori/SIS_INTEL_PRACTICA_6/blob/main/img/speakers.png)
#### Own Elaboration
The speakers is a class that contain all variables or speakers of the event, also have all the domains or the horary of all speech of the event. The domains in the speakers are different than the domains of every speaker. Each domain of a speaker can be in domains of the speakers but Each domain of speakers don’t always be in the domains of a singulary speaker. The assigneds are an array of Booleans that mark if the domain was assigned. The domains and the assigneds mark if all the programation of the event is consistency.
Exist three forms to mark an assigned domain in speakers.

1.	There is no speaker who can at that time of day.
2.	The domain was assigned an one speaker and is consistency.
3.	A speaker can give a speech in that domain but is not consistent with other schedules or speakers.  


We apply a backtrack solution using:

Forward Checking .- This algorithm assigns each speaker its unique domain and removes the domain of neighboring speakers who no longer need it.

MRV .- The algorithm sorts from higher to lower the speakers that will be assigned based on the number of domains that were assigned.

Least constrained value .- The algorithm does is assign a domain to a speaker and count the number of domains left in their speakers that share hours after they’ve removed the domain assigned to the speaker, the algorithm returns a list of the domain with more chances of being unique compared to the domains with more chances to return other value.

The restrictions are observed when we do the forward checking, first we ask if the speaker restrictions are met and then we allow you to assign permanently and move to the next speaker. The full assignment also monitors if all speakers are consistent.

The restrictions were resolved as follows: A candidate domain to be assigned to a speaker is asked the following restrictions. 

_ Asks if the domain was not assigned in other speakers.

 _ Asks if the domain does not have a consecutive schedule (there is no other domain one hour before or after).

_ Asks if the domain was not previously assigned. 

_ Ask if the allotted limit does not exceed 5 speeches.

_ Ask if at the same time and day there is only one international guest at that time. 

If the domain pass those restrictions, it is assigned if it is not, passed to the next domain and if there is no domain that can be assigned, returns an empty list and the back or backtrack is returned.


## Diagram of a simple solution
![case_assign](https://github.com/AlvaroCori/SIS_INTEL_PRACTICA_6/blob/main/img/algorithm_case.png)
#### Own Elaboration
## Assignation of the calendar during the execution of the algorithm
![case_assign_schedules](https://github.com/AlvaroCori/SIS_INTEL_PRACTICA_6/blob/main/img/algorithm_case_assigneds.png)
#### Own Elaboration


## Experiments And Results

## Conclusions
A restricted backtrack could be implemented by applying a graph of speakers connected to each other according to their schedules. Most of the restrictions could be implemented but the case of international speakers still needs to be correctly implemented. The backjumping algorithm can perhaps be used to optimize larger schedules but for this case in which at most last 5 days of the week the backtrack algorithm is fast enough to evaluate the situation and achieve a complete assignment by distributing the schedules between the speakers.

## Bibliography

### Paint of Windows 10
### Priority Queue
https://docs.python.org/3/library/queue.html 
### Difference between two lists
https://stackoverflow.com/questions/3462143/get-difference-between-two-lists
### Priority interation
https://stackoverflow.com/questions/25823905/how-to-iterate-over-a-priority-queue








