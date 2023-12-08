package com.aoc2023

import scala.util.Using
import scala.io.Source
import scala.util.matching.Regex

object Day03 {

  val NEIGHBORS = Seq(
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
  )

  def getPoints(lines: Seq[String]): Map[(Int, Int), String] = {
    for {
      (line, r) <- lines.zipWithIndex
      (char, c) <- line.trim().zipWithIndex
    } yield (r, c) -> char.toString
  }.toMap

  def isSymbol(char: String): Boolean = {
    "[^\\d\\.]".r.matches(char)
  }

  def isDigit(char: String): Boolean = {
    "\\d".r.matches(char)
  }

  def getNumerCoordinatesInRange(
      range: Range,
      points: Map[(Int, Int), String],
      row_idx: Int
  ): Seq[(Int, Int)] = {
    range
      .takeWhile(col_idx =>
        points.get((row_idx, col_idx)).isDefined && isDigit(
          points((row_idx, col_idx))
        )
      )
      .map(col_idx => (row_idx, col_idx))
  }

  def getAdjacentDigits(
      points: Map[(Int, Int), String],
      coord: (Int, Int),
      max_col: Int
  ): Seq[(Int, Int)] = {
    assert(points.contains(coord))

    points.get(coord) match {
      case Some(n) if isDigit(n) =>
        val prefix = getNumerCoordinatesInRange(
          { coord._2 - 1 to 0 by -1 },
          points,
          coord._1
        ).reverse
        val postfix = getNumerCoordinatesInRange(
          { coord._2 + 1 to max_col },
          points,
          coord._1
        )

        { prefix :+ coord } ++ postfix
      case _ => Seq()
    }
  }

  def findNeighborNumbers(
      points: Map[(Int, Int), String],
      r: Int,
      c: Int,
      max_col: Int
  ) = {
    val offsets = NEIGHBORS.filter { case (dr, dc) =>
      isDigit(points((r + dr, c + dc)))
    }
    val number_coords = offsets.map { case (dr, dc) =>
      getAdjacentDigits(points, (r + dr, c + dc), max_col)
    }.distinct
    number_coords.map(coords => coords.map(rc => points(rc)).mkString("").toInt)
  }

  def part1(points: Map[(Int, Int), String], max_col: Int): Int = {
    points
      .filter { case (_, v) => isSymbol(v) }
      .flatMap { case ((r, c), _) =>
        findNeighborNumbers(points, r, c, max_col)
      }
      .sum
  }

  def part2(points: Map[(Int, Int), String], max_col: Int): Int = {
    points
      .filter { case (_, v) => v == "*" }
      .map { case ((r, c), _) =>
        val nums = findNeighborNumbers(points, r, c, max_col)
        if (nums.size == 2) {
          nums(0) * nums(1)
        } else 0
      }
      .sum
  }

  def main(args: Array[String]): Unit = {
    val data = Utils.getInputLines("2023/day03.txt")
    val points = getPoints(data)
    val max_col: Int = points.map((rc, _) => rc._2).max
    println(s"Part 1: ${part1(points, max_col)}")
    println(s"Part 2: ${part2(points, max_col)}")
  }
}
