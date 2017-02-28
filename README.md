# Python Module for REST API calls
## Prerequisites
- Install the latest version of [Python 3](https://www.python.org/ftp/python/3.6.0/python-3.6.0.exe) on your computer.
  - Select the option to set your environment variables during the installation.
- Download the requests module.
```
$ easy_install requests
```

## Installing the SDK 
- Download the `cybersource-rest-sdk-python-master.zip` package into a directory of your choice. 
- Extract and go to the `cybersource-rest-sdk-python-master` directory.
- To install the package and the required dependencies run the following command:
```
$ python setup.py install
```

## Usage
- Register on [VDP (Visa Developer Platform)](https://developer.visa.com/ "Visa Developer Platform").
- Create an application on VDP. Make sure "CyberSource Payment API" is checked before creating the application.
- The Cybersource REST APIs require their payload to be in the form of a json file.
  - See the project's [sample payloads](../master/test/samples/) for examples.
- Put API key and Shared Secret in `configuration.ini`. Cybersource Payment API uses X-Pay-Token authentication method.
  - For more information, refer to the [VDP Manual](https://github.com/visa/SampleCode/wiki/Manual#x-pay-token-authentication "VDP Manual on Github").
- Go to the [test](../master/test/) folder, and run the samples using the following command:
```
$ python <transactionName>.py <payload path>
```
*For example:*
```
$ python auth.py samples/auth.json
```
