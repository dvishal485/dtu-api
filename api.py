from bs4 import BeautifulSoup
import urllib.request
from bs4.element import Tag

dtuUrl = 'http://dtu.ac.in/'


def dtu() -> object:
    '''
    Fetches information from DTU Official Website and returns the useful data as JSON String
    '''
    page = urllib.request.urlopen(dtuUrl)
    soup = BeautifulSoup(page.read(), "html.parser")
    title = soup.title.string
    marqueeLeft = soup.find(direction="up")
    sub = []
    impUpdates = []
    for data in marqueeLeft.find_all('a'):
        if data.text != None and not "»" in data.text:
            sub.append({
                "name": data.text.replace('»', '').strip(),
                "link": convert_link(data.get("href"))
            })
        else:
            if sub != []:
                impUpdates.append({
                    "name": text,
                    "sub_list": sub
                })
                sub = []
            text = data.text.replace('»', '').strip()
            if data.get("href") != None:
                impUpdates.append({
                    "name": text,
                    "link": convert_link(data.get("href"))
                })
    try:
        marqueeLeft = soup.find(direction="left")
        note = {
            "name": marqueeLeft.a.string.strip(),
            "link": convert_link(marqueeLeft.a.get("href"))
        }
    except:
        note = {
            "name": "Nothing new here",
            "link": "http://dtu.ac.in"
        }

    latestTab = soup.find_all("div", class_="latest_tab")

    latestNews = latest_tab_extractor(latestTab[0])
    notices = latest_tab_extractor(latestTab[1])
    jobs = latest_tab_extractor(latestTab[2])
    tenders = latest_tab_extractor(latestTab[3])
    firstYear = latest_tab_extractor(latestTab[4])
    registeration = latest_tab_extractor(latestTab[5])
    events = latest_tab_extractor(latestTab[6])

    finalResult = {
        "title": title,
        "note": note,
        "important_updates": impUpdates,
        "news": latestNews,
        "events": events,
        "notices": notices,
        "first_year_notices": firstYear,
        "registeration_schedule": registeration,
        "tenders": tenders,
        "jobs": jobs,
    }

    return finalResult


def convert_link(url: str) -> str:
    '''
    Converts relative URL String to exact URL string
    '''
    if url != None:
        return url.replace("./", dtuUrl)
    else:
        return None


def latest_tab_extractor(html_component: Tag) -> list:
    '''
    Converts the HTML string under latest_tab div
    from DTU Website into meaningful Array
    '''
    result = []
    try:
        item: Tag
        for item in html_component.find_all("li"):
            aTag = item.find_all("a")
            if len(aTag) > 1:
                sub = []
                i: Tag
                for i in aTag:
                    sub.append({
                        "name": str(i.get_text()).replace('||', '').strip(),
                        "link": convert_link(i.get("href"))
                    })
                if item.a.get("href") == None:
                    if item.h6.string == None and aTag[0].link == None:
                        name = aTag[0].get_text()
                        sub.pop(0)
                    else:
                        name = item.h6.string
                    result.append({
                        "name": name.strip(),
                        "sub_list": sub
                    })
                else:
                    for x in sub:
                        result.append(x)
            else:
                result.append({
                    "name": item.get_text().strip(),
                    "link": convert_link(item.a.get("href"))
                })
            if str(result[len(result)-1]).__contains__('view all'):
                result.pop()
                break
    except:
        if(len(result) == 0):
            result.append({
                "name": "End of results",
                "link": "http://dtu.ac.in/"
            })
    finally:
        return result
