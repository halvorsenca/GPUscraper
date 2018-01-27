from bs4 import BeautifulSoup
import urllib.request
import time

from PyQt5 import Qt
import sys

n = 0
while(1):

    print("iteration" + str(n))
    URL = 'https://www.nvidia.com/en-us/geforce/products/10series/geforce-store/'
    page = urllib.request.urlopen(URL)

    soup = BeautifulSoup(page, 'html.parser')

    things = soup.find_all('h2')

    app = Qt.QApplication(sys.argv)
    systemtray_icon = Qt.QSystemTrayIcon(app)

    changed = []

    for e in things:
        string_rep = str(e)

        if string_rep[11:17] == 'shield':

            if string_rep[-14:] != 'Notify Me</h2>' and string_rep[-14:] != 'd NVIDIA.</h2>':
                print(string_rep[-14:])
                changed.append(1)

    if len(changed) != 0:

        print('there has been a change')
        systemtray_icon.show()
        systemtray_icon.showMessage('URGENT', 'There is a change in the GPUS')


    time.sleep(30)
    n += 1
