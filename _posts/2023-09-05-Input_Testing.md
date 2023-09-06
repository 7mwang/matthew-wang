---
toc: true
comments: true
layout: post
title: Input Testing
description: Here is a space I am currently using to test inputs.
type: tangibles
courses: { csp: {week: 3, categories: [4.A]}}
categories: [C1.4]
---
<html lang = "en">
<head>

<style>
body {
    background-image: url('images/gray-cubes.jpg'); 
    background-repeat: no-repeat;
    background-size: cover;
    min-height: 325vh

}

#clear{
width: 285px;
border: 3px solid gray;
	border-radius: 3px;
	padding: 20px;
	background-color: red;
}

.formstyle
{
width: 301px;
height: 530px;
margin: auto;
border: 3px solid skyblue;
border-radius: 5px;
padding: 20px;
}



input
{
width: 20px;
background-color: green;
color: white;
border: 3px solid gray;
	border-radius: 5px;
	padding: 26px;
	margin: 5px;
	font-size: 15px;
}


#calc{
width: 250px;
border: 5px solid black;
	border-radius: 3px;
	padding: 20px;
	margin: auto;
}

</style>

</head>
<body>
<h1> Calculator Program in JavaScript </h1>
<div class= "formstyle">
<form name = "form1">
	
	<!-- This input box shows the button pressed by the user in calculator. -->
<input id = "calc" type ="text" name = "answer"> <br> <br>
<!-- Display the calculator button on the screen. -->
<!-- onclick() function display the number prsses by the user. -->
<input type = "text" onclick = "form1.answer.value += '' ">
</form>
</div>
</body>
</html>