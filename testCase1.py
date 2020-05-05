from selenium import webdriver
from time import sleep

# Enter test website
browser = webdriver.Chrome()
browser.get('https://ng-pokedex.firebaseapp.com/')

# Check elements
headerCheck = browser.find_element_by_css_selector("header")  # header
searchCheck = browser.find_element_by_xpath("//input[@type='text']")  # search input
pokeCheck = browser.find_element_by_class_name("card--media")  # poke list
footerCheck = browser.find_element_by_css_selector("footer")  # footer

if (headerCheck.is_displayed() and searchCheck.is_displayed() and footerCheck.is_displayed() and pokeCheck.is_displayed()):
    print('Test_1: PASSED')
else:
    print('FAILED!')

# Scroll down to check sticky header
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
if headerCheck.is_displayed():
    print('Test_2: PASSED')
else:
    print('FAILED!')

# Find burger menu and click on it
burgerMenu = browser.find_element_by_css_selector("button")
burgerMenu.click()
# Check menu content Home and About
burgerMenuHome = browser.find_element_by_xpath("//*[text()='Home']")
burgerMenuAbout = browser.find_element_by_xpath("//*[text()='About']")
if (burgerMenu.is_displayed() and burgerMenu.is_displayed() and burgerMenuAbout.is_displayed()):
    print('Test_3: PASSED')
else:
    print('FAILED!')

# Click and check content of About
burgerMenuAbout.click()
checkContentAbout = browser.find_element_by_css_selector("app-about")
if checkContentAbout.is_displayed():
    print('Test_4: PASSED')
else:
    print('FAILED!')

# Click on the menu icon and click on Home
burgerMenu.click()
browser.find_element_by_xpath("//*[text()='Home']")
burgerMenuHome.click()
homePageTittle = browser.title
if homePageTittle == 'Search for Pokémon':
    print('Test_5: PASSED')
else:
    print('FAILED!')

# Type in search input "saur"
browser.execute_script("scrollTo(0,0);")
searchInput = browser.find_element_by_xpath("//input[@type='text']")
searchInput.send_keys('saur')

# Out put should be two poke Bulbasaur and Ivysaur
pokeAmout = 0
for i in range (1,4):
    checkPoke = browser.find_element_by_css_selector('.sprite-{}'.format(i))
    i += 1
    pokeAmout += 1
if pokeAmout > 2:
    print('Test_6: FAILED!')
else:
    print('Test_6: PASSED')


# Click on Bulbasaur icon
bulbasaurDetails = browser.find_element_by_css_selector('.sprite-1')
bulbasaurDetails.click()

# Check red header with X button
headerCheck = browser.find_element_by_class_name('ngx-modal__header')
color = headerCheck.value_of_css_property('background-color')
buttonX = browser.find_element_by_class_name('ngx-modal-closable-target.ngx-modal__close-btn')
red = 'rgba(239, 83, 80, 1)'
if color == red and buttonX.is_displayed():
    header = 'PASSED'
else:
    header = 'FAILED'

# Check Bulbasaur icon
bulbasaurIcon = browser.find_element_by_css_selector('.sprite-1')
if bulbasaurIcon.is_displayed():
    icon = 'PASSED'
else:
    icon = 'FAILED'

# Check tittle should be “Bulbasaur #1”
tittle = browser.find_element_by_xpath("//*[text()='Bulbasaur #1']")
if tittle.is_displayed():
    tittle = 'PASSED'
else:
    tittle = 'FAILED'

# Check type should be only grass - think about solve!
#pokeType = browser.find_element_by_xpath("//*[text()='grass']")

# Check info find values “Height: 0.7 m Weight: 6.9 kg”
content = browser.page_source
if content.find('Height: 0.7 m Weight: 6.9 kg'):
    info = 'PASSED'
else:
    info = 'FAILED!'

# Check description should be “For some time after its birth, it grows by gaining nourishment from the seed on its back.”
if content.find('For some time after its birth, it grows by gaining nourishment from the seed on its back.'):
    description = 'PASSED'
else:
    description = 'FAILED!'

# Check test case 7
if (header == 'PASSED' and icon == 'PASSED') and tittle == 'PASSED' and info == 'PASSED' and description == 'PASSED':
    print('Test_7: PASSED')
else:
    print('Test_7: FAILED!')
sleep(2)

browser.close()
