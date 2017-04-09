import time
import webbrowser
total_break = 3
count_break = 0
print("Programe now start "+time.ctime())
while (count_break < total_break):
    time.sleep(5)
    webbrowser.open("www.google.com")
    count_break = count_break + 1


print("Program now closed..")

