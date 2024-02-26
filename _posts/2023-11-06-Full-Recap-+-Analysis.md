---
toc: True
comments: False
title: Team Project - Final Recap + Code Analysis
type: plans
courses: {'csp': {'week': 12, 'categories': ['4.A']}}
categories: ['C1.4']
---
<html>
<header>Overall, apart from getting terrorized by CORS, this project was great fun I gained good experience from working on it.<br> 
<ul>What did I end up learning?
<li>In the end, I learned loads about JavaScript while working on my game, and Python while working on APIs and databases.</li>
<li>In JavaScript I learned about interacting with CSS and animating, event handlers, sending API requests, cookies, and probability systems.</li>
<li>In Python I learned about using sqlite3 with python, writing API to interact with databases, storing data, analyzing and interacting with data, and posting/getting fron APIs</li>
<li>I also learned a few more minor things like CSS styling, encrypting data, and different bits and pieces with the inner workings of APIs.</li>
</ul><br>
<strong><font size = 20>What didn't I get to?</font></strong>

<br>In the end, I didn't get to create my rocket escape, and only implemented an honestly lame endgame that costs a bunch of a new currency to complete. Other than that, I am pretty<br>satisfied with how far I got with this game. I had a lot of struggle I overcame with APIs, and I'm proud of myself for overcoming those issues.<br>

<strong><font size = 20>How did I use x in y system?</font></strong>
<ul>
<li>I used cookies to store username data, and later called those cookies to interact with my API<br>I did this by first saving the cookie by taking the inner HTML values of a form on our login page, then storing it in a browser cookie named 'username'. Then I continued by defining a function "getCookie(name)", where the name of the cookie was 'username'. I would then define a constant that is a list of all of the cookies on the site. Then, I looped through that list, checked whether the name of the cookie was 'username', and grabbed the value of it if it was. Using this process, I could call the getCookie() function whenever I needed to get the username of the player.</li>
<li>I used sqlite3 to store game data to be loaded using a get request that activates on window load<br>I accomplished this by creating tables in SQLite3, and pushing data to them through my Python API. I would first use a post request from my frontend to update the data on my backend, pushing the data to the database. When I would use a get request, I would look for the data in the database by username, and if the username existed, would grab the data from the database I accomplished this using the execute() and fetchone() functions mainly.</li>
<li>I used default variables to make sure new players didn't get null or undefined game data<br>I didn't do this how a traditional default variable is defined, but instead checked for the existence of a username, and if that username didn't exist, I would assign default values decided by me to the user.</li>
<li>I used if statements to verify the existence of variables<br>In many of my if statements, I would have something like if (username). This would check the boolean value of username, and if it didn't exist, it would be assigned the value of False, while if it did exist, it would be assigned the value of True. I used this with my default variable system, first checking if username is true meaning there is a username, then loading data afterwards.</li>
<li>I used get/post requests with my APIs to store and retrieve game data<br>In my backend, I would first define a class for use with my API blueprint. Then, I would define the get function which would be called when our frontend made a GET request to our backend. In my get() function for my user data class, I would first check my database using execute() and fetchone(), and if if (cursor.fetchone()) returned true, then I would grab data from the database from the user's name, and would send it back to the frontend in a jsonified response. If it returned false, I would send default values back in the same way.</li>
<li>And much much more knowledge was used throughout the project<br>I used a lot of document.getElementById() to change the HTML elements on my game, I used a lot of try-catch block statements to catch errors formatted like try{code} catch(error){console.error(error)}, event listeners to stop certain actions and listen for certain mouse coordinates, while and if statements for looping and conditionals, and referencing of stylesheets and javascript files to clean up my main html file.</li>
<br>
I can honestly say that I could have used my time much more effectively, but I still made many commits (much more towarsd the end to be completely transparent)<br>
to both the frontend and the backend.<br>
My commit graph for October: <br><img src="/matthew-wang/images/commit.png"><br>
Key Commits on Backend:<br>
<a href ="https://github.com/7mwang/Asian-United-Backend/commit/9293f56b2692322839d9772f6c5507422bb0ba47">Started Game</a><br>
<a href ="https://github.com/7mwang/Asian-United-Backend/commit/8166c9c1f311433042a7332e7e7daad0af1bdbdd">Got API Working</a><br>
<a href ="https://github.com/7mwang/Asian-United-Backend/commit/3f4df396a1ad1d3a6a97c08bf5f00ca72e9a3a04">Finished Game Mostly</a><br>
<a href ="https://github.com/7mwang/Asian-United-Backend/commit/2b1d3ed330ed1ae08cbd6981645c3c1dfb6836f2">Username and Pass Saving</a><br>
<a href ="https://github.com/7mwang/Asian-United-Backend/commit/7f7d9ab378daa2b4537cf33f8b394df1f7d6e21a">Login/Registration System</a><br>
<a href ="https://github.com/7mwang/Asian-United-Backend/commit/41a4eacee9d3d654de05f0bfea19f8733cbf3b4e">Top 10 API</a><br>
<a href ="https://github.com/7mwang/Asian-United-Backend/commit/53cc39cde58c627229c03d369e28a0424d96e976">Finalized database, last real change</a><br>
Key Commits on Frontend:<br>
<a href ="https://github.com/JoshThinh/Asian-United-Frontend/commit/be3d3afadade7262f3c558c6e3d13d0d1041b2d3">Moved Game to Front</a><br>
<a href ="https://github.com/JoshThinh/Asian-United-Frontend/commit/e82f7ab1f44bbb559cd8ed085352df8c3d3c3983">Added Login Page, Register Page</a><br>
<a href ="https://github.com/JoshThinh/Asian-United-Frontend/commit/5bb36ba2f7fc36b7f746792341fa80ad80a94068">Finished Leaderboard on Frontend</a><br>
<br>
This is the end of me documenting my CSP Tri 1 Journey :) 