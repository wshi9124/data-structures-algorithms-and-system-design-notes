"""
You are given a set of meeting start times and durations. 
You will determine if there is a meeting conflict, and also the number of conflicts, and total conflict time.
A conflict in this case is defined as a time overlap between two meeting.

For instance (assuming military time format 0000-2400), If:

-meeting A begins at 0800 and its duration is 45 mins
-meeting B begins at 0830 and its duration is 30 mins

Total conflict time is 15 mins. Slots are exclusive and not inclusive of the time. For instance, if meeting B began at 845, then there is no conflict
"""

def conflictInfo(meetings):
    times = []
    conflicts = 0
    totalMins = 0

    for m in meetings:
        time = m.split(",")
        start = int(time[0])
        duration = int(time[1])
        if not time or not duration or time < 0 or time >= 2400 or duration < 0 or duration > 90:
            return "error"
        end = start + ((duration // 60 * 100)) + duration % 60

        times.append([start, end])

    n = len(times)
    for i in range(n):
        start, end = times[i]
        for j in range(i+1, n):
            s, e = times[j]
            t = 0


    if conflicts:
        return "conflict", conflicts, totalMins
    else:
        return "good"