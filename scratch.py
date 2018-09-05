##Ques 1
from datetime import date
days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
print(days[date.weekday(date.today())])
##Ques 2
import webbrowser
webbrowser.open('https://www.youtube.com/watch?v=QJbpJQscn9E&t=113s')
##Ques 3
import os
os.rename('file.txt','file.jpg')