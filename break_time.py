# open a public URL, in this case, the webbrowser docs
import webbrowser
import time

total_breaks = 3
break_count = 0

print("This program started "+time.ctime())
while (break_count < total_breaks):
    time.sleep(2*60*60) #added 2 hours dalay
    webbrowser.open('https://www.youtube.com/watch?v=w-Ng5muAAcg&list=RDw-Ng5muAAcg#t=3')
    break_count = break_count + 1

