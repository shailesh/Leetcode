class UndergroundSystem:
    
    """
    Approach: keep 2 dicts

a dict of userid -> (stationname , starttime)
a dict of (startstation, endstation) -> (totaltimesofar, numberofrides)
We will keep a running tally of all the times for station-to-station, and the number of rides whenever we checkOut() == O(1)

Then when we getAverageTime() we can calculate the average on the fly [0] / [1] == O(1)
    """

    def __init__(self):
        self.dct=dict()
        self.time=dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.dct[id]=(stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start,time=self.dct[id]
        if (start,stationName) in self.time:
            total,count=self.time[(start,stationName)]
            self.time[(start,stationName)]=(total+t-time,count+1)
        else:
            self.time[(start,stationName)]=(t-time,1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total,count=self.time[(startStation,endStation)]
        return total/count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)