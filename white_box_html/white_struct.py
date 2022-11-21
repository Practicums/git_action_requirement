from bs4 import BeautifulSoup
soup = BeautifulSoup(open('white_box_test_html/test_result.html').read(), 'html.parser')
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
node = soup.find_all("div", class_="unbreakable")[0]
node.insert(0, soup2)

f = open("./white_box_test_html/test_changed.html", "w").write(str(soup))