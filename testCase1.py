from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException

browser = webdriver.Chrome()
browser.get('https://ng-pokedex.firebaseapp.com/')

''' Test_1
    Step: Open the page “https://ng-pokedex.firebaseapp.com/”
    Expectation: The page consists of:
                    - header with menu icon
                    - “Search” input
                    - list of Pokemon
                    - footer with creators details '''

headerCheck = browser.find_element_by_css_selector("header")
searchCheck = browser.find_element_by_xpath("//input[@type='text']")
pokeCheck = browser.find_element_by_class_name("card--media")
footerCheck = browser.find_element_by_css_selector("footer")

if headerCheck.is_displayed() and searchCheck.is_displayed() and \
        footerCheck.is_displayed() and pokeCheck.is_displayed():
    print('Test_1: PASSED')
else:
    print('FAILED!')

''' Test_2
    Step: Scroll down the page
    Expectation: The header is sticky '''

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

if headerCheck.is_displayed():
    print('Test_2: PASSED')
else:
    print('FAILED!')

''' Test_3
    Step: Click the menu icon
    Expectation: The menu appears with options:
                    - Home
                    - About '''

burgerMenu = browser.find_element_by_css_selector("button")
burgerMenu.click()
burgerMenuHome = browser.find_element_by_xpath("//*[text()='Home']")
burgerMenuAbout = browser.find_element_by_xpath("//*[text()='About']")

if burgerMenu.is_displayed() and burgerMenu.is_displayed() and burgerMenuAbout.is_displayed():
    print('Test_3: PASSED')
else:
    print('FAILED!')

''' Test_4
    Step: Click “About” option
    Exception: The page with information appears '''

burgerMenuAbout.click()
checkContentAbout = browser.find_element_by_css_selector("app-about")

if checkContentAbout.is_displayed():
    print('Test_4: PASSED')
else:
    print('FAILED!')

''' Test_5
    Steps: Click the menu icon.
          Click “Home” option
    Exception: The main page is displayed '''

burgerMenu.click()
browser.implicitly_wait(1)
burgerMenuHome.click()
homePageTittle = browser.title

if homePageTittle == 'Search for Pokémon':
    print('Test_5: PASSED')
else:
    print('FAILED!')

''' Test_6
    Step: Type “saur” in the Search input
    Exception: 2 Pokemons are displayed:
                - Bulbasaur
                - Ivysaur '''

browser.execute_script("scrollTo(0,0);")
searchInput = browser.find_element_by_xpath("//input[@type='text']")
searchInput.send_keys('saur')
pokeAmout = 0

for i in range(1, 4):
    checkPoke = browser.find_element_by_css_selector('.sprite-{}'.format(i))
    i += 1
    pokeAmout += 1
if pokeAmout > 2:
    print('Test_6: FAILED!')
else:
    print('Test_6: PASSED')

''' Test_7
    Step: Click the Bulbasaur icon
    Exception: The popup appears with:
                - red header with x button
                - Bulbasaur icon
                - title: “Bulbasaur #1”
                - type: grass
                - info: “Height: 0.7 m Weight: 6.9 kg”
                - description: “For some time after its birth, 
                  it grows by gaining nourishment from the seed on its back.” '''

bulbasaurDetails = browser.find_element_by_css_selector('.sprite-1')
bulbasaurDetails.click()

headerCheck = browser.find_element_by_class_name('ngx-modal__header')
color = headerCheck.value_of_css_property('background-color')
buttonX = browser.find_element_by_class_name('ngx-modal-closable-target.ngx-modal__close-btn')
red = 'rgba(239, 83, 80, 1)'

if color == red and buttonX.is_displayed():
    header = 'PASSED'
else:
    header = 'FAILED'

bulbasaurIcon = browser.find_element_by_css_selector('.sprite-1')

if bulbasaurIcon.is_displayed():
    icon = 'PASSED'
else:
    icon = 'FAILED'

tittle = browser.find_element_by_xpath("//*[text()='Bulbasaur #1']")
if tittle.is_displayed():
    tittle = 'PASSED'
else:
    tittle = 'FAILED'

typeGrass = browser.find_element_by_css_selector('.grass')
typePoison = browser.find_element_by_css_selector('.poison')

if typeGrass.is_displayed() and typePoison.is_displayed():
    pokeType = 'FAILED!'
elif typeGrass.is_displayed():
    pokeType = 'PASSED'
else:
    pokeType = 'FAILED!'

content = browser.page_source
if content.find('Height: 0.7 m Weight: 6.9 kg'):
    info = 'PASSED'
else:
    info = 'FAILED!'

if content.find('For some time after its birth, it grows by gaining nourishment from the seed on its back.'):
    description = 'PASSED'
else:
    description = 'FAILED!'

if header == 'PASSED' and icon == 'PASSED' and tittle == 'PASSED' and info == 'PASSED' \
        and description == 'PASSED' and pokeType == 'PASSED':
    print('Test_7: PASSED')
else:
    print('Test_7: FAILED!')

''' Test_8
    Step: Click the x button
    Exception: The popup appears with text: “Are you sure you want to close?”'''

buttonX.click()
try:
    WebDriverWait(browser, 2).until(ec.alert_is_present(), 'Are you sure you want to close?')

    alert = browser.switch_to.alert
    alert.accept()
    print('Test_8: PASSED')
except TimeoutException:
    print('Test_8: FAILED!')

''' Test_9
    Step: Click “Yes” button
    Exception: The popup is closed'''

try:
    buttonYes = browser.find_element_by_id('here button ID')
    print('Test_9: PASSED')
except NoSuchElementException:
    print('Test_9: FAILED!')

browser.close()
