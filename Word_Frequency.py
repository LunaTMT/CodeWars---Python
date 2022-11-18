import pandas as pd
import re

def top_3_words(text):
    x = re.findall(r"'?\b[a-z0-9']+\b'?", text)
    
    if x == []:
      return []
    else:
      data = pd.Series(x)
      return(data.value_counts().keys().tolist())[:3]


if __name__ == "__main__":
    top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
        mind, there lived not long since one of those gentlemen that keep a lance
        in the lance-rack, an old buckler, a lean hack, and a greyhound for
        coursing. An olla of rather more beef than mutton, a salad on most
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
        on Sundays, made away with three-quarters of his income.""")        #, ["a", "of", "on"])

    top_3_words("a a a  b  c c  d d d d  e e e e e")                    #, ["e", "d", "a"])
    top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")#, ["e", "ddd", "aa"])
    top_3_words("  //wont won't won't ")                                #, ["won't", "wont"])
    top_3_words("  , e   .. ")                                          #, ["e"])
    top_3_words("  ...  ")                                              #, [])
    top_3_words("  '  ")                                                #, [])
    top_3_words("  '''  ")                                              #, [])