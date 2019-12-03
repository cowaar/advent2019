import scala.collection.mutable.ListBuffer


class MovementFunctions{

  var listOfVisitedCoords = new ListBuffer[(Int, Int)]



  def addVisitedCoords(currCoords:Coords,moveInstructions:String,listOfVisitedCoords: ListBuffer[Coords]): (ListBuffer[Coords],Coords) ={

    println(currCoords,moveInstructions,listOfVisitedCoords)

    var (newVisitedPositions,newCoords) = moveInstructions(0) match {
      case 'L'  => MoveLeft(currCoords, moveInstructions.substring(1).toInt)
      case 'R'  => MoveRight(currCoords, moveInstructions.substring(1).toInt)
      case 'U'  => MoveUp(currCoords, moveInstructions.substring(1).toInt)
      case 'D'  => MoveDown(currCoords, moveInstructions.substring(1).toInt)
    }

    val newlistOfVisitedCoords = listOfVisitedCoords ++ newVisitedPositions

    (newlistOfVisitedCoords,newCoords)


  }


  def MoveLeft(currCoords: Coords, steps: Int): (ListBuffer[Coords],Coords) = {
    var coordsList = new ListBuffer[Coords]
    var currentCoords = currCoords

    for (i <- 0 to steps-1) {
      val x = currentCoords.x
      val y = currentCoords.y
      var newCoords = Coords(x - 1, y)
      coordsList.append(newCoords)
      currentCoords = newCoords
      println(currentCoords)
    }
    (coordsList,currentCoords)
  }


  def MoveRight(currCoords: Coords, steps: Int): (ListBuffer[Coords],Coords) = {
    var coordsList = new ListBuffer[Coords]
    var currentCoords = currCoords

    for (i <- 0 to steps-1) {
      val x = currentCoords.x
      val y = currentCoords.y
      var newCoords = Coords(x + 1, y)
      coordsList.append(newCoords)
      currentCoords = newCoords
      println(currentCoords)
    }
    (coordsList,currentCoords)
  }

  def MoveUp(currCoords: Coords, steps: Int): (ListBuffer[Coords],Coords) = {
    var coordsList = new ListBuffer[Coords]
    var currentCoords = currCoords

    for (i <- 0 to steps-1) {
      val x = currentCoords.x
      val y = currentCoords.y
      var newCoords = Coords(x , y+1)
      coordsList.append(newCoords)
      currentCoords = newCoords
      println(currentCoords)
    }
    (coordsList,currentCoords)
  }


  def MoveDown(currCoords: Coords, steps: Int): (ListBuffer[Coords],Coords) = {
    var coordsList = new ListBuffer[Coords]
    var currentCoords = currCoords

    for (i <- 0 to steps-1) {
      val x = currentCoords.x
      val y = currentCoords.y
      var newCoords = Coords(x , y -1 )
      coordsList.append(newCoords)
      currentCoords = newCoords
      println(currentCoords)
    }
    (coordsList,currentCoords)
  }


}