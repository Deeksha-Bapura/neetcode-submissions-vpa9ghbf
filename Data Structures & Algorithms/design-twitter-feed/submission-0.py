class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time,tweetId))
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.following[userId] | {userId}
        for u in users:
            for time, tweetId in self.tweets[u][-10:]:
                heapq.heappush(heap, (-time, tweetId))
        result = []
        for _ in range(min(10,len(heap))):
            result.append(heapq.heappop(heap)[1])
        return result
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
