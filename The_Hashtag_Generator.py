def generate_hashtag(s):
    if s == "":
        return False
    string = "#"
    for el in s.lower().split():
        string += el.capitalize()
    return False if len(string) > 140 else string
