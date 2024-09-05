scoreboard players add @p animal_watching 1
tellraw @p ["", {"translate":"questFunctions.new_animal_observed_animal_watching"}, {"score":{"name":"@p","objective":"animal_watching"}}, {"translate":"questFunctions.29"}]
