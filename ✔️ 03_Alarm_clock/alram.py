from datetime import datetime
import winsound
import time
time1 = str(input("Enter Time (H:M) : "))


target = datetime.strptime(time1,'%H:%M').time()


while True:
    now = datetime.now().time()

    print(now.strftime("%H:%M:%S"), end="\r", flush=True)
    
    if now.hour == target.hour and now.minute == target.minute:
        winsound.PlaySound('audio.wav', winsound.SND_ASYNC)
        input("Enter any key to exit: ")

        break
time.sleep(1)


