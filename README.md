# Project description
Law Maker is a Django app that lets initiators to create initiative, which is reviewed later by committees and either accepted or sent for revision back to the initiator. 
An initiative can be submitted only if it had collected enough sign during the petition. 
Petition has creation date and date when it was closed (handed over with initiative to committee to review).

# Entities

![law_maker](https://user-images.githubusercontent.com/5889549/103238718-329a8500-4954-11eb-8866-f1c87f57cdd4.jpg)

Initiative: status, title, description, edition,FK initiator, FK assigned committee for review

Initiator: Name, Surname

Committee: Name, Surname

Petition: FK initiative, sign count (method), date created, date closed

Signature: FK petition, voters name & surname

# Logic
Initiator can create initiatives and start petitions.
Voters get link and vote once for a petition. (not being checked for recurring votes in scope of this project).
Committee can review title, description and petition for the initiative.
