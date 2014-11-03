Asia Miles Data Challenge
=========================

The file data.pdf contains the observation of a study on crabs found around the Boston Area.

The challenge consist of making some sense out of those data. First, extract the data from the dirty PDF file, then perform any kind of analysis you think maybe of interest. We're notably looking for a method to predict the age of a crab given its features.

# Deliverables

## Prediction model

The first deliverable is a program that takes a CSV input from the command line with the following fields, in this order, separated by a comma:

```
Sex, Length, Diameter, Height, Weight, Shucked Weight, Viscera Weight, Shell Weight, Age
```

For example:

```
M,0.3875,0.275,0.1,0.43941725,0.18427175,0.0850485,0.1417475,3
I,0.4,0.275,0.0625,0.510291,0.18427175,0.15592225,0.1417475,3
```

The program should implement your prediction model for the age of the crab for each line, and run it for each line, outputing the predicted age. Given the previous example, the output should have the following fields:

```
Sex, Length, Diameter, Height, Weight, Shucked Weight, Viscera Weight, Shell Weight, Age, Predicted Age
```

and look like:

```
M,0.3875,0.275,0.1,0.43941725,0.18427175,0.0850485,0.1417475,3,3
I,0.4,0.275,0.0625,0.510291,0.18427175,0.15592225,0.1417475,3,4
```

You then need to write another program that takes this output and return meaningful stats about the quality of your predictions. 

Eventually, it should look something like that:

`cat test_dataset.csv | prediction_model | evaluation > stats.log`

The quality and the style of the code and its organization will be evaluated.

You are free to develop in any language of your choice. Clear instruction on how to run/compile the program must be given.

## Presentation

You will be asked to give a presentation about your results. The format is yours to decide, we recommend a presentation no longer than 15 minutes, followed by questions from the audience. As an exercise, assume you are talking to crab-aware people about your finding and how it can help them, but only some of them knows about data mining. You may prepare a summary of your work to be transmitted before the presentation, at your convenience.

You will be evaluated on the following aspects:

- Your reasoning. We want to understand your chain of thoughts and how you reached your conclusion.
- Your results. How good is your prediction model. How good do you think it is, and how good could it be. 
- Your presentations skills. You must be able to present your results to a non-expert audience and defend the validity of your prediction.
