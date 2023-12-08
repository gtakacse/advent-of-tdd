package com.aoc2023

import scala.collection.mutable
object Day04 {

  def getCards(lines: Seq[String]): Seq[(Set[Int], Set[Int])] = {
    lines.map { line =>
      val cards = line
        .split(":")
        .last
        .split("\\|")
        .map(_.trim.split(" +").map(_.toInt).toSet)
      (cards(0), cards(1))
    }
  }

  def part1(cards: Seq[(Set[Int], Set[Int])]): Int = {
    {
      for {
        (winner, me) <- cards
        common = { winner & me }
        score = if (common.isEmpty) 0 else Math.pow(2, common.size - 1)
      } yield score.toInt
    }.sum
  }

  def part2(cards: Seq[(Set[Int], Set[Int])]): Int = {
    cards.zipWithIndex
      .foldLeft(Map.empty[Int, Int]) { case (acc, ((winner, me), idx)) =>
        val common_count = { winner & me }.size
        val n = acc.getOrElse(idx, 0) + 1
        val updated_acc = { idx + 1 to idx + common_count }
          .map(i => i -> { acc.getOrElse(i, 0) + n })
          .toMap
        acc ++ Map(idx -> n) ++ updated_acc
      }
      .map(_._2)
      .sum
  }

  def main(args: Array[String]): Unit = {
    val lines = Utils.getInputLines("2023/day04.txt")
    val cards = getCards(lines)
    println(s"Part 1: ${part1(cards)}")
    println(s"Part 2: ${part2(cards)}")
  }
}
