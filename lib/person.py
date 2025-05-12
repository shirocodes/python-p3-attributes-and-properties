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
    def __init__(self, name = 'Shiro', job = 'Software engineer'):
        self._name = None  # Placeholder before setter
        self._job = None   # Placeholder before setter
        self.name = name   # Will trigger setter validation
        self.job = job     # Will trigger setter validation

    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1<= len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be string between 1 and 25 characters.")
    
    @property
    def job(self):
        return self._job
    
    @job.setter
    def job(self, value):
        if value in APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")

user = Person('User', 'doctor')
print(user.name)
print(user.job)

        
