def enchantmentComponents(enchantmentId, level):
	customName = "[{\"translate\": \""
	customName += enchantmentId(enchantmentId)
	customName += "\"}, {\"text\": \" "
	customName += f"{level}"
	customName += "\"}]"

	return {
		"components": {
			"minecraft:stored_enchantments": {
				"levels": {enchantmentId: level}
			},
			"minecraft:custom_name": customName
		}
	}

def enchantmentTransFromId(enchantmentId):
	return f"enchantment.{enchantmentId.replace(':', '_')}"

# reference
# {
#   "type": "farmingforblockheads:market",
#   "category": "farmingforblockheads:flora",
#   "preset": "farming_crossing:kubejsmiles_ticket_4",
#   "result": {
#     "item": "minecraft:enchanted_book",
#     "components": {
#       "minecraft:stored_enchantments": {
#         "levels": {"minecraft:wind_burst": 3}
#       },
#       "minecraft:custom_name": "[{\"translate\": \"enchantment.minecraft.wind_burst\"}, {\"text\": \" 3\"}]"
#     }
#   }
# }
