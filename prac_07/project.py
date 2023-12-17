import datetime


class Project:
    def __init__(self, name, start_date, priority=int, cost_estimate=float, completion_percentage=int):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}, start:{self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, " \
               f"completion: {self.completion_percentage}% "

    def __lt__(self, other):
        return self.priority < other.priority

    def is_completed(self):
        if self.completion_percentage == 100:
            return True
        else:
            return False
