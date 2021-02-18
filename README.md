# flappyBird
Created a work in progress version of flappy bird using the turtle module in python.

bird:
  2 main actions:
    bird would fall each time the game went through its' loop
      as it would fall it would tilt down
    on user input ("space") bird would tilt up and increase its' Y value simulating the bird jumping
      jump stronger than downward velocity
  check if bird hit ground
  bird would maintain the same X value for the entire game
  
pipes:
  2 pipes spawned every 30 game loops
    the bottom pipe would generate at a yandom Y value 
    the top pipe would spawn a certain distance above the bottom pipe
      allowed for a true random distribution of the types of pipes
  pipes would travel at a constant speed
    each game loop their X value decreased by a constant amount
  after pipes reached far left and exited scene they were deleted from the "pipes" list and cleared from the screen
  
scoreboard:
  iterates through all pipes currently generated in the scene
    if pipe X value becomes < bird X value --> score++
  after bird dies - check if score > highscore
    if score > highscore --> write to data.txt file and update highscore
    
 
    
