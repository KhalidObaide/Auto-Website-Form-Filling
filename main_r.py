from selenium import webdriver
import time 
import random

num = int(input('how many vooter do you need ? '))

#open the url by selected browser
for x in range (0 , num):
	
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
	url_insert = "https://rashidobaidi.com/khalid/users.php?username="+username+"&email="+email+"&password="+password+"&name="+name
	driver.execute_script("window.open(url_insert);")
	
	# filling the blanks
	driver.find_element_by_xpath("//input[@name='name']").send_keys(name)
	driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
	driver.find_element_by_xpath("//input[@name='email']").send_keys(email)
	driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
	# click the button 
	#driver.find_element_by_xpath('//*[@id="main-hero"]/div/div/div/div[1]/div/div[6]/button').click()
	

        #driver.find_element_by_id("main-hero").click()