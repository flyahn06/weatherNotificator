import weather_getter
import win10toast
from time import sleep
import pprint
import subprocess

code, current_weather = weather_getter.generateRequest()

pprint.pprint(current_weather)

def clicked():
    print("Clicked!")
    subprocess.run("python mainwindow.py")


toaster = win10toast.ToastNotifier()
print()
toaster.show_toast(
    f'{current_weather["weather"][0]["description"]}, {current_weather["main"]["temp"]}°C',
    f'클릭하여 더 자세한 정보를 만나보세요',
    icon_path=f'sources\\image\\{current_weather["weather"][0]["icon"]}.ico',
    duration=3,
    threaded=True,
    callback_on_click=clicked
)

while toaster.notification_active():
    sleep(0.1)
