import re
import random
import clock
import process
import schedulers

class Simulator:
    def __init__(self):
        self.numProcesses = 0
        self.clock = clock.Clock()
        self.queue = []
        self.completed = []
        self.responded= []
        self.schedule = schedulers.SJF()
        self.start()

    def start(self):
        for i in range(10**6):
            self.round()
            self.clock.tock()
        self.end()

    def end(self):
        print ("Number Processes", self.numProcesses)
        averageComp=[a.end-a.issueTime for a in self.completed]
        averageRes=[a.response - a.issueTime for a in self.completed]
        averageWait=[a.end - a.issueTime - a.totalTime for a in self.completed]
        print ("Average Completion", float(sum(averageComp))/len(averageComp))
        print ("Average Response", float(sum(averageRes))/len(averageRes))
        print ("Waiting Time", float(sum(averageWait))/len(averageWait))
        print ("Number of Processes Completed", len(self.completed))
        print ("Number of Processes responded", len(self.responded))

        # print [(a.issueTime,a.response, a.end, a.totalTime) for a in self.completed]



    def round(self):
        # print self.clock.clock
        newProcesses = int(random.gauss(-1, 2))
        if newProcesses<0:
            newProcesses=0
        else:
            newProcesses=int(newProcesses)
            
        self.newJobs=[]
        
        for i in range(newProcesses):
            l = int(random.uniform(1, 100))
            r = int(random.uniform(1, l))
            job = process.Process(self.numProcesses ,self.clock.clock, r, l)
            self.newJobs.append(job)
            self.numProcesses += 1
        self.schedule.schedule(self.queue, self.completed,self.responded, self.clock, self.newJobs)


if __name__ == '__main__':
    sim=Simulator()


