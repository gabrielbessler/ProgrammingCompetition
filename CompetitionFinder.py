import urllib.request
from bs4 import BeautifulSoup 

def main(): 
    ''' 
    1. HackerRank 
    ''' 
    websites = ["https://www.hackerrank.com/contests",
                "https://leetcode.com/contest/",
                "https://arena.topcoder.com/#/u/dashboard",
                "https://www.codeforces.com/contests"]
    for website in websites: 
        try:
            soup = BeautifulSoup(urllib.request.urlopen(website))
            # print(soup.prettify())
        except Exception as e: 
            print("Website: " + e)


if __name__ == "__main__": 
    main() 
