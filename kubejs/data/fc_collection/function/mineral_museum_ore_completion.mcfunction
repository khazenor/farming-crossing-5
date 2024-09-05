scoreboard players add @p mineral_museum_ore_completion 1
tellraw @p ["", {"translate":"questFunctions.ore_completion"}, {"score":{"name":"@p","objective":"mineral_museum_ore_completion"}}, {"translate":"questFunctions.8"}]
tellraw @p [""]
