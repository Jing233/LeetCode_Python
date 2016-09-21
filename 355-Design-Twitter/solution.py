import heapq

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = collections.defaultdict(list)
        self.followship = collections.defaultdict(set)
        self.tweetsCnt = 0
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweetsCnt += 1
        self.tweets[userId].append([tweetId, self.tweetsCnt])

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        recentTweets = []
        users = [userId] + list(self.followship.get(userId, set()))
        topK = 10
        
        for user in users:
            for userTweet in self.tweets.get(user, []):
                if len(recentTweets) < topK:
                    heapq.heappush(recentTweets, (userTweet[1], userTweet[0]))
                else:
                    if recentTweets[0][0] < userTweet[1]:
                        heapq.heappushpop(recentTweets, (userTweet[1], userTweet[0]))
        res = []
        while recentTweets:
            res.append(heapq.heappop(recentTweets)[1])
        return res[::-1]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId != followeeId:
            self.followship[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.followship:
            self.followship[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)