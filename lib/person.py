#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name= 'Unknown', job = 'Unknown' ):
        self._name= None
        self._job= None
        self.name= name
        self.job= job

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance (value, str) and 1 <= len(value) <= 25:
            self._name= value.title()
        else:
            print('Name must be string between 1 and 25 characters.')
    @property
    def job(self):
        return self._job
    @job.setter
    def job(self, value):
        if value in APPROVED_JOBS:
            self._job= value
        else:
            print('Job must be in list of approved jobs.')    

#Example usage:
person1 = Person("john doe", "ITC")
print(person1.name)  # Output: John Doe
print(person1.job)   # Output: ITC

person2 = Person("a" * 26, "Invalid Job")  # Name too long and invalid job
# Output: Name must be string between 1 and 25 characters.
# Output: Job must be in list of approved jobs.
print(person2.name)  # Output: None
print(person2.job)   # Output: None

person3 = Person("Jane", "Customer Service")
print(person3.name)  # Output: Jane
print(person3.job)   # Output: Customer Service