# Pivotal API GP1

This framework is part of BDTPython course, the target is to learn how to implement **behave** with python, validate json schemas, and generate a full regression report.

Additionally we learned to create unittest with mocks and configure travis for CI. 

### Full regression and reports

Currently a full regression can be executed in a Windows environment through the **full_regression.bat** file once the project is cloned but take into account
it is necessary to download the allure command line tool and set environment variables before run the regression script.

First download the [allure-commandline_2.8.0](http://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.8.0/allure-commandline-2.8.0.zip) and unzip it
under the **C:/>** partition. You can also unzip it in another location but make sure to update the last line of **full_regression.bat** with the correct path.

Next, set a environment variable for **TRACKER_TOKEN**, it should contains the token you want to use to run the scenarios (required).

e.g.

`C:\>set TRACKER_TOKEN=22x2xx44x11x3xx1xx44`

Finally, you can run full_regression.bat file, this will set the token into the config.yml file, execute the scenarios, and open the default browser to show the final report.
    
### Python packages:

* requests
* behave
* allure-behave
* jsonschema
* simplejson
* PyYAML
* mock
