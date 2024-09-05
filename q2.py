def merge(intervals):
    intervals.sort(key = lambda x:x[0])
    merged = [intervals[0]]

    for interval in intervals[1:]:
        last = merged[-1]

        if interval[0] <= last[1]:
            last[1] = max (last[0] , interval[1])
        else :
            merged.append(interval) 

    return merged 

intervals = [[1,3],[2,6],[8,10],[15,18]]  
merged_interval = merge(intervals)
print(merged_interval)       