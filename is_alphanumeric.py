import regex as re
def alphanumeric(password):
    pattern = re.match(r'^[a-zA-Z0-9_]+$', password) 
    return True if pattern else False

if __name__ == "__main__":
    alphanumeric("hello world_") #F
    alphanumeric("PassW0rd") #T
    alphanumeric("     ") #F

