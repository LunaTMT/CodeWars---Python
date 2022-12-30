
def format_duration(s):
    if s == 0:
        return 'now'

    year, s = divmod(s, (60 * 60 * 24 * 365))
    days, s = divmod(s, (60 * 60 * 24))
    hours, s =  divmod(s, (60 * 60))
    minutes, s = divmod(s, (60))
    seconds = s

    valids = list(map(str, [year, days, hours, minutes, seconds]))
    text = ["year", "day", "hour", "minute", "second"]
    check = [x for x in zip(valids, text) if x != "0"]      #conditional check and merge (zip) 
    valids =  list(filter(lambda x: x[0] != "0", check))    #filtering out all valid values (> 0)

    msg = ""
    valid_len = len(valids)
    
    for i, valid in enumerate(valids):
        merged = " ".join(valid)
        if i == valid_len-1 and valid_len != 1:
            msg = msg[:-2] + ' and '
        msg += merged + 's, ' if valid[0] != "1" else merged + ", "

    return msg[:-2]







if __name__ == "__main__":

    format_duration(1)     #"1 second")
    format_duration(62)    #"1 minute and 2 seconds")
    format_duration(120)   #"2 minutes")
    format_duration(3600)  #"1 hour")
    format_duration(3662)  #"1 hour, 1 minute and 2 seconds")

