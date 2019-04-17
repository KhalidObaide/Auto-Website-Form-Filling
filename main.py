from selenium import webdriver
import time 
import random
from selenium.webdriver.common.keys import Keys

#num = int(input('how many vooter do you need ? '))
num = 1
#open the url by selected browser
for x in range (0 , 3):
	
	#taking information for rating  
	url = "https://mysenior.io/register?ref=test_u"
	# choosing browser 
	driver = webdriver.Chrome("C:/Users/stu_lab/Desktop/khalid/chromedriver")
	driver.get (url)
	# filling blanks 
	s_chars = ('a' , 'e' , 'o' , 'u' , 'i')
	chars = ('b' , 'c' , 'd' , 'f' , 'g' ,'h' , 'j' , 'k' , 'l' , 'm' , 'n' , 'p' , 'q' , 'r' , 's' ,'t' ,'v' ,'w' , 'x' , 'z')

	emailpast = ('@gmail.com' , '@yahoo.com' , '@outlook.com' , '@protonmail.com')

	emailthing = ('2010' , 'sh4' , '2020' , 'please' , '2000' , 'this')

	username = random.choice(chars) + random.choice(s_chars) + random.choice(chars) + random.choice(s_chars)

	secname = random.choice(chars) + random.choice(s_chars) + random.choice(chars) + random.choice(s_chars)

	name = username + " " + secname
	email = username + secname +random.choice(emailthing) +random.choice(emailpast)

	password = name + str(time.time()) 

	# filling the blanks
	driver.find_element_by_name('name').send_keys(name)
	driver.find_element_by_name('username').send_keys(username)
	driver.find_element_by_name('email').send_keys(email)
	driver.find_element_by_name('password').send_keys(password)
	#driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/nav/div/div[2]/div[2]/div[2]/div/div/div/ul/li[3]/i').click()
	# click the button 
	#driver.find_element_by_xpath('//*[@button]').click()
	#url_insert = "https://rashidobaidi.com/khalid/users.php?username="+username+"&email="+email+"&password="+password+"&name="+name
	#driver.get("https://rashidobaidi.com/khalid/users.php?username=test3&email=test2&password=123453&name=test3")
	driver.execute_script("window.open('https://rashidobaidi.com/khalid/users.php?username="+username+"&email="+email+"&name="+name+"&password="+password+"');")
	time.sleep(7)
	driver.close()
