from selenium import webdriver
import time
import re

path = r''
driver = webdriver.Chrome(path)

url = 'https://www.travelmath.com/nearest-airport'

city_list = ['Tulsa, Oklahoma', 'Fair Banks, Alaska', 'St. Cloud, Minnesota', 'Nashua, New Hampshire', 'Mesa, AZ', 'riverside, ca','california, chula vista',]
nearest_airport_dict = {}

for i in city_list:
    driver.get(url)
    text_box = driver.find_element_by_xpath('//*[@id="CalcToField"]')
    text_box.send_keys(i)
    time_breaker = 0
    driver.find_element_by_xpath('//*[@id="EchoTopic"]/div/div[1]/div/form/div[4]/div/button/strong').click()
    time.sleep(.15)
    while True:
        try:
            true_variable = driver.find_element_by_xpath('//*[@id="EchoTopic"]/div[1]/div[1]/p[1]').text + driver.find_element_by_xpath('//*[@id="EchoTopic"]/div[1]/div[1]/p[2]').text #//*[@id="EchoTopic"]/div[1]/div/h3
            #true_variable += ' ' + driver.find_element_by_xpath('//*[@id="EchoTopic"]/div[1]/div[1]/p[2]').text
        except:
            time.sleep(.1)
            time_breaker += 1
            if time_breaker == 3:
                print(i + ' was not found')
                break
            continue
        else:
            if 'Travelmath' in true_variable:
                print(i + ' was not found')
                break
            print(true_variable)
            sections = re.findall(r'(?:nearest\smajor\sairport\sis\s|closest\smajor\sairport\sto\s)(.+?)\((.+?)\s\/\s(.+?)\)', true_variable) #(?:nearest\smajor\sairport\sis|closest\smajor\sairport\sto.+?\sis)\s(.+)?\s\((.+)?\s\/\s(.+)?\)
            nearest_airport_dict[i] = [sections[0][0], sections[0][1], sections[0][2]]

            break

driver.close()

print(nearest_airport_dict)
