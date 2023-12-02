package com.aoc2023

import org.scalatest.funsuite.AnyFunSuite
import com.aoc2023.Day02._

class Day02Test extends AnyFunSuite {

    val threshold = RGB(red = 12, green = 13, blue = 14)
    val path = "2023/day02.txt"

    test("RGB parsing") {
        val cases = Seq(
            (RGB(1,3,4), "3 green, 4 blue, 1 red"),
            (RGB(1,3,4), "4 blue, 3 green, 1 red"),
            (RGB(1,3,4), "4 blue, 1 red, 3 green"),
            (RGB(1,3,4), "4 blue, 1 red, 3 green"),

            (RGB(11,2,3), "11 red, 2 green, 3 blue"),
            (RGB(11,0,3), "11 red, 3 blue"),
            (RGB(0,0,0), "")
        )

        cases.foreach{ case (exp, inp) =>
            assert(exp == parseRgb(inp))    
        }
    }
    
    test("game parsing") {
        val cases = Seq(
            (Game(1, Seq(RGB(4,0,3), RGB(1,2,6), RGB(0,2,0))), "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"),
            (Game(1, Seq(RGB(0,0,3))), "Game 1: 3 blue"),
            (Game(1, Seq(RGB(0,0,0))), "Game 1: "),
        )

        cases.foreach{ case (exp, inp) =>
            assert(exp == parseGame(inp))
        }
    }

    test("part 1"){
        assert(8 == part1(path, threshold))
    }

    test("part 2"){
        assert(2286 == part2(path, threshold))
    }

}
