package com.aoc2023

import scala.util.Using
import scala.io.Source
import scala.util.matching.Regex
import java.lang.Math

object Day02 {

    case class Game(id: Int, bags: Seq[RGB]) {

        def isPossible(threshold: RGB): Boolean = {
            bags.forall(_.isValid(threshold))
        }

        def getMinThreshold: Int = {
            val (r, g, b) = bags.foldLeft((0, 0, 0)){ case ((r, g, b), bag) =>
                (
                    Math.max(r, bag.red),
                    Math.max(g, bag.green),
                    Math.max(b, bag.blue),
                )    
            }
            r * g * b
        }
    }

    case class RGB(red: Int, green: Int, blue: Int) {

        def isValid(threshold: RGB): Boolean = {
            red <= threshold.red && green <= threshold.green && blue <= threshold.blue
        }
    }

    def parseRgb(bag: String): RGB = {
        RGB(
            red ="(\\d+) red".r.findFirstMatchIn(bag).map(_.group(1).toInt).getOrElse(0),
            green = "(\\d+) green".r.findFirstMatchIn(bag).map(_.group(1).toInt).getOrElse(0),
            blue = "(\\d+) blue".r.findFirstMatchIn(bag).map(_.group(1).toInt).getOrElse(0)
        )
    } 

    def parseGame(line: String) = {
        val game_id: Int = "^Game (\\d+)".r
            .findFirstMatchIn(line)
            .map(_.group(1).toInt)
            .getOrElse(throw IllegalStateException("Game id not found."))
        val bags = line.split(";").map(parseRgb)
        Game(game_id, bags)
    }

    def part1(path: String, threshold: RGB): Int = {
        Utils.getInputLines(path).foldLeft(0){ case (acc, line) =>
            val game = parseGame(line)
            if (game.isPossible(threshold)){
                game.id + acc
            } else {
                acc
            }
        }
    }

    def part2(path: String, threshold: RGB): Int = {
        Utils.getInputLines(path).map{ line =>
            parseGame(line).getMinThreshold
        }.sum
    }

    def main(args: Array[String]): Unit = {
        val path: String = "2023/day02.txt"
        val threshold = RGB(red = 12, green = 13, blue = 14)
        println(s"Part 1: ${part1(path, threshold)}")
        println(s"Part 2: ${part2(path, threshold)}")
    }
  
}
