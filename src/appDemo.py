from py4j.java_gateway import JavaGateway
from pathlib import WindowsPath

JavaGW = JavaGateway()
SXApp = JavaGW.jvm.org.sikuli.script.App
SXScreen = JavaGW.jvm.org.sikuli.script.Screen
SXKey = JavaGW.jvm.org.sikuli.script.Key

# SXApp.open("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
SXApp.openLink("https://cn.bing.com")

screen = SXScreen()
screen.getCenter()

img = str(WindowsPath.joinpath(WindowsPath.cwd(),'src' , 'images', 'bing_input.png'))
print(img)

# a Match object is completely handled at the Java level
# not defined at the Python level
match = screen.exists(img, 3.0) # number must be float/double
print(match)
if match:
    print(match)
    match.wait(1.0)
    match.type("SikuliX")
    match.type(SXKey.ENTER)
else:
    print('not match')
