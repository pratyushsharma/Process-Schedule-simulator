import bisect

class FCFS :
    def __init__(self):
        self.contextSwitch = 0
        self.presentJob = 0

    def schedule(self, ready, completed, responded, clock):
        if len(ready) > 0:
            nextJob = ready[0]
            if nextJob != self.presentJob:
                clock.tock(self.contextSwitch)
            nextJob.tick(clock)
            self.presentJob = nextJob
            if nextJob.status == 2:
                nextJob.status =4
                responded.append(nextJob)

            if nextJob.status == 1:
                ready.remove(nextJob)
                completed.append(nextJob)

            if nextJob.status == 3:
                ready.remove(nextJob)
                completed.append(nextJob)
                responded.append(nextJob)



class round_robin :
    def __init__(self):
        self.contextSwitch = 0
        self.presentJob = 0
        self.round = 5
        self.robin = self.round
        self.index=0

    def schedule(self, ready, completed, responded, clock):
        if len(ready) > 0:
            if self.robin==0:
                self.index=(self.index+1)%len(ready)
                self.robin = self.round

            nextJob = ready[self.index]
            if nextJob != self.presentJob:
                clock.tock(self.contextSwitch)
                self.robin = self.round
            nextJob.tick(clock)


            self.presentJob = nextJob

            if nextJob.status == 2:
                nextJob.status =4
                responded.append(nextJob)

            if nextJob.status == 1:
                ready.remove(nextJob)
                completed.append(nextJob)

            if nextJob.status == 3:
                ready.remove(nextJob)
                completed.append(nextJob)
                responded.append(nextJob)

            self.robin-=1

def comp(a):
        return a.left

class SJF :
    def __init__(self):
        self.contextSwitch = 0
        self.presentJob = 0

    

        

    def schedule(self, ready, completed, responded, clock):
        if len(ready) > 0:
            minimum = ready[0]

            for job in ready:
                if job.left<minimum.left:
                    minimum=job


            nextJob = minimum

            # nextJob = min(ready,key=comp)
            


            if nextJob != self.presentJob:
                clock.tock(self.contextSwitch)

            nextJob.tick(clock)


            self.presentJob = nextJob

            if nextJob.status == 2:
                nextJob.status =4
                responded.append(nextJob)

            if nextJob.status == 1:
                ready.remove(nextJob)
                completed.append(nextJob)

            if nextJob.status == 3:
                ready.remove(nextJob)
                completed.append(nextJob)
                responded.append(nextJob)





