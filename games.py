#Games module

class Player(object):
    """A player for a game"""
    def __init__(self,name,score = 0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = ""
        rep += self.name + "\t" + str(self.score)
        return rep

    def ask_yes_no(question):
        """Ask a yes or no question"""
        response = None
        while response in ("y","n"):
            response = raw_input(question).lower()
            return response

    def ask_number(question,low,high):
        """Ask for a number within a range"""
        response = None
        while respones not in range(low,high):
            response = int(raw_input(question))
            return reponse

if __name__ == "__main__":
    print "You ran this module directly and did not import it"
    raw_input("\n\nPress the enter key to exit")
    
