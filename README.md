# Introduction 
This project is an automation testing solution for ACTC. Here is the skill set for this solution.
- Python
- pytest
- pytest-html
- py4j
- pylint
- selenium
- python-dotenv
- requests
- SikuliX
- Chrome
- Chromedriver

# Getting Started
1.	Install Chrome and config chromedriver
    - Install Chrome
    - Downdload chromedriver which matches the intalled Chrome version  [Download](https://sites.google.com/a/chromium.org/chromedriver/downloads)
    - Put the chromedriver.exe in the C:\chromedriver_win32
    - Add C:\chromedriver_win32 to the System Environment **Path**
2.	Install latest version of VS Code [Download](https://code.visualstudio.com)
3.  Install latest version of Python [Download](https://www.python.org/downloads/windows/)
4.	Clone this repository and open it with VS Code
5.	Run the following script under the root of this repository
    ```
    pip install virtualenv
    python -m venv venv
    PS > .\venv\Scripts\Activate.ps1
    pip install -r requirements
    ```
6. Config the openjdk
    - Download the openjdk [Download](https://jdk.java.net/14/)
    - Unzip the openjdk to C:\openjdk-14.0.1_windows-x64_bin\jdk-14.0.1
    - Set up the JAVA_HOME environment with C:\openjdk-14.0.1_windows-x64_bin\jdk-14.0.1
    - Add following 2 values to the System Environment Path
        ```
        %JAVA_HOME%\bin
        %JAVA_HOME%\jre\bin
        ```
    - Test java with follow command in the PowerShell
        ```
        java -version
        ```
7. Config the SikuliX
    > The SikuliX API 2.0.4 could not running up, so use the 2.0.3 
    - Download the SikuliX IDE 2.0.4 [Download](https://launchpad.net/sikuli/sikulix/2.0.4/+download/sikulixide-2.0.4.jar)
    - Download the Sikulix API 2.0.3 [Download](https://launchpad.net/sikuli/sikulix/2.0.3/+download/sikulixapi-2.0.3.jar)
    - Create a new folder named SikuliX under D: and put these two jars in it
    - Run the following script under D:\SikuliX in the PowerShell
        ```
        java -jar .\sikulixide-2.0.4.jar
        ```
    - Ignore the notice and the IDE will open, then close the IDE
    - Copy the py4j jar to SikuliX IDE extensions folder
        ```
        from: venv\share\py4j\py4j0.10.9.jar
        to: C:\Users\{YOUR_LOGIN_NAME}\AppData\Roaming\Sikulix\Extensions
        ```
    - Run the following script under D:\SikuliX in the PowerShell to check the SikuliX API
        ```
        java -jar .\sikulixapi-2.0.3.jar -p -v
        ```
# Test
Run the following script to start the automation testing, the **test_classes** folder can be changed

```
pytest .\src\test_classes --html=report.html --self-contained-html
```
