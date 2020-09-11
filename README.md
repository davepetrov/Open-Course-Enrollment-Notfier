# Open-Course-Enrollment-Notfier
A simple script that notifies you in you terminal when a specific UofT course is not full

Usage: python3 lesson-notify.py  [Utor Password] [UtorID] [x-path_to_pencil] [x-path_to_lesson]
Keep the program running in the background, check terminal periodically for news on your course enrollment status

Example:
python3 lesson-notify.py fakeusername fakepassword '/html/body/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div[3]/div[2]/div[3]/div[2]/div/div/div[1]/div/div[4]/div/div[3]/div/table/tbody[2]/tr/td[6]/button' '/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/form/table[2]/tbody[3]/tr/td[5]/div/div/div/div[1]/span'


Read more about X-Path's here:
https://www.w3schools.com/xml/xml_xpath.asp

x-path to pencil:
![x-path to pencil](/images/pencil.png)

x-path to lesson:
![x-path to lesson](/images/lesson.png)
