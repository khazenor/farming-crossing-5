scoreboard players add @p mineral_museum 1
tellraw @p ["", {"translate":"questFunctions.new_mineral_mined_mineral_museum"}, {"score":{"name":"@p","objective":"mineral_museum"}}, {"translate":"questFunctions.33"}]
