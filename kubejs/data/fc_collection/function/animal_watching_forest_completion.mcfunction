scoreboard players add @p animal_watching_forest_completion 1
tellraw @p ["", {"translate":"questFunctions.forest_completion"}, {"score":{"name":"@p","objective":"animal_watching_forest_completion"}}, {"translate":"questFunctions.1"}]
tellraw @p [""]