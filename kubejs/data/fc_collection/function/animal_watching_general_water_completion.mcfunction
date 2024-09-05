scoreboard players add @p animal_watching_general_water_completion 1
tellraw @p ["", {"translate":"questFunctions.general_water_completion"}, {"score":{"name":"@p","objective":"animal_watching_general_water_completion"}}, {"translate":"questFunctions.2"}]
tellraw @p [""]
