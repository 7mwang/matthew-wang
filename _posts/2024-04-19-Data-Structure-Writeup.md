---
toc: true
comments: true
layout: post
title: Data Structures Writeup
author: Matthew Wang
description: Data structures project writeup with screenshots, labels, and explanations.
courses: { csp: {week: 33} }
type: hacks
---

From VSCode using SQLite3 Editor, show your unique collection/table in database, display rows and columns in the table of the SQLite database.


This is our data table for our user data.


![323749580-927fa2a9-b378-4b2f-af91-191c00375500](https://github.com/7mwang/matthew-wang/assets/108709185/bb6c6550-e1f5-406d-beae-2db525f9e903)
  
  
From VSCode model, show your unique code that was created to initialize table and create test data.


This is the model used to generate user test data and the admin account into an sql file.


![323753262-66768bda-33be-4ca1-855a-ed57cfe80958](https://github.com/7mwang/matthew-wang/assets/108709185/adc2cc0b-9fca-4560-9b18-77e6ac89fcfb)


In VSCode using Debugger, show a list as extracted from database as Python objects.


Data is separated from body into variables.


![323760334-7bc92106-2647-4030-abf0-752094851553](https://github.com/7mwang/matthew-wang/assets/108709185/64b4aa5a-1496-4c05-b24d-c17d56e5a731)


In VSCode use Debugger and list, show two distinct example examples of dictionaries, show Keys/Values using debugger.


Returning data in dictionary, and setting up data with dictionaries and multiple key value pairs.


![image](https://github.com/7mwang/matthew-wang/assets/108709185/fa175cf3-c1b2-48e7-b918-da4d57be3a5a)


![323761413-8ca7d606-c9b2-443b-9cde-a1359c55920e](https://github.com/7mwang/matthew-wang/assets/108709185/e5881967-28dd-498d-9dd9-b330fe29fd30)


In VSCode, show Python API code definition for request and response using GET, POST, UPDATE methods. Discuss algorithmic condition used to direct request to appropriate Python method based on request method.


On webpage, multiple different actions lead to different outcomes. For example, updating data and submitting images uses put, while logging in uses post.


![323853176-85b9a615-dd0b-4037-a9db-638b35bb1f76](https://github.com/7mwang/matthew-wang/assets/108709185/45076b2e-000b-4d0c-bf2b-56b732a950d2)


In VSCode, show algorithmic conditions used to validate data on a POST condition.


Data is checked to be long enough and exists so the post request can go through.


![323853404-ad6dd3d9-fb31-4ac9-b552-c60777b12d1e](https://github.com/7mwang/matthew-wang/assets/108709185/1ef6507f-2cc2-4fb9-bc0f-d849031d5ccc)


In Postman, show URL request and Body requirements for GET, POST, and UPDATE methods.
    

Body needed in login/signup system


![323854778-28c45771-2a61-48dd-8b25-87db476aed52](https://github.com/7mwang/matthew-wang/assets/108709185/a8ad16b5-713a-440c-b293-9507604417e3)


In Postman, show the JSON response data for 200 success conditions on GET, POST, and UPDATE methods.


JSON response shows success message, from 200 status


![323854970-2d9cb7ab-7ebc-4c4f-bfc3-8c29a757a508](https://github.com/7mwang/matthew-wang/assets/108709185/5b65609d-3105-4303-821f-8599c7e4090c)


In Postman, show the JSON response for error for 400 when missing body on a POST request.


When the body is either not there, or too short, the api returns a 400 error.


![image](https://github.com/7mwang/matthew-wang/assets/108709185/781b2832-9974-4396-82b3-9e83c4d00da5)


In Postman, show the JSON response for error for 404 when providing an unknown user ID to a UPDATE request.


When logging in, message user not found is returned if the user isn't in the database.


![323854870-2f138211-db76-4ab6-8e02-71487555a5a0](https://github.com/7mwang/matthew-wang/assets/108709185/818b085e-f9ec-4318-a2b8-f29d55c50f9f)


In Chrome inspect, show response of JSON objects from fetch of GET, POST, and UPDATE methods.


After login, api returns responses and data into console.


![323855159-1c49fa7d-dc5a-4aba-ae82-2f066eb44c73](https://github.com/7mwang/matthew-wang/assets/108709185/e96edefe-e36e-4173-ae01-7228d41f6a36)


In the Chrome browser, show a demo (GET) of obtaining an Array of JSON objects that are formatted into the browsers screen.


Data page shows all user data in a formatted table.


![image](https://github.com/7mwang/matthew-wang/assets/108709185/a6e1800a-e59c-4da5-8b29-3590ea482b90)


In JavaScript code, describe fetch and method that obtained the Array of JSON objects.


Code below gets all user data from backend, and formats it into a table


![image](https://github.com/7mwang/matthew-wang/assets/108709185/e88f8e9f-0882-44a1-927a-b851ffff11d2)


In JavaScript code, show code that performs iteration and formatting of data into HTML.


![image](https://github.com/7mwang/matthew-wang/assets/108709185/752f135f-7c94-431e-ae8a-02ed2706adea)


In the Chrome browser, show a demo (POST or UPDATE) gathering and sending input and receiving a response that show update. Repeat this demo showing both success and failure.


![image](https://github.com/7mwang/matthew-wang/assets/108709185/70526355-66eb-47ea-b34e-11b1fcdbbbda)


![image](https://github.com/7mwang/matthew-wang/assets/108709185/70cdc489-2567-46cb-9d2d-ce791d9d3376)
    
    
In JavaScript code, show and describe code that handles success. Describe how code shows success to the user in the Chrome Browser screen.
The code takes the user's data and send its to the api to confirm whether the user has access. If the user is authorized in the database, it sends a positive response back to the frontend, which is interpreted as a goahead to chance the data, sending another request to the backend to update the data.


![image](https://github.com/7mwang/matthew-wang/assets/108709185/b6215383-465a-4bb1-8563-79b42fc971ba)


In JavaScript code, show and describe code that handles failure. Describe how the code shows failure to the user in the Chrome Browser screen.
The code takes the user's data and send its to the api to confirm whether the user has access. If the user is not authorized in the database, it sends a negative response back to the frontend, which is interpreted, and the frontend does not send a request to the backend to change the data.


![image](https://github.com/7mwang/matthew-wang/assets/108709185/c13e76f2-da97-4d01-affc-7efd25e7b77d)


