scoreboard players add @p animal_watching_caves_completion 1
tellraw @p ["", {"translate":"questFunctions.caves_completion"}, {"score":{"name":"@p","objective":"animal_watching_caves_completion"}}, {"translate":"questFunctions.3"}]
tellraw @p [""]