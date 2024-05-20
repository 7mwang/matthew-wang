---
toc: true
comments: true
layout: post
title: Data Structures Final Project Plan
author: Matthew Wang
description: Final Data Structures Project Ideation
courses: { csp: {week: 33} }
type: plans
---
# The Idea:


My idea for improving this project is to develop an algorithm aimed at the purpose of improving the community aspect of our project, and allow users to somewhat interact with each other.


## Matthew:


Create a way for the users to rate recipes, and sort them by highest rating, lowest rating, most ratings, etc.


- Loops/Iteration:
    - Loop through the list of rated recipes stored in the backend
    - Check each recipe for x parameter, for example category through something like a filter

- Sorting/Searching:
    - Search for specific ratings in the database
    - Sort recipes by rating, and display ordered list to user

- Big O & Time Complexity/Optimization:
    - Test sort time for large samples of data
    - Use python time library in the loop to print out time for each action, and isolate what is causing issues if there are any
    - Make sure run time for small samples/large samples is the same, e.g. each interval is the same

- Deployment:
    - Basic deployment onto AWS
    - Make sure SQlite database is accessible, and connected to the github.io frontend
    - Data needs to be accessible for looping/iterating/sorting/searching to function correctly

![img](https://files.catbox.moe/dsvoev.png)


# Time Allocation


## 5/20
- Finalize plans with team
- Begin researh on how to implement feature

## 5/21-24
- Finish up research, have a concrete idea of how to make the project
- Implement recipe logging, so that starred recipes go into a database

## 5/25-26
- Look back on recipe logging, make more efficient
- Debug sessions

## 5/27-End of Project
- Add filter functionality
- Recipe of the day
- Best recipes sorted by stars
- Possibly add categories, and best recipe by stars on certain category
- Use citizen science to determine categories, ex. "would you say this fits the x category"
