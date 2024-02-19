# ml_model_deployment_as_public_api_on_heroku
This repository contains the source code of the project where I trained and deployed diabetes prediction model as public api on heroku.This public api url takes following inputs to be posted as json : pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,dpf and age, and returns classification result and score as response. 
<br>
<br>
For Heroku Deployment, steps are simple : 
<br>
<br>
1- upload your api creation using fastapi python files (i.e. main.py,utils.py here), ml model file, requirements.txt, Procfile, and runtime.txt on your github repository.
<br>
2- go to your heroku dashboard, create new app and connect your github repository with your heroku app.
<br>
3- enable automatic deploys, and deploy your mentioned branch to generate a public url as a result.
<br>
4- now you can use this url in your api implementation (i.e. predict.py here) or any UI to post user inputs and it will return results in response and if there are any errors you can check them in logs section in your heroku app dashboard.
<br>
<br>
<br>
Author : Umair Siddique