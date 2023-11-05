# Advent of TDD

A follow along workshop to introduce the idea and concepts of using TDD for [Advent of Code](https://adventofcode.com) problems.

## Introduction

In this workshop you will use the Day 1 problem from Advent of Code 2022.
In the following exercises you will review the day 1 instructions, design and implement your tests first.
We will guide you on some of the design and thought process behind each exercise.
A branch will be given at the end of the exercise with a possible solution.

## Exercises

### Exercise 1, Part 1: Breaking up the Problem - Unit Testing 

Start by reading the instructions for [Part 1](day1-part1.md).
As with regular requirements, there's a lot of extra information surrounding what you need to implement.
To solve the first part of the problem there are a few pieces to consider.
You are not going to go straight to getting the answer required by the exercise, instead we are going to start by focusing on the `Elf`.

Looking at the problem the `Elf` is a key domain object and is a good place to start.
Approaching this problem I would look at the requirements and note that we are likely going to be reading line-by-line a file.
Each blank line represents the creation of a new `Elf`.
This exercise is going to be quite simple, but let's focus on creating the following tests.

* Create an `Elf` and `assertThat` it has `getTotalCalories` of 0. 
This is our post condition of creating an `Elf`.
* Now let's use the example case to `addCalories(1000)` and call `getTotalCalories` to `assertThat` it is equal to 1000.
* Now let's `addCalories(1000)`, `addCalories(2000)`, `addCalories(3000)` and call `getTotalCalories` to `assertThat` it is equal to 6000.
* Given that we're going to need to find the max calories, we're going to need to compare `Elf`s together. 
Let's use the Java standard for Comparing (e.g. `Comparable<Elf>`) to write some tests to compare `Elfs` for their total calories
You only need two tests for this.

Check your solution against the `exercise-1` branch.

### Exercise 2, Part 1: Spike - Reading in Input

### Exercise 3, Part 1: Integration Testing

### Exercise 4, Part 2: A New Part of the Problem