"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""

def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    # dic = {}
    # for word in strs:
    #     sotrted_word = "".join(sorted(word))

    #     if sotrted_word not in dic:
    #         dic[sotrted_word] = [word]
    #     else:
    #         dic[sotrted_word] += [word]
    
    # return dic.values() 

    hashmap = {}

    for word in strs:
        sortedWord = "".join(sorted(word))

        if sortedWord not in hashmap:
            hashmap[sortedWord] = [word]
        else:
            hashmap[sortedWord] += [word]
        
    return hashmap.values()
