# Project description
Law Maker is a Django app that lets initiators to create initiative, which is reviewed later by committees and either accepted or sent for revision back to the initiator. 
An initiative can be submitted only if it had collected enough sign during the petition. 
Petition has creation date and date when it was closed (handed over with initiative to committee to review).

# Entities

![law_maker (1)](https://user-images.githubusercontent.com/5889549/103239524-68406d80-4956-11eb-9d07-aa442f4524b7.jpg)

Initiative: status, title, description, edition,FK initiator, FK assigned committee for review

Initiator: Name, Surname

Committee: Name, Surname

Petition: FK initiative, sign count (method), date created, date closed

Signature: FK petition, voters name & surname

# Logic
Initiator can create initiatives and start petitions.
Voters get link and vote once for a petition. (not being checked for recurring votes in scope of this project).
Committee can review title, description and petition for the initiative.
