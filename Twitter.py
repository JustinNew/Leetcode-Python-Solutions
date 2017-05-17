class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweet = []
        self.followed = {}

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweet.append((userId, tweetId))
        return

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        count = 10
        result = []
        for i in range(len(self.tweet)-1,-1,-1):
            (uId, tId) = self.tweet[i]
            if (userId in self.followed) and (uId in self.followed[userId]):
                result.append(tId)
                count -= 1
            elif uId == userId:
                result.append(tId)
                count -= 1
            if count == 0:
                return result
        return result
        
    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.followed:
            self.followed[followerId] = self.followed[followerId] | {followeeId} 
        else:
            self.followed[followerId] = {followeeId}
        return

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.followed:
            self.followed[followerId] -= {followeeId}
            return
        else:
            return

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
