# Questions :--- 933. Number of Recent Calls

"""
Problem Statement:---

You have a RecentCounter class which counts the number of recent requests within a certain time frame.
Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that have happened in the inclusive range [t - 3000, t], that is, the new request plus every earlier request that is no more than 3000 milliseconds older.
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

Example 1:

Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]

Output
[null, 1, 2, 3, 3]

"""


# Code :----
class RecentCounter:
    def __init__(self):
        self.pings = []

    def ping(self, t):
        self.ping.append(t)
        count = 0

        for ping in self.ping:
            if ping >= t - 3000:
                count += 1

        return count
