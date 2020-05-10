from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.parleto.io/kariera/')

''' 
Test_1
    Step: Open the page “https://www.parleto.io/kariera/”
    Expectation: Opens a page with:
                    - header
                    - footer
                    - job offer
                    - steps to join
'''

headerCheck = browser.find_element_by_class_name('page-nav')
footerCHeck = browser.find_element_by_css_selector('.page-footer__wrap')
jobOfferCheck = browser.find_element_by_css_selector('.career-section__content')
stepsToJoinCheck = browser.find_element_by_css_selector('.steps-section')

if headerCheck.is_displayed() and footerCHeck.is_displayed() and jobOfferCheck.is_displayed() \
        and stepsToJoinCheck.is_displayed():
    print('Test_1: PASSED')
else:
    print('Test_1: FAILED!')

''' 
Test_2
    Step: Scroll down to section with tittle: “Znajdź role dla siebie!”
    Expectation: Scroll down to section with actual job offers
'''

scrollSection = browser.find_element_by_class_name('career-section__header')
browser.execute_script("arguments[0].scrollIntoView();", scrollSection)

if scrollSection.is_displayed():
    print('Test_2: PASSED')
else:
    print('Test_2: FAILED!')

''' 
Test_3
    Step: Click on job offer called "Software Tester"
    Expectation: Forwarding to Software Tester job details.
'''
qaJobOffer = browser.find_element_by_xpath("//*[text()='Software Tester']")
qaJobOffer.click()
qaDetails = browser.title

if qaDetails == 'Software Tester | Parleto | Team Value Software House':
    print('Test_3: PASSED')
else:
    print('Test_3: FAILED!')

''' 
Test_4
    Step: Scroll down to button 'Aplikuj'
    Expectation: Scroll down to see button 'Aplikuj'
'''

button = browser.find_element_by_class_name('box-offer__apply-button')
browser.execute_script("arguments[0].scrollIntoView();", button)

if button.is_displayed():
    print('Test_4: PASSED')
else:
    print('Test_4: FAILED!')

''' 
Test_5
    Step: Click the button 'Aplikuj'
    Expectation: Forwarding to application form 
'''

button.click()
jobTittle = browser.find_element_by_class_name('offer-job-title')
if jobTittle.is_displayed() and browser.find_elements_by_xpath("//h1[contains(text(), 'Software Tester | Parleto')]"):
    print('Test_5: PASSED')
else:
    print('Test_5: FAILED!')

# Later try to add logo verification
browser.close()
