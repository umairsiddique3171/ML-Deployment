# ml_model_deployment_as_public_api_using_fastapi_and_ngrok
This repository contains the source code of the project where I trained and deployed diabetes prediction model as public api using fastapi and ngrok. In this project, basically what was done is this that local api url of ml model was created using fast api and then public api url was generated by connecting that local api url port with ngrok tunnel. This public api url takes following inputs to be posted as json : pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,dpf and age, and returns classification result and score. 
<br>
---local-host url -> only you can access it.
<br>
---public-url ngrok -> anyone with url can access it until the terminal is running. It's a temporary solution.
<br>
---for permanent solution you can use Heroku or other hosting platforms.
<br>
---ngrok helps you quickly share what you have on your local host with anyone in the world.
<br>
---ngrok allows you to tunnel your local host into temporary url.
<br>
---extremely useful for team members or freelance person to quickly deploy their local code to temporary web server to share progress.
<br>
---it works real time which means if your manager as for some changes in code, after making changes you can post the code again and new
temporary url will be generated and all your manager has to do is to refresh the website.
<br>
<br>
Sample input data was taken from diabetes dataset, which can be found here: https://github.com/umairsiddique3171/ML-Deployment/blob/main/ml_model_deployment_as_public_api_using_fastapi_and_ngrok/diabetes_classifier/diabetes_data.csv
<br>
<br>
Results video was also recorded and compressed, which can be found here : https://github.com/umairsiddique3171/ML-Deployment/blob/main/ml_model_deployment_as_public_api_using_fastapi_and_ngrok/results.mp4
<br>
<br>
This video will help you while setting up ngrok in your system environment : https://www.youtube.com/watch?v=aFwrNSfthxU
<br>
<br>
<br>
Author : Umair Siddique