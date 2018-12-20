SET PYTHONPATH=%~dp0\..\src;%~dp0..\features;%~dp0..\environment

behave -f allure_behave.formatter:AllureFormatter -o allure_result_folder

allure serve %~dp0\allure_result_folder