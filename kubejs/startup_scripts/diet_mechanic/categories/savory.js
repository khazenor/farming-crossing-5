const savoryFoods = [
  "aquaculture:algae",
  "aquaculture:arapaima",
  "aquaculture:atlantic_cod",
  "aquaculture:atlantic_halibut",
  "aquaculture:atlantic_herring",
  "aquaculture:bayad",
  "aquaculture:blackfish",
  "aquaculture:bluegill",
  "aquaculture:boulti",
  "aquaculture:brown_shrooma",
  "aquaculture:brown_trout",
  "aquaculture:capitaine",
  "aquaculture:carp",
  "aquaculture:catfish",
  "aquaculture:fish_fillet_cooked",
  "aquaculture:fish_fillet_raw",
  "aquaculture:gar",
  "aquaculture:muskellunge",
  "aquaculture:pacific_halibut",
  "aquaculture:perch",
  "aquaculture:pink_salmon",
  "aquaculture:piranha",
  "aquaculture:pollock",
  "aquaculture:rainbow_trout",
  "aquaculture:red_grouper",
  "aquaculture:red_shrooma",
  "aquaculture:smallmouth_bass",
  "aquaculture:sushi",
  "aquaculture:synodontis",
  "aquaculture:tambaqui",
  "aquaculture:tuna",
  "aquaculture:turtle_soup",
  "artifacts:eternal_steak",
  "artifacts:everlasting_beef",
  "artifacts:onion_ring",
  "dumplings_delight:beef_tomato_boiled_dumpling",
  "dumplings_delight:calamari_boiled_dumpling",
  "dumplings_delight:calamari",
  "dumplings_delight:chicken_mushroom_boiled_dumpling",
  "dumplings_delight:chinese_cabbage_leaf",
  "dumplings_delight:chinese_cabbage",
  "dumplings_delight:cod_boiled_dumpling",
  "dumplings_delight:dandelion_leaf_boiled_dumpling",
  "dumplings_delight:eggplant_egg_boiled_dumpling",
  "dumplings_delight:eggplant",
  "dumplings_delight:fennel",
  "dumplings_delight:fungus_boiled_dumpling",
  "dumplings_delight:garlic_chive_egg_boiled_dumpling",
  "dumplings_delight:garlic_chive",
  "dumplings_delight:garlic_clove",
  "dumplings_delight:garlic",
  "dumplings_delight:greenonion",
  "dumplings_delight:mushroom_boiled_dumpling",
  "dumplings_delight:mutton_boiled_dumpling",
  "dumplings_delight:pork_cabbage_boiled_dumpling",
  "dumplings_delight:pork_cabbage_wonton",
  "dumplings_delight:pork_carrot_wonton",
  "dumplings_delight:pork_celery_boiled_dumpling",
  "dumplings_delight:pork_fennel_boiled_dumpling",
  "dumplings_delight:pork_kelp_boiled_dumpling",
  "dumplings_delight:pork_mushroom_wonton",
  "dumplings_delight:pork_potato_boiled_dumpling",
  "dumplings_delight:pufferfish_boiled_dumpling",
  "dumplings_delight:rabbit_meat_boiled_dumpling",
  "dumplings_delight:salmon_boiled_dumpling",
  "dumplings_delight:tomato_egg_boiled_dumpling",
  "farmersdelight:apple_cider",
  "farmersdelight:apple_pie_slice",
  "farmersdelight:bacon_and_eggs",
  "farmersdelight:bacon_sandwich",
  "farmersdelight:bacon",
  "farmersdelight:baked_cod_stew",
  "farmersdelight:barbecue_stick",
  "farmersdelight:beef_patty",
  "farmersdelight:beef_stew",
  "farmersdelight:bone_broth",
  "farmersdelight:cabbage_leaf",
  "farmersdelight:cabbage_rolls",
  "farmersdelight:cabbage",
  "farmersdelight:cake_slice",
  "farmersdelight:chicken_cuts",
  "farmersdelight:chicken_sandwich",
  "farmersdelight:chicken_soup",
  "farmersdelight:chocolate_pie_slice",
  "farmersdelight:cod_roll",
  "farmersdelight:cod_slice",
  "farmersdelight:cooked_bacon",
  "farmersdelight:cooked_chicken_cuts",
  "farmersdelight:cooked_cod_slice",
  "farmersdelight:cooked_mutton_chops",
  "farmersdelight:cooked_rice",
  "farmersdelight:cooked_salmon_slice",
  "farmersdelight:dog_food",
  "farmersdelight:dumplings",
  "farmersdelight:egg_sandwich",
  "farmersdelight:fish_stew",
  "farmersdelight:fried_egg",
  "farmersdelight:fried_rice",
  "farmersdelight:fruit_salad",
  "farmersdelight:glow_berry_custard",
  "farmersdelight:grilled_salmon",
  "farmersdelight:ham",
  "farmersdelight:hamburger",
  "farmersdelight:honey_cookie",
  "farmersdelight:honey_glazed_ham",
  "farmersdelight:kelp_roll_slice",
  "farmersdelight:kelp_roll",
  "farmersdelight:melon_popsicle",
  "farmersdelight:minced_beef",
  "farmersdelight:mixed_salad",
  "farmersdelight:mushroom_rice",
  "farmersdelight:mutton_chops",
  "farmersdelight:mutton_wrap",
  "farmersdelight:nether_salad",
  "farmersdelight:noodle_soup",
  "farmersdelight:onion",
  "farmersdelight:pasta_with_meatballs",
  "farmersdelight:pasta_with_mutton_chop",
  "farmersdelight:pie_crust",
  "farmersdelight:pumpkin_slice",
  "farmersdelight:pumpkin_soup",
  "farmersdelight:ratatouille",
  "farmersdelight:raw_pasta",
  "farmersdelight:roast_chicken",
  "farmersdelight:roasted_mutton_chops",
  "farmersdelight:salmon_roll",
  "farmersdelight:salmon_slice",
  "farmersdelight:shepherds_pie",
  "farmersdelight:smoked_ham",
  "farmersdelight:squid_ink_pasta",
  "farmersdelight:steak_and_potatoes",
  "farmersdelight:stuffed_potato",
  "farmersdelight:stuffed_pumpkin",
  "farmersdelight:sweet_berry_cheesecake_slice",
  "farmersdelight:sweet_berry_cookie",
  "farmersdelight:tomato_sauce",
  "farmersdelight:tomato",
  "farmersdelight:vegetable_noodles",
  "farmersdelight:vegetable_soup",
  "farmersdelight:wheat_dough",
  "fruitsdelight:apple_jam",
  "fruitsdelight:apple_jello",
  "fruitsdelight:baked_durian",
  "fruitsdelight:baked_pear",
  "fruitsdelight:bayberry_cookie",
  "fruitsdelight:bayberry_jam",
  "fruitsdelight:bayberry_jello",
  "fruitsdelight:bayberry_soup",
  "fruitsdelight:bayberry",
  "fruitsdelight:bellini_cocktail",
  "fruitsdelight:blueberry_custard",
  "fruitsdelight:blueberry_jam",
  "fruitsdelight:blueberry_jello",
  "fruitsdelight:blueberry_muffin",
  "fruitsdelight:blueberry",
  "fruitsdelight:bowl_of_pineapple_fried_rice",
  "fruitsdelight:chorus_jam",
  "fruitsdelight:chorus_jello",
  "fruitsdelight:cranberry_cookie",
  "fruitsdelight:cranberry_jam",
  "fruitsdelight:cranberry_jello",
  "fruitsdelight:cranberry_muffin",
  "fruitsdelight:cranberry",
  "fruitsdelight:dried_persimmon",
  "fruitsdelight:durian_flesh",
  "fruitsdelight:durian_jam",
  "fruitsdelight:durian_jello",
  "fruitsdelight:durian_pie",
  "fruitsdelight:fig_chicken_stew",
  "fruitsdelight:fig_jam",
  "fruitsdelight:fig_jello",
  "fruitsdelight:fig_pudding_slice",
  "fruitsdelight:fig_tart",
  "fruitsdelight:fig",
  "fruitsdelight:glowberry_jam",
  "fruitsdelight:glowberry_jello",
  "fruitsdelight:hamimelon_jam",
  "fruitsdelight:hamimelon_jello",
  "fruitsdelight:hamimelon_juice",
  "fruitsdelight:hamimelon_popsicle",
  "fruitsdelight:hamimelon_shaved_ice",
  "fruitsdelight:hamimelon_slice",
  "fruitsdelight:hawberry_jam",
  "fruitsdelight:hawberry_jello",
  "fruitsdelight:hawberry_roll",
  "fruitsdelight:hawberry_sheet",
  "fruitsdelight:hawberry_stick",
  "fruitsdelight:hawberry_tea",
  "fruitsdelight:hawberry",
  "fruitsdelight:jam_bread",
  "fruitsdelight:kiwi_jam",
  "fruitsdelight:kiwi_jello",
  "fruitsdelight:kiwi_juice",
  "fruitsdelight:kiwi_popsicle",
  "fruitsdelight:kiwi",
  "fruitsdelight:lemon_cookie",
  "fruitsdelight:lemon_jam",
  "fruitsdelight:lemon_jello",
  "fruitsdelight:lemon_juice",
  "fruitsdelight:lemon_slice",
  "fruitsdelight:lemon_tart",
  "fruitsdelight:lemon",
  "fruitsdelight:lychee_cherry_tea",
  "fruitsdelight:lychee_chicken",
  "fruitsdelight:lychee_jam",
  "fruitsdelight:lychee_jello",
  "fruitsdelight:lychee",
  "fruitsdelight:mango_jam",
  "fruitsdelight:mango_jello",
  "fruitsdelight:mango_milkshake",
  "fruitsdelight:mango_salad",
  "fruitsdelight:mango_tea",
  "fruitsdelight:mango",
  "fruitsdelight:mangosteen_cake",
  "fruitsdelight:mangosteen_jam",
  "fruitsdelight:mangosteen_jello",
  "fruitsdelight:mangosteen_tea",
  "fruitsdelight:mangosteen",
  "fruitsdelight:melon_jam",
  "fruitsdelight:melon_jello",
  "fruitsdelight:orange_chicken",
  "fruitsdelight:orange_jam",
  "fruitsdelight:orange_jello",
  "fruitsdelight:orange_juice",
  "fruitsdelight:orange_marinated_pork",
  "fruitsdelight:orange_slice",
  "fruitsdelight:orange",
  "fruitsdelight:peach_jam",
  "fruitsdelight:peach_jello",
  "fruitsdelight:peach_tea",
  "fruitsdelight:peach",
  "fruitsdelight:pear_jam",
  "fruitsdelight:pear_jello",
  "fruitsdelight:pear_juice",
  "fruitsdelight:pear_with_rock_sugar",
  "fruitsdelight:pear",
  "fruitsdelight:persimmon_cookie",
  "fruitsdelight:persimmon_jam",
  "fruitsdelight:persimmon_jello",
  "fruitsdelight:persimmon",
  "fruitsdelight:pineapple_jam",
  "fruitsdelight:pineapple_jello",
  "fruitsdelight:pineapple_marinated_pork",
  "fruitsdelight:pineapple_pie",
  "fruitsdelight:pineapple_slice",
  "fruitsdelight:sweetberry_jam",
  "fruitsdelight:sweetberry_jello",
  "minecraft:apple",
  "minecraft:baked_potato",
  "minecraft:beef",
  "minecraft:beetroot_soup",
  "minecraft:beetroot",
  "minecraft:bread",
  "minecraft:carrot",
  "minecraft:chicken",
  "minecraft:chorus_fruit",
  "minecraft:cod",
  "minecraft:cooked_beef",
  "minecraft:cooked_chicken",
  "minecraft:cooked_cod",
  "minecraft:cooked_mutton",
  "minecraft:cooked_porkchop",
  "minecraft:cooked_rabbit",
  "minecraft:cooked_salmon",
  "minecraft:cookie",
  "minecraft:dried_kelp",
  "minecraft:enchanted_golden_apple",
  "minecraft:glow_berries",
  "minecraft:golden_apple",
  "minecraft:golden_carrot",
  "minecraft:honey_bottle",
  "minecraft:melon_slice",
  "minecraft:mushroom_stew",
  "minecraft:mutton",
  "minecraft:ominous_bottle",
  "minecraft:poisonous_potato",
  "minecraft:porkchop",
  "minecraft:potato",
  "minecraft:pufferfish",
  "minecraft:pumpkin_pie",
  "minecraft:rabbit_stew",
  "minecraft:rabbit",
  "minecraft:rotten_flesh",
  "minecraft:salmon",
  "minecraft:spider_eye",
  "minecraft:suspicious_stew",
  "minecraft:sweet_berries",
  "minecraft:tropical_fish",
  "refurbished_furniture:bread_slice",
  "refurbished_furniture:cheese_sandwich",
  "refurbished_furniture:cheese_toastie",
  "refurbished_furniture:cheese",
  "refurbished_furniture:glow_berry_jam_toast",
  "refurbished_furniture:meatlovers_pizza_slice",
  "refurbished_furniture:sweet_berry_jam_toast",
  "refurbished_furniture:toast",
  "refurbished_furniture:vegetable_pizza_slice",
  "regions_unexplored:duskmelon_slice",
  "regions_unexplored:hanging_earlight_fruit",
  "regions_unexplored:meadow_sage",
  "regions_unexplored:salmonberry",
  "solonion:golden_lunchbox",
  "solonion:lunchbag",
  "solonion:lunchbox"
]