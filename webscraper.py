from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/england-vs-india-2nd-semi-final-1298178/ball-by-ball-commentary').text
#print(html_text)

soup = BeautifulSoup(html_text, 'lxml')
bbbs = soup.find_all('div', class_ = 'lg:hover:ds-bg-ui-fill-translucent ds-hover-parent ds-relative')
#print(byb)

for ball in bbbs:
    bowlertobatter = ball.find('div', class_ = 'ds-leading-none ds-mb-0.5').text
    print(bowlertobatter)

    
