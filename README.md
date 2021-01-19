# Probability_In_Robotic_Design_Handbook
Probability is the fundamental of the Robotic movement. As humans, we use probabilities methods to solve these Robotic movement problem in a variety of ways. 

<img src="https://github.com/jackyhuynh/Probability_In_Robotic_Design/blob/main/images/risk-danger-dial-low.jpg" width="400" height="200">

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
- Now that you have built your sample space and understand the mechanics, it is time to move into some probability.
- Probability can typically be thought of as: Total number of events that could occur/Number of ways an event can occur
​- An "event" is defined as some type of state that can happen. For example, turning "left" or "right" are both events. Similarly, pressing the "gas" or "brake" are also events. All probabilities will be between 0 and 1 inclusive.

## Python Basic (Notebook 1 to 10)
Basic Python variables, for loop, if else, control flow. Small exercises about python variables.

## Bayes' Rule

In probability theory and statistics, Bayes' theorem (alternatively Bayes' law or Bayes' rule), named after Reverend Thomas Bayes, describes the probability of an event, based on prior knowledge of conditions that might be related to the event.[1] For example, if the risk of developing health problems is known to increase with age, Bayes' theorem allows the risk to an individual of a known age to be assessed more accurately (by conditioning it on their age) than simply assuming that the individual is typical of the population as a whole.

One of the many applications of Bayes' theorem is Bayesian inference, a particular approach to statistical inference. When applied, the probabilities involved in the theorem may have different probability interpretations. With Bayesian probability interpretation, the theorem expresses how a degree of belief, expressed as a probability, should rationally change to account for the availability of related evidence. Bayesian inference is fundamental to Bayesian statistics.
[Wikipedia](https://en.wikipedia.org/wiki/Bayes'_theorem#:~:text=In%20probability%20theory%20and%20statistics,%20Bayes'%20theorem%20(alternatively,conditions%20that%20might%20be%20related%20to%20the%20event.).

### Keyworld: 
Prior
Posterior
Normalizer (Normalizing Probabilty)
Total probability
Bayes Rules Diagram
Equivalent Diagram:
So, this should be stated as:
- P(Pos, C) = P(Pos|C) P(C)
- P(Neg, C) = P(Neg|C) P(C)
- P(Pos, ~C) = P(Pos|~C) P(~C)
- P(Neg, ~C) = P(Neg|~C) P(~C)

### Robot Sensing Example
#### Step by Step Walkthrough
The step-by-step breakdown of the solution is pretty quick. Let's recap what's covered in the solution video.
Let's start with what we know:

#### Prior Probabilities
- The robot is perfectly ignorant about where it is, so prior probabilities are as follows:
- P(at red)=0.5
- P(at green)=0.5

#### Conditional Probabilities
- The robot's sensors are not perfect. Just because the robot sees red does not mean the robot is at red.
- P(see red∣at red)=0.8
- P(see green∣at green)=0.8

#### Posterior Probabilities:
From these prior and posterior probabilities we are asked to calculate the following posterior probabilities after the robot sees red:
- P(at red∣see red)
- P(at green∣see red)
and as a reminder, Bayes' rule looks like this:
- P(A|B ) = (P(B|A) * P(A))/P(A∣B)= 
or, if we want to use our "versions" of A and B (for posterior #1)...
- P(at red|see red ) = (P(see red|at red) * P(at red))/P(see red)
Now, we can read two of those terms from what we already know about our prior and conditional probabilities which means we can rewrite this as...
- P(at red|see red ) = (0.8 * 0.5)/P(see red)
But we still have one unknown! What was the probability that we would see red? The answer is 0.5 and there are two ways I can convince myself of that. The first is intuitive and the second is mathematical.

#### Why is P(see red) 0.5?
Argument 1: Intuitive
- Of course it's 0.5! What else could it be? The robot had a 50% belief that it was in red and a 50% belief that it was in green. Sure, its sensors are unreliable but that unreliability is symmetric and not biased towards mistakenly seeing either color.
- So whatever the probability of seeing red is, that will also be the probability of seeing green. Since these two colors are the only possible colors the probability MUST be 50% for each!

Argument 2: Mathematical (Law of Total Probability)
There are exactly two situations where the robot would see red.
* When the robot is in a red square and its sensors work correctly.
* When the robot is in a green square and its sensors make a mistake.
I just need to add up these two probabilities to get the total probability of seeing red.
P(see red) = P(at red) * P(see red|at red) + P(at green)*P(see red|at green)
I can read these quantities from above!
P(see red)= 0.5 * 0.8 + 0.5 * 0.2
P(see red)= 0.4 + 0.1
P(see red)= 0.5

# Introduce to Probability Distribution

## What is a Probability Distribution?
Probability distributions allow you to represent the probability of an event using a mathematical equation. Like any mathematical equation:

- probability distributions can be visualized using a graph especially in 2-dimensional cases.
- probability distributions can be worked with using algebra, linear algebra and calculus.
- These distributions make it much easier to understand and summarize the probability of a system whether that system be a coin flip experiment or the location of a self-driving car.

## Types of Probability Distributions
Probability distributions are really helpful for understanding the probability of a system. Looking at the big pictures, there are two types of probability distributions:

- discrete probability distributions
- continuous probability distributions
- Before we get into the details about what discrete and continuous mean, take a look at these two visualizations below. The first image shows a discrete probability distribution and the second a continuous probability distribution. What is similar and what is different about each visualization?

