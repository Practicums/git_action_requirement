from bs4 import BeautifulSoup
soup = BeautifulSoup(open('git_action_requirement/white_box_html/test_result.html').read(), 'html.parser')
soup2 = BeautifulSoup('''

  <div class="row aic jsb mb10 pl30"> 
    <div class="row flex1 mw0 mr40 ml60">
        <span class="row flex1 mw0 fs32 ws">
            White Box Test Report
        </span>
    </div>
  </div>
<div class="white_test">
</div>
''', 'html.parser')
soup.find_all("span", class_="ws")[0].string.replace_with('Black Box Test Report')

node = soup.find_all("div", class_="unbreakable")[0]
node.insert(0, soup2)

f = open("git_action_requirement/white_box_html/test_changed.html", "w").write(str(soup))