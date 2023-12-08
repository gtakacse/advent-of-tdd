package com.aoc2023

import org.scalatest.funsuite.AnyFunSuite
import com.aoc2023.Day04._

class Day04Test extends AnyFunSuite {

  val path = "2023/day04.txt"
  val cards = getCards(Utils.getInputLines(path))

  test("part 1") {
    assert(13 == part1(cards))
  }

  test("part 2") {
    assert(30 == part2(cards))
  }

}
