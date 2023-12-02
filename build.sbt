ThisBuild / scalaVersion := "3.3.1"


lazy val AoC = project
  .in(file("."))
  .settings(
  name := "AdventOfTDD",
  libraryDependencies ++= Seq(
    "org.scala-lang" %% "toolkit" % "0.1.7",
    "org.scala-lang" %% "toolkit" % "0.1.7" % Test,
    "org.scalatest" %% "scalatest" % "3.2.15" % "test"
    )
  )
