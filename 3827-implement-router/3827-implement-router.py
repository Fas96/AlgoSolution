class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = collections.deque()
        self.packet_set = set()
        self.dest_to_timestamps = {}

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.packet_set:
            return False

        if len(self.queue) == self.memoryLimit:
            oldest = self.queue.popleft()
            self.packet_set.remove(oldest)
            old_dest = oldest[1]
            old_timestamp = oldest[2]
            ts_list = self.dest_to_timestamps.get(old_dest, [])
            index = bisect.bisect_left(ts_list, old_timestamp)
            if index < len(ts_list) and ts_list[index] == old_timestamp:
                ts_list.pop(index)
            if not ts_list:
                del self.dest_to_timestamps[old_dest]

        self.queue.append(packet)
        self.packet_set.add(packet)
        if destination not in self.dest_to_timestamps:
            self.dest_to_timestamps[destination] = [timestamp]
        else:
            bisect.insort(self.dest_to_timestamps[destination], timestamp)
        
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []

        packet = self.queue.popleft()
        self.packet_set.remove(packet)
        source, destination, timestamp = packet

        ts_list = self.dest_to_timestamps.get(destination, [])
        index = bisect.bisect_left(ts_list, timestamp)
        if index < len(ts_list) and ts_list[index] == timestamp:
            ts_list.pop(index)
        if not ts_list:
            del self.dest_to_timestamps[destination]
        
        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dest_to_timestamps:
            return 0

        ts_list = self.dest_to_timestamps[destination]
        left = bisect.bisect_left(ts_list, startTime)
        right = bisect.bisect_right(ts_list, endTime)
        return right - left


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)