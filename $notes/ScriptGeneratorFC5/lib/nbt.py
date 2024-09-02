def enchantment(enchantmentName, level):
	return {
		'StoredEnchantments':[
			{
				'id': enchantmentName,
				'lvl': level
			}
		]
	}

def nametag(name):
	return {
		'RepairCost':0,
		'display': {
			'Name': f'{{"text": "{name}"}}'
		}
	}
