package com.aoc2023

import org.scalatest.funsuite.AnyFunSuite
import com.aoc2023.Day01._

class Day01Test extends AnyFunSuite {
    test("create calibration number"){
        assert (12 == get_calibration_number(Seq("1", "2")))
        assert (12 == get_calibration_number(Seq("1", "3", "4", "2")))
        assert (11 == get_calibration_number(Seq("1")))
        assert (0 == get_calibration_number(Seq()))
    }

    test("find digits"){
        assert (Seq() == find_digits(""))
        assert (Seq() == find_digits("abcd"))

        assert (Seq("7") == find_digits("bsdf7sdf"))
        assert (Seq("7") == find_digits("7sdf"))
        assert (Seq("7") == find_digits("xsdf7"))
        assert (Seq("7") == find_digits("7"))

        assert(Seq("1", "0") == find_digits("10"))
        assert(Seq("1", "1", "2", "1") == find_digits("1121"))

        assert (Seq() == find_digits("seven"))
        assert (Seq() == find_digits("ten"))
    }

    test("find digits with literal string"){
        assert(Seq() == find_digits_with_literals(""))
        assert(Seq() == find_digits_with_literals("abcd")) 
        
        assert (Seq("1") == find_digits_with_literals("1"))
        assert (Seq("1") == find_digits_with_literals("a1a"))
        assert (Seq("1", "2", "3") == find_digits_with_literals("1ab2cd3ef"))

        assert (Seq("1") == find_digits_with_literals("onebb"))
        assert (Seq("1") == find_digits_with_literals("aone"))

        assert (Seq("1", "8") == find_digits_with_literals("oneight"))

        assert (Seq("1", "2") == find_digits_with_literals("one2"))
        assert (Seq("2", "1") == find_digits_with_literals("2one"))

    }


    test("part1"){
        assert(142 == part1("2023/day01a.txt"))
    }

    test("part2"){
        assert(281 == part2("2023/day01b.txt"))
    }


  
}
