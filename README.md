# Probability_In_Robotic_Design_Handbook
Probability is the fundamental of the Robotic movement. As humans, we solve these probabilities in a variety of ways. 

## Introduction
### Uncertainty in Robotics
Using the word certain the way we'll use it in this handbook, nothing in the previous question is ever certain:

1. What other traffic will do: People are impossible to predict with certainty!
2. Where you are: It may seem like you know where you are when you drive, but you don't. At least not with complete certainty. You may know where you are with sufficient certainty, but if I asked you how many millimeters away from the center lane you were, you wouldn't know.
3. How fast you're going: The same reasoning applies to knowing your speed. You can get a good idea of how fast you're going by looking at your speedometer (which measures your speed), but these measurements are never perfect.
4. What will happen when you turn the wheel: A car is an imperfect mechanical system. If you turned the steering wheel by the same amount 100 times, the car would turn a slightly different amount every time.
As humans, we solve these problems in a variety of ways, but in this handbook, we will solve them using Python (programming languages), and probability(math)

### Probabilistic "Events" in Robotics

!img](https://github.com/jackyhuynh/Probability_In_Robotic_Design/blob/main/images/heads-or-tails.jpeg)

You might be wondering what coins have to do with robotics.
- A coin flip is a perfect example of a probabilistic event: a set of outcomes to some experiment where each outcome has a probability.
- With a coin, the outcomes are clear: heads or tails, and the probabilities are simple: 0.5 and 0.5.
A self-driving car makes hundreds of calculations about probabilistic events every second, but the events are not as clean as a coin flip. For example:
- What is the probability that this sensor measurement is accurate to within 5 centimeters? What about 1 centimeter?
- What is the probability that some other vehicle will turn left at this intersection? Go straight? Turn right? What if they just sit there forever?
- The radar and lidar measurements seem to disagree! What's the probability that the range finder somehow became detached from the roof?
These examples are all much more interesting than "heads or tails?" but they are also less straightforward, which makes it much harder to learn probability theory from them.