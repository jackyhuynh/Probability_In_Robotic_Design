# Probability_In_Robotic_Design_Handbook
Probability is the fundamental of the Robotic movement. As humans, we use probabilities methods to solve these Robotic movement problem in a variety of ways. 

<img src="https://github.com/jackyhuynh/Probability_In_Robotic_Design/blob/main/images/risk-danger-dial-low.jpg" width="200" height="400">

## Introduction

### Uncertainty in Robotics
Using the word certain the way we'll use it in this handbook, nothing in the previous question is ever certain:

1. What other traffic will do: People are impossible to predict with certainty!
2. Where you are: It may seem like you know where you are when you drive, but you don't. At least not with complete certainty. You may know where you are with sufficient certainty, but if I asked you how many millimeters away from the center lane you were, you wouldn't know.
3. How fast you're going: The same reasoning applies to knowing your speed. You can get a good idea of how fast you're going by looking at your speedometer (which measures your speed), but these measurements are never perfect.
4. What will happen when you turn the wheel: A car is an imperfect mechanical system. If you turned the steering wheel by the same amount 100 times, the car would turn a slightly different amount every time.
As humans, we solve these problems in a variety of ways, but in this handbook, we will solve them using Python (programming languages), and probability(math)

### Probabilistic "Events" in Robotics

![img](https://github.com/jackyhuynh/Probability_In_Robotic_Design/blob/main/images/heads-or-tails.jpeg)

You might be wondering what coins have to do with robotics.
- A coin flip is a perfect example of a probabilistic event: a set of outcomes to some experiment where each outcome has a probability.
- With a coin, the outcomes are clear: heads or tails, and the probabilities are simple: 0.5 and 0.5.
A self-driving car makes hundreds of calculations about probabilistic events every second, but the events are not as clean as a coin flip. For example:
- What is the probability that this sensor measurement is accurate to within 5 centimeters? What about 1 centimeter?
- What is the probability that some other vehicle will turn left at this intersection? Go straight? Turn right? What if they just sit there forever?
- The radar and lidar measurements seem to disagree! What's the probability that the range finder somehow became detached from the roof?
These examples are all much more interesting than "heads or tails?" but they are also less straightforward, which makes it much harder to learn probability theory from them.

### Two Cars

![alt](https://github.com/jackyhuynh/Probability_In_Robotic_Design/blob/main/images/intersections.jpg)

The following questions deal with two cars that have pulled up to an intersection. It is equally likely than any individual car will turn left (L), go straight (S), or turn right (R).
In the notation we are using, P(S, L) means "probability that car one goes straight (S) and car two turns left (L)."

Question 1
For this question, assume the probabilities of left, straight, and right are all equal. That is:
P(L) = \frac{1}{3}P(L)= 1/3	 
P(S) = \frac{1}{3}P(S)= 1/3	 
P(R) = \frac{1}{3}P(R)= 1/3

### Managing Complexity
Roboticists will often use the term state space to describe the set of all possible outcomes for a probabilistic event.
For a coin the state space for a "flip" event can be written mathematically as:
- {H,T}
And for a car at an intersection the state space for a "turn" event can be written mathematically as:
- {L,S,R}
Coins and cars may seem differently, but we can treat them in similar ways when we think in terms of events and state spaces.
In the last question you saw that calculating a truth table for 2 coin flips requires 4 calculations while calculating the truth table for 2 car turns at an intersection requires 9 calculations.
We can make these statements more broadly applicable:
- When calculating the truth table for 2 events which each have a state space size of 2, we need to make 4 calculations.
- When calculating the truth table for 2 events which each have a state space size of 3, we need to make 9 calculations.
And in fact, there's a mathematical pattern here that can be expressed algebraically:
- When calculating the truth table for NN events which each have a state space size of xx, we need to make x^N calculations
- x^N gets very big very fast as x or N get bigger.
How this exponential complexity growth can really slow down the performance of the code running inside of a self driving car.

#### Cars and Probability
Probability is used to analyze sensor data, predict future events, and make decisions. Below we will explore the foundation of probability to be a self-driving car engineer!

## Probability Definition

### Probability
- Now that you have built your sample space and understand the mechanics, it is time to move into some probability.
- Probability can typically be thought of as: Total number of events that could occur/Number of ways an event can occur
​- An "event" is defined as some type of state that can happen. For example, turning "left" or "right" are both events. Similarly, pressing the "gas" or "brake" are also events. All probabilities will be between 0 and 1 inclusive.


​	