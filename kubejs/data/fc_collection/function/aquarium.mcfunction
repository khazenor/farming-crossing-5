scoreboard players add @p aquarium 1
tellraw @p ["", {"translate":"questFunctions.new_fish_caught_aquarium"}, {"score":{"name":"@p","objective":"aquarium"}}, {"translate":"questFunctions.37"}]
