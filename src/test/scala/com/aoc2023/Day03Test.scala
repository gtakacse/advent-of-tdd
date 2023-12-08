package com.aoc2023

import org.scalatest.funsuite.AnyFunSuite
import com.aoc2023.Day03._

class Day03Test extends AnyFunSuite {

    val points = getPoints(Utils.getInputLines("2023/day03.txt"))
    val max_col = points.map(_._1._2).max

    test("test finding neigbor numbers"){

        val inp = Seq(
            "123",
            "4*5",
            "678"
        )
        val points = getPoints(inp)
        val max_col = 2
        assert(Seq(123, 4, 5, 678) == findNeighborNumbers(points, 1, 1, max_col))
    
        val inp2 = Seq(
            "...",
            ".*.",
            "..."
        )
        assert(Seq() == findNeighborNumbers(getPoints(inp2), 1, 1, max_col)) 

        val inp3 = Seq(
            "11.22",
            "12*34",
            "33.34",
            "99.*.",
            "...5."
        )
        val points3 = getPoints(inp3)

        assert(Seq(11,22,12,34,33,34) == findNeighborNumbers(points3, 1, 2, 4))
        assert(Seq(34, 5) == findNeighborNumbers(points3, 3, 3, 4))

    }
  
    test("part 1") {        
        assert(4361 == part1(points, max_col))
    }

    test("part 2"){
        assert(467835 == part2(points, max_col))
    }
}
