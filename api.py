from functools import total_ordering
from typing import List
from bs4 import BeautifulSoup
import urllib.request
from bs4.element import Tag

dtuUrl = 'http://dtu.ac.in/'


def dtuMainWebpage(extended: bool = False) -> object:
    '''
    Fetches information from DTU Official Webpage and returns the useful data as JSON Object

    Argument -
        `extended` : bool (defaults `false`)
            If `True` returns the whole page information instead of just the main components.
            Useful when creating alternate version of webpage so need the webpage to be scraped entirely.
    '''
    page = urllib.request.urlopen(dtuUrl)
    soup = BeautifulSoup(page.read(), 'html.parser')
    title = soup.title.string

    # Extracting important updates from marquee in upward direction
    marqueeUp = soup.find(direction='up')
    sub = []
    impUpdates = []

    data: Tag
    for data in marqueeUp.find_all('a'):
        if data.text != None and not '»' in data.text:
            sub.append({
                'name': data.text.replace('»', '').strip(),
                'link': convert_link(data.get('href'))
            })
        else:
            if sub != []:
                impUpdates.append({
                    'name': text,
                    'sub_list': sub
                })
                sub = []
            text = data.text.replace('»', '').strip()
            if data.get('href') != None:
                impUpdates.append({
                    'name': text,
                    'link': convert_link(data.get('href'))
                })
    try:
        marqueeUp = soup.find(direction='left')
        note = {
            'name': marqueeUp.a.string.strip(),
            'link': convert_link(marqueeUp.a.get('href'))
        }
    except:
        note = {
            'name': 'Nothing new here',
            'link': 'http://dtu.ac.in'
        }

    # Extracting tabs of webpage containing information
    latestTab = soup.find_all('div', class_='latest_tab')

    latestNews = latest_tab_extractor(latestTab[0])
    notices = latest_tab_extractor(latestTab[1])
    jobs = latest_tab_extractor(latestTab[2])
    tenders = latest_tab_extractor(latestTab[3])
    firstYear = latest_tab_extractor(latestTab[4])
    registeration = latest_tab_extractor(latestTab[5])
    events = latest_tab_extractor(latestTab[6])

    # Extracting last updated
    bottomSection = soup.find('div', id='bottom_Section')
    lastUpdated = bottomSection.get_text().split(
        'Last updated :')[1].split('\n')[0].strip()
    if not extended:
        return {
            'title': title,
            'last_updated': lastUpdated,
            'note': note,
            'important_updates': impUpdates,
            'news': latestNews,
            'events': events,
            'notices': notices,
            'first_year_notices': firstYear,
            'registeration_schedule': registeration,
            'tenders': tenders,
            'jobs': jobs,
        }
    else:
        # Extracting Menu bar which contains sub-menus and redirecting links
        menu = []
        linkBar = soup.find('div', id='smoothmenu1').ul
        linkBarMenus = linkBar.find_all('li', recursive=False)
        i: Tag
        for i in linkBarMenus:
            menu.append(link_bar_extractor(i))

        # Extracting the slider displaying images from important moments
        showcase = []
        slider = soup.find('div', id='slider2')
        showcaseDiv = slider.find_all('div', class_='contentdiv')
        for i in showcaseDiv:
            try:
                showcase.append({
                    'name': i.get_text().replace('\n', '').strip(),
                    'image_link': convert_link(i.img.get('src'))
                })
            except:
                None

        # Extracting side menu (can be hardcoded as well as not changed with time)
        sidemenu = []
        wrapper = soup.find('div', id='wrapper_sec')
        sideMenuDivs = wrapper.find_all('div', class_='college_gallery')
        for i in sideMenuDivs:
            sideMenuDivArray = side_menu_extractor(i)
            sidemenu.extend(sideMenuDivArray)

        # Extracting top menu bar (can be hardcoded as well as not changed with time)
        topMenu = []
        topMenuList = wrapper.find('ul')
        for i in topMenuList.find_all('li'):
            name = i.get_text().replace('\n', '').strip()
            if name != '':
                topMenu.append({
                    'name': name,
                    'link': convert_link(i.a.get('href'))
                })

        return {'title': title,
                'last_updated': lastUpdated,
                'top_menu': topMenu,
                'menu': menu,
                'showcase': showcase,
                'side_menu': sidemenu,
                'note': note,
                'important_updates': impUpdates,
                'news': latestNews,
                'events': events,
                'notices': notices,
                'first_year_notices': firstYear,
                'registeration_schedule': registeration,
                'tenders': tenders,
                'jobs': jobs, }


def convert_link(url: str) -> str:
    '''
    Converts relative URL String of DTU Webpage to exact URL string
    '''
    if url != None:
        return url.replace('./', dtuUrl)
    else:
        return None


def link_bar_extractor(html_component: Tag) -> list:
    '''
    Converts the HTML under link bar from DTU Webpage
    into meaningful Array
    '''
    result = {}
    submenu = []
    try:
        heading = html_component.find('a').get_text().strip()
        i: Tag
        for i in html_component.ul.find_all('li', recursive=False):
            try:
                link = i.a.get('href')
                if link != None:
                    submenu.append({
                        'name':  i.a.get_text().strip(), 'link': convert_link(link)
                    })
                else:
                    subsublist = []
                    x: Tag
                    for x in i.find_all('li'):
                        subsublist.append({
                            'name':  x.a.get_text().strip(), 'link': convert_link(x.a.get('href'))
                        })
                    submenu.append({
                        'name':  i.a.get_text().strip(), 'sub_list': subsublist
                    })
            except:
                None
        result = {
            'name': heading,
            'sub_list': submenu
        }
    except:
        None
    finally:
        return result


def side_menu_extractor(html_component: Tag) -> list:
    '''
    Converts the HTML under the side menu
    from DTU Webpage containing links to
    various resources into meaningful Array
    '''
    result = []
    items = html_component.find_all('li')
    i: Tag
    for i in items:
        try:
            result.append({'name': i.get_text().replace(
                '\n', '').strip(), 'link': convert_link(i.find('a').get('href'))})
        except:
            None
    return result


def latest_tab_extractor(html_component: Tag) -> list:
    '''
    Converts the HTML under latest_tab div
    from DTU Webpage into meaningful Array
    '''
    result = []
    try:
        item: Tag
        for item in html_component.find_all('li'):
            try:
                aTag = item.find_all('a')
                if len(aTag) > 1:
                    sub = []
                    i: Tag
                    for i in aTag:
                        try:
                            sub.append({
                                'name': str(i.get_text()).replace('||', '').strip(),
                                'link': convert_link(i.get('href'))
                            })
                        except:
                            None
                    if item.a.get('href') == None:
                        if item.h6.string == None and aTag[0].link == None:
                            name = aTag[0].get_text()
                            sub.pop(0)
                        else:
                            name = item.h6.string
                        result.append({
                            'name': name.strip(),
                            'sub_list': sub
                        })
                    else:
                        for x in sub:
                            result.append(x)
                else:
                    result.append({
                        'name': item.get_text().strip(),
                        'link': convert_link(item.a.get('href'))
                    })

                '''
                As mentioned DTU webpage is poorly optimized, it because 
                it contains all the previous links/data all everything in
                it's main homepage. It is good to keep old database for
                record but no need keep it avalible here, but should have
                a seperate page for the same.
                Since this old information is pretty useless to most, we will
                be limiting the results by showing only the default info.
                '''
                if str(result[len(result)-1]).__contains__('view all'):
                    result.pop()
                    break
            except:
                None
    except:
        if(len(result) == 0):
            result.append({
                'name': 'End of results',
                'link': 'http://dtu.ac.in/'
            })
    finally:
        return result
