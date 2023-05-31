from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# In[14]:


driver = webdriver.Edge()
driver.get("https://in.linkedin.com/")


# In[15]:


time.sleep(10)
username = driver.find_element(By.XPATH,"//input[@name='session_key']")
password = driver.find_element(By.XPATH,"//input[@name='session_password']")
username.send_keys("rinkuahirwar06022002@gmail.com")
password.send_keys("password")

time.sleep(2)
submit = driver.find_element(By.XPATH,"//button[@type='submit']")
submit.click()




time.sleep(1)
company_name="yahoo"
designation=["talent","acquisition"]
print("Enter the company name whose HR you want to connect : ")
company_name=input()









for i in ['2','3']:
    #opening connection page
    driver.get("https://www.linkedin.com/search/results/people/?keywords=" + company_name +"%20" + designation[0] + "%20" + designation[1] + "&network=%5B%22S%22%5D&origin=FACETED_SEARCH&&page=+"+i+"&sid=1")
    time.sleep(5)
    #selecting all buttons on the page
    all_buttons = driver.find_elements(By.TAG_NAME,"button")
    #from above selecting only the connect buttons
    connect_buttons = [i for i in all_buttons if i.text=="Connect"]

    #print(connect_buttons)

    for i in connect_buttons:
        #clicking connect button
        driver.execute_script("arguments[0].click();",i)
        time.sleep(2)


        #selecting and clicking Add a note button
        Add_a_note_button =  driver.find_element(By.XPATH,"//button[@aria-label='Add a note']")
        # print(Add_a_note_button)
        Add_a_note_button.click()
        # driver.execute_script("argument[0].click();",Add_a_note_button)
        time.sleep(2)

        #selecing text_area and adding custom-message
        text_area_window = driver.find_element(By.ID,"custom-message")
        text_area_window.send_keys("Hi \n Since the Placement season has started for the batch graduating in 2024. Being the Placement Coordinator at NIT Jalandhar CSE batch'24 I would like to invite "+company_name+" to our campus for recruiting young talent, I would like to connect with you for the same")
        time.sleep(2)

        #clicking on submit button
        Send_button = driver.find_element(By.XPATH,"//button[@aria-label='Send now']")
        Send_button.click()
        #driver.execute_script("argument[0].click();",Send_button)
        
        try :
            
            close = driver.find_element(By.XPATH,"//button[@aria-label='Dismiss']")
            close.click()
            #driver.execute_script("argument[0].click();",close)
            time.sleep(2)
        except Exception as e :
            print("hi");




driver.quit()

