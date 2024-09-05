scoreboard players add @p animal_watching_grass_completion 1
tellraw @p ["", {"translate":"questFunctions.grass_completion"}, {"score":{"name":"@p","objective":"animal_watching_grass_completion"}}, {"translate":"questFunctions.5"}]
tellraw @p [""]
