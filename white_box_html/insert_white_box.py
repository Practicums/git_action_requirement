from bs4 import BeautifulSoup
import argparse
soup = BeautifulSoup(open('./white_box_test_html/test_changed.html').read(), 'html.parser')

node = soup.find_all("div", class_="white_test")[0]
f = open("./error.txt", encoding='utf-8')
lines = f.readlines()
file_name = lines[0]
print(file_name)
if len(lines) == 0:
    exit(0)
if len(lines) == 1:
    lines.append('''<div class="row aic pb5  color-passed">
        <div class="w120"></div>
        <div>No Error to display!</div>
    </div> ''')
else:
    for i in range(1, len(lines)):
        lines[i] = '''<div class="row aic pb5  color-failed">
        <div class="w120"></div>
        <div>{0}</div>
    </div> '''.format(lines[i])
    
soup2 = BeautifulSoup('''
<div class="step-row  border-b-gray">
    <div class="row aic pb5 fs14 bold">        
        <div class="w120 color-skipped">
            Modified File
        </div> 
        <div class="flex1 pr10">
            {0}
        </div>
    </div>
    '''.format(file_name) + 
' '.join([lines[i] for i in range(1, len(lines))])
    +
'</div>  ' , 'html.parser'     
)
node.insert(0, soup2)
f = open("white_box_test_html/test_changed.html", "w").write(str(soup))




