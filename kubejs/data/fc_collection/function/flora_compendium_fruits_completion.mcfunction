scoreboard players add @p flora_compendium_fruits_completion 1
tellraw @p ["", {"translate":"questFunctions.fruits_completion"}, {"score":{"name":"@p","objective":"flora_compendium_fruits_completion"}}, {"translate":"questFunctions.20"}]
tellraw @p [""]