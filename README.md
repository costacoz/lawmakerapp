# Project description
Law Maker is a Django app that lets initiators to create initiative, which is reviewed later by committees and either accepted or sent for revision back to the initiator.\
An initiative can be submitted only if it had collected enough sign during the petition.\
Petition has creation date and date when it was closed (handed over with initiative to committee to review).

# Rules/restrictions (*configurable in admin panel)
* Petition should gather at least 10* signatures.
* Initiative can be reapplied up to 3* times
* One voter can vote only once per petition (non-configurable)
* Initiator cannot submit the same unchanged petition that was already submitted, it should contain changes to description and new petition.  (non-configurable)
* Petition can last 2* days. Petition is automatically closed either after 2 days or if petition gathered required amount of signatures.



# Entities

![law_maker (2)](https://user-images.githubusercontent.com/5889549/103284063-e9dddd00-49e2-11eb-8b8a-9b1c049ba8c5.jpg)

**Initiative**: status, title, description, edition,FK initiator, FK assigned committee for review

**Initiator**: Name, Surname

**Committee**: Name, Surname

**Petition**: FK initiative, sign count (method), date created, date closed

**Signature**: FK petition, voters name & surname

# Logic
**Initiator** can create initiatives and start petitions.\
**Voters** get link to the petition and vote only once for a petition.\
**Committee** can review initiative title, description and petition for the initiative.\
**Committee** can decline initiative, which passes it back to initiator with status declined and remaining count of permitted amount of resubmissions left.\
**Committee** can change status from declined to approved and vice versa.


## Views
### Initiator
**Initiatives index**\
**Create initiative**\
**Initiative details**
### Committee
**Assigned initiatives for review**\
**Initiative details**
### Voter
**Initiative details**\
**Petition details view**

# Project’s highlighted technology stack
* TDD (+ coverage.py usage to check code coverage)
* Numpy
* Pandas
* Django generic views
* Django 3.1




ToDo:
Insert video demo of using the systems views in logical manner (initiative-petition-committee-decline-edition-petition-committee-accept).
