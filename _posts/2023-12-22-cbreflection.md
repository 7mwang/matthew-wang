---
toc: true
comments: true
layout: post
title: College Board Practice MCQ Reflection
description: College Board Practice MCQ Reflection
courses: {csp: {week: 13}}
type: plans
permalink: reflection
---
To prepare for the College Board Practice MCQ, I did a couple things:

Most notably, I went through the first MCQ that we did, and reviewed not only what I got wrong, but I quickly went through the entire test to refresh myself on the concepts I would need to know. I then went through the team teaches that were presented throughout these past few weeks, and reviewed them briefly so I could get a better understanding of the content they taught. This way, I wouldn't be having huge holes in my comprehension of the content that college board would have taught me, and I wouldn't have to go through and watch all of the videos. Instead, I could use the resources I already have access to, and not waste my time. I also gained experience in CSP testing, as we don't really do many MCQ's in our regular curriculum. I wasn't was pressed for time as I hoped to be, but I was still able to remain pressured for the duration of me actually taking the exam. This did lead me to get a lower than normal score, but I think over time, the pressure will definitely be beneficial to me. It will further prepare me for the AP test, and will familiarize me with the feeling of time pressure, so I feel more comfortable during the exam. 

# Learnings

Through this MCQ, I discovered more of my weaknesses and what I need to practice more of. A commonality between this MCQ and the first MCQ that we did was the logic gate problems. They proved especially confusing for me, so I need to and will go back and review how they work. I also got a better understanding of psuedo code, and looping, despite getting a couple of the problems wrong. Looking back at why I got those questions wrong, I definitely now have a better understanding of the syntax of CB's psuedo code. 

## Test Corrections
# Format:

Question topic summed up in a couple words

My answer

Correct answer

Reasoning

# Q2: Citizen Science

My answer: C

The image analysis is likely to require complex research methods.

Correct answer: D

The image analysis is likely to take a longer time for the research team than for a distributed group of individuals.

Citizen science is incorporated here because if the image analysis is distributed to more people, they can complete it faster. It doesn't really have much to do with complexity.

# Q5: Logic Gates

My answer: B

A = true,  B = false, C = false, D = true

Correct Answer: C

A = false, B = true,  C = true,  D = true

One of A&B must be true for the OR gate to output true, and both inputs to the C&D AND gate must be true for it to output true. Finally, the two true outputs are put into an AND gate, and since they are both true, it will output true.

# Q16: Terminating a Loop

My answer: A

Inserting index <- index + 1 between lines 6 and 7

Correct answer: D

Inserting index <- index - 1 between lines 7 and 8

This ensures that every element is checked over, instead of only removing 1 from index if the if statement is fulfilled.

# Q23: Flow chart logic

My answer: C

available <- weekday or miles >= 20

Correct answer: D

available <- weekday and miles >= 20

In the flow chart, both conditions must be met for available to be true, not just one. Using "and" instead of "or" guarantees that both must be true in order for available to be true, and not just one.

# Q34: Moving a robot to an end goal

My answer: B

Move once, rotate 1 time, move again
Move once, rotate 2 times, move again
Move once, rotate 3 times, move again

Correct answer: C

Move once, rotate 1 time, move again
Move once, rotate 3 times, move again
Move once, rotate 0 times, move again

I got this wrong due to a lack of visualization on my part. I had trouble visualizing the robot's movement.

# Q39: Error in calculating sum

My answer: B

Line 3 should be changed to REPEAT UNTIL (i ≥ 10).

Correct answer: C

Lines 5 and 6 should be interchanged.

The error in the code had nothing to do with the amount of times it was looping. It had to do with the incrementing of variable i occruring before the sum was calculated. Since the loop would terminate after i > 10, if the incrementing took place before the sum was calculating, the loop would stop. The sum must be calculated before i increments to avoid accidental loop termination. 

# Q44: Connections terminated to lose connection

My answer: C

Three connections removed

Correct answer: B

Two connections removed

I got this wrong because I didn't account for just completely ostracizing U from the rest of the devices, which would have just completely stopped all connection in only 2 steps.

# Q45: Coin Flip Sim

My answer: C

Flip coin, check if all 3 coins have the same value, only winning if the result is all of heads/tails

Correct answer: D

Flip coin, check if all 3 coins have the same value, win if all have same value

I didn't account for all of the numbers flipping and outputting 0, and only checked for 3. The coin has 2 sides, so the results of 3 flips can either be 0, 0, 0, or 1, 1, 1.

# Q50: Algorithms completed in a resonable amount of time

My answer: B

An algorithm that acccesses only the first 10 elements in the list, regardless of the size of the list

Correct answer: D

An algorithm that accesses each element in the list twice

An algorithm that accesses each element in the list n times

An algorithm that accesses only the first 10 elements in the list, regardless of the size of the list

For an algorithm to run in reasonable time, it must take a number of steps less than or equal to a polynomial function. Algorithm I accesses elements times (twice for each of n elements), which is considered reasonable time. Algorithm II accesses elements (n times for each of n elements), which is considered reasonable time. Algorithm III accesses 10 elements, which is considered reasonable time.

# Q53: Crowdsourcing

My answer: D

A mobile application that transmits a message to all users any time a lost pet is returned to its owner

Correct answer: C

A mobile application that allows users to report the location of a pet that appears to be lost and upload a photo that is made available to other users of the application

My answer sends messages to individuals, but doesn't get their help. The correct answer allows many users to upload information, which would help in the finding of the pet.