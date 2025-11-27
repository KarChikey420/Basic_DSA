def groupAnagrams(strs):
        string_map=defaultdict(list)
        
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord("a")]+=1
            string_map[tuple(count)].append(s)
        return list(string_map.values())