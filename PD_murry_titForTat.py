import sys

def PD_murry_titForTat(myHist, oppHist, myScore, oppScore):
    if oppHist == []:
        return 'C'
    else:
        return oppHist[-1]

if __name__ == "__main__":
    sys.stderr.write("ERROR - this is not intended to be run stand-alone\n")
    exit(-1)