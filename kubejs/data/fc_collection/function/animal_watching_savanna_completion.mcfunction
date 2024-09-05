scoreboard players add @p animal_watching_savanna_completion 1
tellraw @p ["", {"translate":"questFunctions.savanna_completion"}, {"score":{"name":"@p","objective":"animal_watching_savanna_completion"}}, {"translate":"questFunctions.2"}]
tellraw @p [""]
