# ml_model_deployment_as_web_app_using_streamlit_on_heroku
This repository contains the source code of the project where I trained and deployed diabetes prediction model as web app using streamlit on heroku. In web application interface, user has to fill following fields : pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,dpf and age, and then push the result button to get the classification results with confidence score. 
<br>
<br>
For streamlit web app deployment on heroku, steps are simple : 
<br>
<br>
1- upload your steamlit web app creation python files (i.e. app.py, utils.py here), ml model file, requirements.txt, Procfile, setup.sh file, and runtime.txt on your github repository.
<br>
2- go to your heroku dashboard, create new app and connect your github repository with your heroku app.
<br>
3- enable automatic deploys, and deploy your mentioned branch to generate a public url as a result.
<br>
4- browse this url and your streamlit web app would be working.
<br>
<br>
<br>
Author : Umair Siddique