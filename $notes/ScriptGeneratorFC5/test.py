import json

ids = [
	"ancient_blaze",
	"baby_ender_dragon",
	"crab",
	"elephant",
	"flamingo",
	"giraffe",
	"koala",
	"lion",
	"mantaray",
	"monkey",
	"nether_knight",
	"ostrich",
	"owl",
	"peacock",
	"penguin",
	"raccoon",
	"seahorse",
	"shark",
	"shroomie",
	"snail"
]

iconKey = 'icon'
nameKey = 'name'
observeKey = 'observe'
def jsonOb(id):
	return {
		iconKey: f"livingthings:{id}_spawn_egg",
		nameKey: f"Spot a {id.replace('_', ' ')}",
		observeKey: f"livingthings:{id}"
	}

if __name__ == "__main__":
	obs = []
	for id in ids:
		obs.append(jsonOb(id))
	print(json.dumps(obs))

	