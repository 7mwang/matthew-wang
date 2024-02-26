---
toc: true
comments: false
layout: post
title: Final Review | CPT, CB Reqs, & more
author: Matthew Wang
description: A reflection of my work this trimester on our CPT project including my contributions, experience, and results, as well as a trimester-wide summary of how I worked on and experienced CSP.
courses: { csp: {week: 24} }
type: tangibles
---


# CB Reqs | What specifically are the requirements?


Below is a list of all the requirements for the CPT project in CSP, found on the College Board website.


<img src = "https://files.catbox.moe/zk2afu.png">


I will be going over how our project and specifically my feature fulfills these requirements below, after going over the general idea of our project.


# CPT | Project Planning


<a href = "https://github.com/DavidL0914/frontcasts/issues/2">Issue with our initial plans</a>


# CPT | The aim of the Project

- Create a cooking/baking focused website
    - Allow users to search recipes fetched from an already existing API
    - Allow users to post on a dynamically updating forum that has all of its data stored in a database
    - Create an admin panel for administators to manage user data
    - Let users edit their own personal settings that won't apply to all users, and persist those changes across site pages 


# CPT | What did I contribute?


## Main Individual Feature:


### Recipe Searching function


<img src = "https://files.catbox.moe/6egqg4.png">


## Other things I created:


- Admin panel that includes 3/4 CRUD Operations and is only accessible if the user accessing it has the "admin" role
    - Read: Read all data from database
    - Update: Update users' usernames
    - Delete: Delete users from the database

<img src = "https://files.catbox.moe/42urt0.png">

<img src = "https://files.catbox.moe/qakkbp.png">


- Security features
    - Redirecting the user to the login page if they try to access features without being signed in


# CPT | How our Project and my Feature Fulfills CB Requirements


## First requirement:


<img src = "https://files.catbox.moe/bw87jk.png">


My main feature allows the user to input what they want to search, and click a button which triggers a search function that sends a request to an API, which returns JSON-serialized data, which is then interpreted and formatted by a function, and displayed on the page. The user's search query and clicking of the button serves as the user input. Clear instructions are also provided to the user about how to use the page, and how to interpret the given response.


User input and instruction in code:


<img src = "https://files.catbox.moe/lwhngp.png">


Main event (event that causes site to be updated and data to be visible to user) that occurs as a result of the user input/actions:


<img src = "https://files.catbox.moe/4kdhnp.png">


There are also two functions that go into getting data for displaying by using API fetches, but this function is the one that displays all the data to the user, and allows the user to interact with the data.


## Second Requirement:


<img src = "https://cdn.discordapp.com/attachments/1059758784509116476/1211548158770024469/image.png?ex=65ee9926&is=65dc2426&hm=f1cc5cc56350a277d00c8b9f7dc0a2bbc8c61a9603909558970489821617f745&">


One of example of use of a list or other storage type, in our case dictionaries, in our project occurs when a user tries to access the admin panel used to update user data.


<img src = "https://media.discordapp.net/attachments/1059758784509116476/1211549585369993266/image.png?ex=65ee9a7a&is=65dc257a&hm=99d2db03b80d0eed40db2015247a7b0b661297c8fc7c4435f377dc279904ab5d&=&format=webp&quality=lossless">


When the user triggers the function "update()" via clicking a button's onclick event attribute, the user's inputted data is packed into a dictionary, and sent as data to the backend. This is one of the most common places where dictionaries are seen in our project, as it is much easier to send data this way, and parse it on the backend.


After the data is sent to the backend, the data is managed in the backend API, where data storage is once again used.


<img src = "https://media.discordapp.net/attachments/1059758784509116476/1211550248716083281/image.png?ex=65ee9b18&is=65dc2618&hm=0d6dbf6e7d2cd7b4e3eed08869cb4a7318962c6e961df0f610ac46c866803156&=&format=webp&quality=lossless">


Here, after getting the JSON data from the request, the function accesses data from a database, and packs it into "user", where the data can be easily filtered.


Using different types of data storage, we are able to easily manage and iterate through data, making our project more organized and simple.


## Third Requirement:


<img src = "https://media.discordapp.net/attachments/1059758784509116476/1211551019771887616/image.png?ex=65ee9bd0&is=65dc26d0&hm=5c846af57b8c7d7dc9add9888de56c53ff466d17690114e18cf01794b5f2c58c&=&format=webp&quality=lossless">


In our project, we have numerous procedures that all contribute to the functionality of our project.


Specifically, citing an example different than the one I used for the second requirement, we have a delete() function under the class _CRUD which is also under the class UserAPI.


<img src = "https://cdn.discordapp.com/attachments/1059758784509116476/1211553032597278770/image.png?ex=65ee9db0&is=65dc28b0&hm=edca89bc2ba99fe4a38a2c61463ac81e6e50d2806b3ccb3cb71980cbfda050c5&">


Here, the procedure's name is _CRUD.delete(), the return type is JSON, specified by the jsonify() function used to turn the data into JSON-serialized data in the return, and the only parameter used is the uid, which is defined by "uid = body.get('uid')"


## Fourth Requirement:


<img src = "https://media.discordapp.net/attachments/1059758784509116476/1211554579984941097/image.png?ex=65ee9f21&is=65dc2a21&hm=20cd1a00c38b1d7cb3000a47b21d42644b355fe0b6f907afcd6f4496e33a3f57&=&format=webp&quality=lossless">


<img src = "https://media.discordapp.net/attachments/1059758784509116476/1211557301580726363/image.png?ex=65eea1aa&is=65dc2caa&hm=4d392b089c257b8ac52bf580cf06dc34caa0771e33b1733ad2ee84c492d52c9a&=&format=webp&quality=lossless&width=550&height=305">


This algorithm on our frontend runs as follows:


### First function:


- Fetch data from api
- Handle repsonse data
- Determine user access through cookies
- If user access is granted (admin user), display table title, and data in a table by calling second function
- If user access is not granted, display an "Unauthorized" message


### Second function:

- Use the "data" variable from the previous function
- Iterate through the data, and append each data value to the table
- Return completed table 


## Fifth Requirement


<img src = "https://media.discordapp.net/attachments/1059758784509116476/1211557849759486003/image.png?ex=65eea22d&is=65dc2d2d&hm=af2ef136638ba1f830ccd4b5e423ab12edec5badd3d9ca966f5dae46bb98c56c&=&format=webp&quality=lossless">


All of the functions that we create are called, whether that be through window.onload, event listeners, or onclick attributes. In the case mentioned in the fourth requirement, the function is called through a window.onload, meaning that as soon as the page loads, the function will run without any user input. 


<img src = "https://media.discordapp.net/attachments/1059758784509116476/1211558244464599050/image.png?ex=65eea28b&is=65dc2d8b&hm=4b1eb1742b715e571cd06fe6d7430dd853969904ec76d70bb901bc4572608b01&=&format=webp&quality=lossless">


## Sixth Requirement


<img src = "https://media.discordapp.net/attachments/1059758784509116476/1211558398345084978/image.png?ex=65eea2af&is=65dc2daf&hm=c10eb28fef2ac25d48e61aabc42b78df91a6b387345f3b08da342798db06edd8&=&format=webp&quality=lossless">


Again, in the case mentioned in the fourth requirement, there are several outputs that can occur.


1. The user has access, meaning they are an admin user, and the data is displayed


<img src = "https://media.discordapp.net/attachments/1059758784509116476/1211560871726157875/image.png?ex=65eea4fd&is=65dc2ffd&hm=37db02b3a3ffbe08d98525be7071f915e92ff190f54ec05dd47429a067c615ce&=&format=webp&quality=lossless">


2. The user has no access, meaning they are a default user, and instead of the data being displayed, they are told through updating an element on screen that they are "Unauthorized" to see the data.


<img src = "https://media.discordapp.net/attachments/1059758784509116476/1211561078040039466/image.png?ex=65eea52e&is=65dc302e&hm=820ba045cda6d0f874ee19e3d16306a2835798b0b9eab0a5d29d5ceb8d3b6abc&=&format=webp&quality=lossless">


# CPT | All Commits


<img src = "https://cdn.discordapp.com/attachments/1059758784509116476/1211566989663936532/image.png?ex=65eeaab0&is=65dc35b0&hm=60da7d785a9bc4d54b78ea6b4d2fe8a2b39e69db280bd805f60a1111d3a7c1d1&">


<img src = "https://cdn.discordapp.com/attachments/1059758784509116476/1211567025768366141/image.png?ex=65eeaab8&is=65dc35b8&hm=b9c74a87e37de94a0f3880400d99672a8de5bb2e179ff0f9f9420ca062152a4c&">


My total commits and commit graph for February (2 other repositories are my personal blog and personal project, totalling an extra 4 commits that aren't CPT related)


<a href = "https://github.com/DavidL0914/frontcasts/commits?author=7mwang">My commits to the frontend</a>


<a href = "https://github.com/DavidL0914/backcasts/commits?author=7mwang">My commits to the backend</a>

## Favorite/Key Commits - Frontend:


- <a href = "https://github.com/DavidL0914/frontcasts/commit/e6ae6d5dad7a6d3ce7ddd06a48c2cafea4a10785">Finally making cookies work</a>
- <a href = "https://github.com/DavidL0914/frontcasts/commit/8975aeebf7284848f7a32427373313d3cc15e537">Finishing my individual feature</a>


## Favorite/Key Commits - Backend:


- <a href = "https://github.com/DavidL0914/backcasts/commit/2b654b474bacd30c9c2f9cb7f078019608a817df">Implementation of admin and roles</a>


# Personal | Overall Trimester Experience


Honestly, this trimester has had a lot of ups and downs. Similarly to last trimester, I have had to spend countless hours debugging issues that weren't really mentioned here at all. I spent many hours on debugging cookie saving issues, authorization issues, data parsing issues, among many other things. It's not that I'm particularly upset to have spent so much time on these things, but I just wish I were smarter, and could have figured out these things faster instead of spending up to 5 hours per debugging session, of which I had multiple, trying to fix issues that ended up resolving in one line of code. There were things that, honestly to my surprise, worked instantly, and things that took a lot of time to implement. Recently, I've spent a lot of time trying to figure out cross-domain cookie issues, spending time on the Ubuntu terminal changing nginx configurations, and both of the repos I am working on, as well as the github pages for my frontend. I still honestly have not resolved these issues, but hope to resolve them during finals week. Debugging has had me working hours upon hours a day in heavy work-weeks, but not every week was like that, thankfully. 




Other than all the debugging, my group was also completely shifted as a result of my previous actions, or rather inaction to change my backend logic. After switching groups, I quickly acclimated to the new system, though, so if anything, given how much more organized I can be with the new system, this was a blessing.




As for good things that happened this trimester, I was pretty satisfied when I got my features, to work, and I think I gained a lot of experience this trimester. Though not everything I worked on ended up making it into the CPT project, I am completely okay with that, as I've learned a lot already and can apply this knowledge to my future projects, both in class and out. 




I also learned a lot more about working in a team through this project. I really couldn't have done anything without my team, as we frequently communicated about not only what we were doing and helping each other, but also when we were pushing and telling others when to pull. We didn't end up using pull requests, as once we figured out how to use them, we had completed most of our project, but using this system, we were able to keep each other updated on changes, and tell each other to pull so that not every commit would have loads of merge conflicts.




Overall, I think this was a new and challenging but welcomed experience. I think this will better prepare me for my future, as I do want to pursue computer science later in life, as well as preparing me for trimester 3. 