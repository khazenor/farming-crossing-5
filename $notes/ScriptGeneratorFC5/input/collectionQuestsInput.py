filenameKey = 'filename'
iconKey = 'icon'
nameKey = 'name'
dependencyIdKey = 'dependencyId'
increaseRateKey = 'increaseRate'

collectionNotificationKey = 'collectionNotification'

typeKey = 'type'
itemQuestTypeConst = 'itemQuestType'
observationQuestTypeConst = 'observationQuestType'

questGroupsKey = 'questGroups'
tasksKey = 'tasks'
observeKey = 'observe'
additionalRewardsKey = 'additionalRewards'
questStartAtCenterKey = 'questStartAtCenter'

questlineGroupId = '6A7C23160DA2BBC4'

itemSeedStrs = {
}

questlines = [
  { # Cooking collection
    filenameKey: 'cooking_collection',
    nameKey: 'Cooking Collection',
    iconKey: 'farmersdelight:cooking_pot',
    collectionNotificationKey: 'New dish cooked!',
    increaseRateKey: 0.04,
    typeKey: itemQuestTypeConst,
    questStartAtCenterKey: False,
    questGroupsKey: [
      {
        nameKey: 'Sweets (Farmers Delight) Completion',
        iconKey: 'farmersdelight:apple_pie',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
            'farmersdelight:apple_pie',
            'farmersdelight:sweet_berry_cheesecake',
            'farmersdelight:chocolate_pie',
            'farmersdelight:sweet_berry_cookie',
            'farmersdelight:honey_cookie',
            'farmersdelight:melon_popsicle',
            'farmersdelight:glow_berry_custard'
        ]
      }, {
        nameKey: 'Salads (Farmers Delight) Completion',
        iconKey: 'farmersdelight:fruit_salad',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
            'farmersdelight:fruit_salad',
            'farmersdelight:mixed_salad',
            'farmersdelight:nether_salad'
        ]
      }, {
        nameKey: 'Sandwiches (Farmers Delight) Completion',
        iconKey: 'farmersdelight:egg_sandwich',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
            'farmersdelight:egg_sandwich',
            'farmersdelight:chicken_sandwich',
            'farmersdelight:hamburger',
            'farmersdelight:bacon_sandwich'
        ]
      }, {
        nameKey: 'Soups (Farmers Delight) Completion',
        iconKey: 'farmersdelight:beef_stew',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
            'farmersdelight:beef_stew',
            'farmersdelight:bone_broth',
            'farmersdelight:chicken_soup',
            'farmersdelight:vegetable_soup',
            'farmersdelight:fish_stew',
            'farmersdelight:pumpkin_soup',
            'farmersdelight:baked_cod_stew'
        ]
      }, {
        nameKey: 'Asian Foods (Farmers Delight) Completion',
        iconKey: 'farmersdelight:dumplings',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
            'farmersdelight:dumplings',
            'farmersdelight:fried_rice',
            'farmersdelight:cabbage_rolls'
        ]
      }, {
        nameKey: 'Dinners (Farmers Delight) Completion',
        iconKey: 'farmersdelight:steak_and_potatoes',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
            'farmersdelight:steak_and_potatoes',
            'farmersdelight:mutton_wrap',
            'farmersdelight:bacon_and_eggs',
            'farmersdelight:stuffed_potato',
            'farmersdelight:mushroom_rice',
            'farmersdelight:ratatouille'
        ]
      }, {
        nameKey: 'Noodles (Farmers Delight) Completion',
        iconKey: 'farmersdelight:pasta_with_mutton_chop',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
            'farmersdelight:pasta_with_meatballs',
            'farmersdelight:pasta_with_mutton_chop',
            'farmersdelight:vegetable_noodles',
            'farmersdelight:squid_ink_pasta',
            'farmersdelight:noodle_soup'
        ]
      }, {
        nameKey: 'BBQ (Farmers Delight) Completion',
        iconKey: 'farmersdelight:barbecue_stick',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
            'farmersdelight:barbecue_stick',
            'farmersdelight:grilled_salmon',
            'farmersdelight:roasted_mutton_chops'
        ]
      }, {
        nameKey: 'Large Meals (Farmers Delight) Completion',
        iconKey: 'farmersdelight:roast_chicken_block',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
            'farmersdelight:roast_chicken_block',
            'farmersdelight:stuffed_pumpkin_block',
            'farmersdelight:honey_glazed_ham_block',
            'farmersdelight:shepherds_pie_block',
            'farmersdelight:rice_roll_medley_block'
        ]
      }
    ]
  }
]