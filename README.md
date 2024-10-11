# boston_housing_Dpricing deployment of ml model

# STEPS:
 # Software and tools requirements:
 1. [GithubAccount](https://github.com/eleven111101)
 2. [Python](https://www.python.org/downloads/)
 3. [Jupyter notebook](https://jupyter.org/install)
 4. [Heroku](https://www.heroku.com/)
 5. [VScodeIDE](https://code.visualstudio.com/download)
 6. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)
 7. [Anaconda](https://www.anaconda.com/download?utm_source=anacondadoc&utm_medium=documentation&utm_campaign=download&utm_content=topnavalldocs)
 8. [POSTMAN](https://www.postman.com/downloads/)
 9. [JSONINT](https://jsonlint.com/)

# For cloning any repository
1. Open cmd prompt and then clone the repository.
2. Clone the repository by providing URL.
3. ``` git clone "URl"```


 # Create a new Environment for project
 ```conda create -p venv python==3.7 -y```

# Environment purpose
 ```
To activate this environment
$ conda activate "D:\TCS_GENAI\End_to_EndML\Git_clone\boston_housing_Dpricing\ve"
*******
To deactivate an active environment, use
$ conda deactivate 
```
 # Install the Libraries using the Generation of the txt format files
``` Requirement.txt -- Run this file in pip install -r requirements.txt ```

 # Create a global username and email for commiting
 ```git config --global user.name "your_name" ```
 *******
 ```git config --global user.email "your_email"```

 # Create a message for commiting
 ```git commit -m "your_message" ```
 *******
 ```git push/origin >> Browser open and the commit has happened"```

 # After coding the app.py 
```
1. Access the app at the default URL: 127.0.0.1:5000.  
2. Use POSTMAN if the `Predict_API` function doesn't work directly.  
3. Validate your JSON format using JSONLINT.com.  
4. In POSTMAN, enter the URL and send a POST request with JSON data.
5. The function will run and return the prediction.
```

# Code for home-page.HTML 
This will generate predictions based on the input values. You'll need to add a corresponding function in the `app.py` file of your Flask application to handle this.

# Cloud application
```
1. We'll begin by using the Heroku cloud platform.
2. Next, we'll create a Procfile.
3. The Procfile defines the commands to execute once the app starts.
4. We'll navigate to the Heroku dashboard and create a new app.
5. The project will be deployed using Heroku's direct deployment methods.
6. We'll also use the Heroku CLI to deploy the project.
```