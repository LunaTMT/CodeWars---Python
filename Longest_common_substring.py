


def longestCommonSS(strs):
        
        inter = set(strs[0])
        for item in strs:
            inter = inter & set(item)

        if not inter:
            return ""

        if len(strs) == 1:
            return strs[0]
        
        valid = []

        for letter in inter:
            i = 1
            indexs = [item.index(letter) for item in strs]

            while True:
                slices = [item[indexs[idx] : indexs[idx] + i] for idx, item in enumerate(strs)]

                if len((set(slices))) != 1 or i > max(strs, key=len):
                    if i >= 2:
                        valid.append(slices[0][:-1])
                    break
                i += 1
        return max(valid, key=len)

if __name__ == "__main__":
    strs = ["reflower","flow","flight"]
    longestCommonPrefix(strs)
