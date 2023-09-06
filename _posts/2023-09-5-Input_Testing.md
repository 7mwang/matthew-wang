---
toc: true
comments: true
layout: post
title: Input Testing
description: This is where I will do input testing with forms
type: tangibles
courses: { csp: {week: 2, categories: [4.A]}}
categories: [C1.4]
---
<!-- Create a simple Program to build the Calculator in JavaScript using with HTML and CSS web languages. -->
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
<html>
<body>
<script>
    var num = 0;
    function add() {
        var click = document.getElementById('click');
        num++;
        click.value = String(num);
        document.getElementById('add').value = String(num);
    }
</script>
<form NAME="myform">
    <input TYPE="button" NAME="click" VALUE="0" id="click" onclick="add()">
    <input TYPE="text" ID="add" NAME="result" VALUE="">
</form>
