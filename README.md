# FoodTruck
A Mobile Application using Flutter for suggesting healthier alternative food products based on the food product they choose. Basically User will scan the bar-code of the food product and based on that our app will suggest users the healthier alternative using ML and Image Processing and if the barcode is not in our database we will ask the user to upload the food-product details into our DataBase. 

<img width="809" alt="Screenshot 2021-09-28 at 5 54 11 PM" src="https://user-images.githubusercontent.com/63253383/135095860-a649e0da-8f8b-4fc6-a58d-f15840de4ea0.png">

# Work-Flow
As Shown Above the user will scan the bar-code and send an http request to the backend: <br />
<br />
  if the barcode-ID already exists: <br />
       we return the list of healthier alternative food products.<br />
  else: <br />  Ask user to scan food-products Nutritional-Information,Ingredients-Information and Other details and send it to our database. <br />
  
# App 
App Developer is expected to work only within the app directory. <br />
```
$ cd app
$ flutter pub get
```
## Required Skills:

* Should possess good knowledge and development skills with Dart and Flutter.
* Good Knowledge on flutter http package.
* Good Interest in Open-source contribution.

# Server 
Server Developer is expected to work only within the server directory. <br />

```
$ cd server
$ pip install virtualenv
#Create virtualenv
$ python3 -m venv venv
#Create virtualenv for windows
$ py -3 -m venv venv
#Activate virualenv:
$ . venv/bin/activate
#Activate virualenv for windows
$ venv\Scripts\activate
#Install Flask on the enviroment
$ pip install -r requirements.txt
```
## Required Skills:

* Should possess good knowledge and development skills with python and Flask.
* Good Knowledge regarding Rest-APIs and Database management.
* Good Interest in Open-source contribution.

# ML
ML Developer is expected to work only within the MachineLearningKit folder inside server directory. <br />

Follow the same setup procedure as shown in server setup.

## Required Skills:

* Should be able to Retrive Text from image sent from the app.
* Should be able to code a ML model which recognises food-products from the given image.
* Good Interest in Open-source contribution.

# GITHUB GUIDELINES
Kindly Refer To CONTRIBUTING.md 
