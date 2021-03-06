# Probability_In_Robotic_Design_Handbook

Probability is the fundamental of the Robotic movement. As humans, we use probability methods to solve these Robotic movement problems in a variety of ways. This project is the combination of Python basic (function & data structures) and math (probability) to solve real-world problems. The src code file contains many small notebooks which each will solve one probability problem.
There is 30 problems and each one is contain in diffrent notebook (store in src folder).


<img src="https://github.com/jackyhuynh/Probability_In_Robotic_Design/blob/main/images/risk-danger-dial-low.jpg" width="400" height="200">

## Programming Probability Distributions

It's time to get more experience programming in Python. Probability distributions involve algebraic functions and visualizing those functions.

You'll start out by making a few basic functions to calculate and visualize continuous uniform probability distributions.

Then, you'll program a more complex distribution: a non-uniform discrete probability distribution.

Next, you'll use those skills to explore how a self-driving car, or really any robot, might represent its location probabilities in a discrete, 1-D world. Then you'll expand into probabilities in a 2-D world. You're going to implement the 2-D world using something called a class, which is a sort of programming template. You'll learn more about classes in the exercises.

Finally, you'll become familiar with a probability distribution that is especially important to self-driving cars: the normal distribution.


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

![Img](https://github.com/jackyhuynh/Probability_In_Robotic_Design/blob/main/images/probability-distributions.jpg)

# Discrete vs. Continuous Variables

## Discrete Variables

As mentioned before, there are two main categories of probability distributions: discrete probability distributions and continuous probability distributions. To see the difference, let's talk about discrete variables and continuous variables.

The word discrete implies that a variable can only take on certain values. Usually this ends up meaning that the variable is countable like:

- Number of times a coin landed on heads
- How many times a dice landed on 1, 2, 3, 4 5 or 6

![img](https://github.com/jackyhuynh/Probability_In_Robotic_Design/blob/main/images/discrete-variables.jpg)

You wouldn't say that a dice landed midway between 3 and 4 like 3.4. Or that the coin landed on heads and a half. And oftentimes these discrete variables lend themselves to counting like:

- How many times did the coin land on heads?
- How many times did the dice land on five?
Of course, in a real-world experiment, the coin has some tiny tiny chance of landing on its side or the dice on an edge. But the case would still be discrete; you'd create an category like "side" or "edge" to account for those cases.

## Continuous Variables

In contrast, a variable like temperature is continuous. Temperature can take on any decimal value like -5.6 or 100.41 degrees.

Weight, height, temperature, longitude, and latitude are continuous variables. All of these variables could be decimal values. These variables have something else in common; you'd use some sort of instrument to measure them like a thermometer, a ruler, a scale or in the case of longitude, a chronometer.

Notice as well that you can't really associate counts with these variables. With a discrete variable like coins, you could count the number of times the coin landed on heads.

![img](https://github.com/jackyhuynh/Probability_In_Robotic_Design/blob/main/images/continuous-variables.png)

Thermometer, Tape Measure and Scale. Examples of Continuous Variables

The probability distributions for discrete variables and continuous variables are different. 

## Continuous Probability Distributions

The discrete distribution is broken up into slices. Each slice represents an outcome like zero heads, one heads, two heads, or three heads.
The continuous distribution has an un-broken line across the entire x-axis range. You could have a velocity of 20 or 20.5 or -10.451.
Notice the y-axis label on the continuous distribution: "probability density function". For the discrete probability distribution, the y-axis represented the probability of an event occurring. In the continuous case, the probability density function does not represent probability directly; instead, the area underneath the density function curve represents probability.
You'll learn more about this in the next part of the lesson.
But without knowing what "probability density function" even means, you can tell that it's more likely that the velocity is around 20 and less likely that the velocity is around 0 or 40.

## Characteristics of a Continuous Distribution

Here are a few characteristics of a continuous distribution and the probability density function. Keep these in mind as you go through the next part of the lesson.
- The y values must be greater than or equal to 0.
- The probability of a specific x value occurring is equal to 0
- The probability of an event occurring between two values of x is equal to the area under the curve between those two x values.
- The total area under the probability density function curve is equal to 1.
In practice, these rules mean that the probability that velocity equals exactly 20 is zero. For a continuous distribution, you can only calculate a probability between a range of values like 19.99 and 20.01.
Because the total area under the curve is 1, there is a 100% chance that the velocity has some value between negative infinity and positive infinity.

## Uniform Continuous Distribution

There are many different types of continuous distributions: link to list of continuous [probability distributions](https://en.wikipedia.org/wiki/List_of_probability_distributions#Continuous_distributions).
But they all have the same characteristics described above. To calculate probabilities with a continuous distribution, you have to calculate the area underneath a curve. Calculating the area under a curve like in the above visualization requires calculus or a software program.
So Sebastian has chosen to use a specific continuous distribution called the uniform continuous distribution. The uniform continuous distribution forms a rectangle. So you can calculate the area underneath the curve simply by multiplying the base by the height.
Below is an example of a uniform continuous probability distribution. Sebastian will explain more about where this distribution comes from and how to use it.

![img](https://github.com/jackyhuynh/Probability_In_Robotic_Design/blob/main/images/uniform-continuous.png)

## What Is A Density Function?

For a continuous probability distribution, the y-axis represents a probability density function.
A density function is just an equation to mathematically represent a continuous distribution. If you're familiar with calculus, the integral of the probability density function is the probability. If you're not familiar with calculus, not to worry! You do not need calculus for this section. Taking the integral is the same as calculating the area under the curve.
It's relatively easy to calculate the area underneath a uniform continuous probability distribution. These distributions look like rectangles, so the area is the base of the rectangle times the height of the rectangle.

## Piece-Wise Continuous Probability Distributions

The probability distribution you just learned about sort of looks like a discrete probability distribution. But in fact, it is still a continuous distribution. It's called a piece-wise continuous distribution. If you're unfamiliar with piecewise functions, it just means that the function is divided into parts: check out this link for more examples.

## How To Tell If This Is Continuous Or Discrete?

Ask yourself, is my variable of interest continuous or discrete? Hour, in this case, is a continuous variable because hour can be any decimal value between 0 and 24. So this is a continuous probability distribution.

You could rephrase this problem to make it discrete. If you counted how many people were born between 1am-2am, 2am-3am, 3am-4am, etc, the problem becomes discrete. You are slicing the hour variable so that it can only take on specific values ie 1, 2, 3, 4, 5, etc.

## Technology
- Python 
- Object Oriented Design
- Jupyter Notebook
- Data Visualization
- Machine Learning
- AI
- Localization
- Data Structures

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
What things you need to install the software and how to install them
- Jupyter Notebook: If you want just test the code, simply go to google and search for jupiter notebook or another Python online IDE. The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. 
- Anacoda Navigator: Install Anaconda Navigator if you want to develop data sciences using python or R. Anaconda Navigator is a desktop graphical user interface included in Anaconda that allows you to launch applications and easily manage conda packages, environments and channels without the need to use command line commands. 

### Installing

A step by step series of examples that tell you how to get a development enviroment running

* [Install Anacoda Navigator](https://docs.anaconda.com/anaconda/navigator/install/#:~:text=Installing%20Navigator%20Navigator%20is%20automatically%20installed%20when%20you,install%20anaconda-navigator.%20To%20start%20Navigator,%20see%20Getting%20Started.) - If you haven't downloaded and installed Anacoda Navigator yet, here's how to get started.
* [Jupyter Notebook](https://jupyter.org/try) - Click here to go to the online free Jupiter Notebook.


## Running the tests

Explain how to run the automated tests for this system:
- There is no download IDE need, all you need is download all the src to your machine and run it.
- Using Jupiter Notebook
- Navigate to the file .ipynb
- hit:

```
Ctrl + Enter
```

## Deployment

All the notebook can be used for research and academic basic function for Python. class can be deploy and ready to work as support function. Idea for localization and/or GPS application. This is actually what we use for driving direction everyday. According to Sebastian, this technology have been around for 35 years, and still helping human each day.
Please refer to my notebook for a better understanding of implementation.

## Built With

* [Jupyter Notebook](https://jupyter.org/try) 

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Truc Huynh** - *Initial work* - [TrucDev](https://github.com/jackyhuynh)

## Format
my README.md format was retrieved from
* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Udacity.com for design an outstanding program for Students.
