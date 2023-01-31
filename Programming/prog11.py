import requests
import re

def solve():
    answer = ""

    url = "https://www.hackthissite.org/missions/prog/11/"
    referer = "https://www.hackthissite.org/missions/programming/"

    cookies = {'HackThisSite' : 'your cookie'}
    session = requests.Session()
    session.headers.update({'referer' : referer})
    
    site = session.post(url, cookies = cookies)
    
    code = re.search("String: .*", site.text)[0].split()[1].strip('<br')
    shift = int(re.search("Shift: .*", site.text)[0].split()[1].strip("<br"))
    
    for d in re.findall("\d+", code):
        d = (int(d) - shift) % 127
        answer += chr(d)

    url = "https://www.hackthissite.org/missions/prog/11/index.php"
    payload = {'solution' : answer}    
    site = session.post(url, data = payload, cookies = cookies)

if __name__ == "__main__":
    solve()
