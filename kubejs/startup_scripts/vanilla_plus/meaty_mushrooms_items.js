StartupEvents.registry('item', event => {
	// left for legacy support
	simpleFood(event, 'roasted_brown_mushroom', 4, 1)
	simpleFood(event, 'roasted_red_mushroom', 4, 1)

	// actual meaty mushrooms
	simpleFood(event, 'mushroom_patty', 4, 1)
	simpleFood(event, 'cooked_mushroom_patty', 4, 1)
})