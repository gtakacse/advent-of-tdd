package com.aoc2023

import scala.util.Using
import scala.io.Source
import scala.util.matching.Regex

object Day01 {

  val DIGITS = Seq(
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
  ).zipWithIndex.tail

  val numberPattern: Regex = "\\d".r

  def find_digits(str: String): Seq[String] = {
    numberPattern.findAllMatchIn(str).map(m => m.matched).toSeq
  }

  def find_digits_with_literals(str: String): Seq[String] = {
    str.zipWithIndex.flatMap { case (ch, idx) =>
      numberPattern.findFirstMatchIn(ch.toString) match {
        case Some(m) => Some(m.matched)
        case _ =>
          val s = str.splitAt(idx)._2
          DIGITS
            .find { case (num_str, num) => s.startsWith(num_str) }
            .map { case (num_str, num) => num.toString }
      }
    }
  }

  def get_calibration_number(digits: Seq[String]): Int = {
    if (digits.size > 0) {
      { digits.head + digits.last }.toInt
    } else {
      0
    }
  }

  def part1(path: String): Int = {
    Using.resource(Source.fromResource(path))(
      _.getLines()
        .map { line =>
          val digits = find_digits(line)
          get_calibration_number(digits)
        }
        .sum
    )
  }

  def part2(path: String): Int = {
    Using.resource(Source.fromResource(path))(
      _.getLines()
        .map { line =>
          val digits = find_digits_with_literals(line)
          get_calibration_number(digits)
        }
        .sum
    )
  }

  def main(args: Array[String]): Unit = {
    val path: String = "2023/day01.txt"
    println(s"Part 1: ${part1(path)}")
    println(s"Part 2: ${part2(path)}")
  }

}
