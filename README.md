# James Rider Test FW
<insertar imagen fw aca>

# Pre-requisites
Follow along all the necessary configuration for each of the below pre-requisites, including global variables.
- Terminal of choice, as [WARP](https://www.warp.dev/)
- Python 3
- Install [Node.js](https://nodejs.org/en)
- Install [Appium](https://appium.io/docs/en/latest/quickstart/install/)
  - [UiAutomator2](https://appium.io/docs/en/latest/quickstart/uiauto2-driver/)
- Install  [Android Studio](https://developer.android.com/studio?hl=es-419) and SDK.
- [Appium Inspector](https://github.com/appium/appium-inspector/releases) this is optional, but needed when building tests.

# Setup

1. `python3 -m venv env_name`
2. `source env_name/bin/activate`
3. `pip3 install -r requirements.txt`
4. Make sure you open the Android Emulator and had connected your real device


# How to run test
- In order to execute all tests : `behave` 


- With Allure report  `behave -f allure_behave.formatter:AllureFormatter -o "reports" features/tests/[FEATURE_TO_RUN]_test.feature`







## Extras
#### Issues you may encounter
| Problem                                                                                                                                                                         |                                                                Solution                                                                | 
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------:|
| ADB not found                                                                                                                                                                   | Need to be added to the path: https://dev.to/ravics09/solution-of-command-not-found-adb-error-29e7; Get device name with `adb devices` |
| Loading the APK                                                                                                                                                                 |                                          Drag and Drop or go to `File > Profile or Debug APK`                                          |
| Error `UnknownMethodException: Message: The requested resource could not be found, or a request was received using an HTTP method that is not supported by the mapped resource` |               Downgraded Appium & Selenium latest to on previous, and removed `wd/hub` from URL in desired capabilities                |

  