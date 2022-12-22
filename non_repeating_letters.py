import pandas as pd

def first_non_repeating_letter(string):
    if not string:
        return ''
    print(string)
    
    try:
        letters = [letter for letter in string.lower()]
        data = pd.Series(letters)
        freq = data.value_counts()
        print(freq)
        return freq[freq == 1].index[0]
    except:
        return 1


if __name__ == "__main__":
    #first_non_repeating_letter('a') #, 'a')
    first_non_repeating_letter('abba')  #, ''
    first_non_repeating_letter('hello world, eh?')  #, 'w')
    first_non_repeating_letter('stress')    # 't')
    first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!')