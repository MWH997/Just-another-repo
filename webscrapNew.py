from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import csv
import numpy as np


#Declaring variables
Dnames = []
Ddes = []
sbString = ["1","2","3","4"]


driver = webdriver.Firefox()
url = "https://www.asiatic360.com/"
driver.get(url)

#Waiting for the page to load
timeout = 20
try:
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="menu-item-19"]')))
except TimeoutException:
    print ('Timed out waiting for page to load')
    driver.quit()

#Clicking on About us
driver.find_element_by_xpath('//*[@id="menu-item-19"]/a').click()

#Waiting for the page to load
timeout = 30
try:
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page"]/div[2]/div/div/section/div/div/div/div/div/section[7]/div')))
except TimeoutException:
    print ('Timed out waiting for page to load')
    driver.quit()


#Clicking on each board of directors and saving the information
for i in sbString:
	#Modifying XPATH to work for each director button
	urlPr1 = '//*[@id="sb"]'
	urlN1 = urlPr1[:11] +i+ urlPr1[11:]

	#Clicking on each director
	driver.find_element_by_xpath(urlN1).click()

	##Modifying XPATH to work for each director box
	urlPr2 =  '//*[@id="sbe"]/div[1]/img'
	urlN2 = urlPr2[:12] +i+ urlPr2[12:]

	#Waiting for each director information to load
	timeout = 20
	try:
    		WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, urlN2)))
	except TimeoutException:
    		print ('Timed out waiting for page to load')
    		driver.quit()
	
	#Modifying XPATH for Name
	urlI1 = '//*[@id="sbe"]/div[2]/div/div/h2'
	urlF1 = urlI1[:12] +i+ urlI1[12:]

	#Modifying XPATH for Designation
	urlDP = '//*[@id="sbe"]/div[2]/div/div/p[1]'
	urlDF = urlDP[:12] +i+ urlDP[12:]

	#Saving the Names & Designation
	Dnames.append(driver.find_element_by_xpath(urlF1).text)
	Ddes.append(driver.find_element_by_xpath(urlDF).text)	
	 
driver.quit()

print(Dnames)
print(Ddes)

#Merging two lists
dArr = np.column_stack((Dnames,Ddes))

#Creating & Writing to the csv file
with open('asiatic360.csv','w') as excelF:
	writer = csv.writer(excelF)
	writer.writerow(['Name','Designation'])
	writer.writerows(dArr)
	

	


