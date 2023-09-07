---
toc: true
comments: true
layout: post
title: Input Testing
description: This is where I will do input testing with forms and javascript
type: tangibles
courses: { csp: {week: 2, categories: [4.A]}}
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

form {
    text-align: center;
    margin: 50px auto;
    max-width: 400px;
    padding: 20px;
    background-color: #fff;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
input{
    padding: 10px 20px;
    font-size: 18px;
    background-color: #3498db;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
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
    var startTime = 0;
    var isTestRunning = false;
    function startTest() {
        if (!isTestRunning) {
            num = 0;
            startTime = Date.now();
            isTestRunning = true;
            document.getElementById('startButton').innerHTML = 'Click!';
        } else {
            num++;
            document.getElementById('add').value = String(num);
            var currentTime = Date.now();
            var timeElapsed = (currentTime - startTime) / 1000; // Convert to seconds
            document.getElementById('timePassed').value = timeElapsed.toFixed(2) + ' seconds';
        }
        }
    function endTest() {
        isTestRunning = false;
        var endTime = Date.now();
        var timeElapsed = (endTime - startTime) / 1000; // Convert to seconds
        var clickSpeed = num / timeElapsed;
        alert('Click Speed: ' + clickSpeed.toFixed(2) + ' clicks per second');
        document.getElementById('startButton').innerHTML = 'Start';
        document.getElementById('add').value = '0';
    }
</script>
<form NAME="myform">
    <input TYPE="button" NAME="click" VALUE="0" id="startButton" onclick="startTest()">
    <input TYPE="text" ID="add" NAME="result" VALUE="0">
    <input TYPE="text" ID="timePassed" NAME="time" VALUE="0 seconds">
    <input TYPE="button" VALUE="Results" onclick="endTest()">
</form>
