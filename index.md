---
layout: default
title: Student Blog
---
<section id="introduction"></section>
<!--gives td, or table data a white border of thickness 1 pixel-->
<!--setting background image, and making sure the site looks good and has enough space by expanding minimum height-->
<style>
p{text-alignt: left}
td{
  border:1px solid white;
}
body {
    background-image: url('images/gray-cubes.jpg'); 
    background-repeat: no-repeat;
    background-size: cover;
    min-height: 325vh

}
</style>
<!--creates a section that can be hyperlinked, with id introduction, so if you want to make a link to it it would be "https://www.url.com/#introduction", can be used to go to different sections of a page-->  
<font size ="+5">
<u>
<!--<u> underlines, <span> can be used similarly to <div> but can be used in between lines, while div is used in big chunks/blocks, div is used to make/mark sections (not the same as <section>)-->
    <span style="color:#fffff2;">
    Matthew Wang's CSP Webserver
    </span>
</u>
</font>
<br>
<font size="+2">
<span style="color:#fffff2;">
Hey, my name is Matthew Wang, welcome to my CSP Page! 
<br>
<font size="+1">
<!--<a> is a hyperlink, href is the link/website addon that will be activated when hyperlink is pressed. You can also put a button where it says "down to buttons..." to make it so you click a button to activate the link instead of clicking text-->
<ul>
<li><a id="godown" href="#aboutme">About me!</a></li><br>
</ul>
</font>
<font size="+2">
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><section id="aboutme">
<br><br><br><br><hr><a id="goup" href="#introduction">Back to Introduction...</a><br>
Some things about me:
<!--<ul> = bulletted list, every content in <li> (list) will be bulletted -->
<ul>
<li>I was born in Arizona</li>
<li>I have three sisters, two of which graduated from DNHS</li>
<li>I enjoy reading, as well as playing games in my free time</li>
</ul>
Below is my freeform drawing!
<br>
<!--<img> tag, src = source, "path of image"-->
<img src="images/freeform.png" 
     width="400" 
     height="500"
     align="left"/>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<!--creates a large separator line-->
<hr class="dotted">
<br><br><br><br><br><br><br><br>
<hr>
<section id="accomplishments">
<b>Accomplishments</b>