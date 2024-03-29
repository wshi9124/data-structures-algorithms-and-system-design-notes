"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
"""

def ladderLength(self, beginWord, endWord, wordList):
    # Create a set of words for faster lookup
    wordSet = set(wordList)

    if endWord not in wordList:
        return 0
    
    q = collections.deque([(beginWord,1)])
    visit = set()

    while q:
        word, level = q.popleft()

        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                # Skip if the character is the same as in the original word
                if c == word[i]:
                    continue
                newWord = word[:i] + c + word[i+1:]
                if newWord in wordSet and newWord not in visit:
                    if newWord == endWord:
                        return level + 1
                    q.append((newWord, level + 1))
                    visit.add(newWord)
    return 0

    # #BFS
    # #n**2 * m time complexity

    # if endWord not in wordList:
    #     return 0

    # # dictionary where if you insert a new value for the first time, the default value will be an empty list (adjacentcy list)
    # nei = collections.defaultdict(list)
    # wordList.append(beginWord)

    # for word in wordList:
    #     for j in range(len(word)):
    #         pattern = word[:j] + "*" + word[j+1:]
    #         nei[pattern].append(word)
        

    # visit = set([beginWord])
    # q = collections.deque([beginWord])

    # result = 1
    # while q:
    #     for i in range(len(q)):
    #         word = q.popleft()
    #         if word == endWord:
    #             return result
    #         for j in range(len(word)):
    #             pattern = word[:j] + "*" + word[j+1:]
    #             for neiWord in nei[pattern]:
    #                 if neiWord not in visit:
    #                     visit.add(neiWord)
    #                     q.append(neiWord)
    #     result += 1
    # return 0
                