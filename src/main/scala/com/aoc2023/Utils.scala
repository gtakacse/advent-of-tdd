package com.aoc2023

import scala.util.Using
import scala.io.Source

object Utils {
  
    def getInputLines(path: String): Seq[String] = {
        Using.resource(Source.fromResource(path))(_.getLines.toSeq)
    }
}
