import random


class Process:

    def __init__(self, id, issueTime, responseTime, totalTime):
        self.id = id
        self.totalTime = totalTime
        self.issueTime = issueTime
        self.responseTime = responseTime
        self.left = totalTime
        self.completed = 0
        self.status = 0

    def tick(self, clock):
        self.completed += 1
        self.left -= 1
        if self.completed == self.responseTime:
            self.response = clock.clock
            self.status = 2
        if self.completed == self.totalTime:
            self.end = clock.clock
            self.status = 1
            if self.responseTime == self.totalTime:
                self.status = 3

    def __str__(self):
        return "%d and id:%d" % (self.left, self.id)
