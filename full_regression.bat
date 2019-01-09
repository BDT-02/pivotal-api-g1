powershell -Command "(gc config.yml) -replace 'TRACKER_TOKEN', '%TRACKER_TOKEN%' | Out-File config.yml"

SET PYTHONPATH=%~dp0\..\src;%~dp0..\features;%~dp0..\environment

behave -f allure_behave.formatter:AllureFormatter -o allure_result_folder

git checkout -- config.yml

C:\allure-2.8.0\bin\allure serve %~dp0\allure_result_folder
