from list import collectionQuests as cqlist
from src import questCollectionReader

fcCategoryKey = 'fc'
floraCategoryKey = 'flora'
farmCategoryKey = 'farm'
miningCategoryKey = 'mining'

nameKey = 'name'
iconKey = 'icon'
entryGroupsKey = 'entryGroups'
itemsKey = 'items'
priceKey = 'price'
priceItemKey = 'priceItem'
productNumKey = 'productNum'
nbtKey = 'nbt'

categories = {
  fcCategoryKey: {
    nameKey: "Farming Crossing Shop",
    iconKey: "lootbags:loot_bag",
    entryGroupsKey: [
      {
        priceKey: 16,
        itemsKey: ["minecraft:villager_spawn_egg"]
      },
      {
        priceKey: 32,
        itemsKey: ["minecraft:wandering_trader_spawn_egg"]
      },
      {
        priceKey: 8,
        itemsKey: ["minecraft:bundle"]
      },
      {
        priceKey: 4,
        itemsKey: ["minecraft:white_bed"]
      },
      {
        itemsKey: ['kubejs:check_food_cravings']
      },
      { # furniture
        priceKey: 8,
        itemsKey: ["lootbags:loot_bag"],
        nbtKey: {
          "Color": 13882323,
          "Loot":"lootbags:furniture/loot_furniture",
          "Name":"Furniture Kit",
          "Type":"COMMON"
        }
      },
      { # Neighborly
        priceKey: 16,
        itemsKey: ["lootbags:loot_bag"],
        nbtKey: {
          "Type": "RARE",
          "Loot": "lootbags:furniture/loot_neighborly",
          "Color": 13882323,
          "Name": "Neighborly Villager Move In Kit"
        }
      },
      { # Storage
        priceKey: 16,
        productNumKey: 2,
        itemsKey: ["kubejs:1k_storage_disk_ticket"]
      },
      {
        priceKey: 72,
        productNumKey: 2,
        itemsKey: ["kubejs:4k_storage_disk_ticket"]
      },
      {
        priceKey: 297,
        productNumKey: 2,
        itemsKey: ["kubejs:16k_storage_disk_ticket"]
      },
      {
        priceKey: 1215,
        productNumKey: 2,
        itemsKey: ["kubejs:64k_storage_disk_ticket"]
      },
      { # storage items
        priceKey: 32,
        itemsKey: [
          "refinedstorage:disk_drive",
          "refinedstorage:crafting_grid",
          "refinedstorage:controller",
          "createaddition:alternator"
        ]
      },
      { # Storage upgrade
        priceKey: 1000,
        itemsKey: ['kubejs:creative_upgrade']
      },
      { # handcrafted
        productNumKey: 2,
        itemsKey: [
          "handcrafted:black_sheet",
          "handcrafted:blue_sheet",
          "handcrafted:brown_sheet",
          "handcrafted:cyan_sheet",
          "handcrafted:gray_sheet",
          "handcrafted:green_sheet",
          "handcrafted:light_blue_sheet",
          "handcrafted:light_gray_sheet",
          "handcrafted:lime_sheet",
          "handcrafted:magenta_sheet",
          "handcrafted:orange_sheet",
          "handcrafted:pink_sheet",
          "handcrafted:purple_sheet",
          "handcrafted:red_sheet",
          "handcrafted:white_sheet",
          "handcrafted:yellow_sheet",
          "handcrafted:black_cushion",
          "handcrafted:blue_cushion",
          "handcrafted:brown_cushion",
          "handcrafted:cyan_cushion",
          "handcrafted:gray_cushion",
          "handcrafted:green_cushion",
          "handcrafted:light_blue_cushion",
          "handcrafted:light_gray_cushion",
          "handcrafted:lime_cushion",
          "handcrafted:magenta_cushion",
          "handcrafted:orange_cushion",
          "handcrafted:pink_cushion",
          "handcrafted:purple_cushion",
          "handcrafted:red_cushion",
          "handcrafted:white_cushion",
          "handcrafted:yellow_cushion" 
        ]
      }
    ]
  },
  floraCategoryKey: {
    nameKey: "Garden Stand",
    iconKey: "minecraft:poppy",
    entryGroupsKey: [
      {
        priceKey: 8,
        itemsKey: [
          "minecraft:chorus_fruit",
          "aquaculture:algae"
        ]
      },
      { # dyes
        priceKey: 4,
        productNumKey: 8,
        itemsKey: [
          "minecraft:black_dye",
          "minecraft:blue_dye",
          "minecraft:brown_dye",
          "minecraft:cyan_dye",
          "minecraft:gray_dye",
          "minecraft:green_dye",
          "minecraft:light_blue_dye",
          "minecraft:light_gray_dye",
          "minecraft:lime_dye",
          "minecraft:magenta_dye",
          "minecraft:orange_dye",
          "minecraft:pink_dye",
          "minecraft:purple_dye",
          "minecraft:red_dye",
          "minecraft:white_dye",
          "minecraft:yellow_dye"
        ]
      },
      { # delight tea leaf
        itemsKey: ["delightful:green_tea_leaf"]
      },
      { # pam seeds
        itemsKey: [
          'pamhc2crops:agaveseeditem',
          'pamhc2crops:alfalfaseeditem',
          'pamhc2crops:aloeseeditem',
          'pamhc2crops:amaranthseeditem',
          'pamhc2crops:arrowrootseeditem',
          'pamhc2crops:artichokeseeditem',
          'pamhc2crops:asparagusseeditem',
          'pamhc2crops:barleyseeditem',
          'pamhc2crops:barrelcactusseeditem',
          'pamhc2crops:beanseeditem',
          'pamhc2crops:bellpepperseeditem',
          'pamhc2crops:blackberryseeditem',
          'pamhc2crops:blueberryseeditem',
          'pamhc2crops:bokchoyseeditem',
          'pamhc2crops:broccoliseeditem',
          'pamhc2crops:brusselsproutseeditem',
          'pamhc2crops:cabbageseeditem',
          'pamhc2crops:cactusfruitseeditem',
          'pamhc2crops:calabashseeditem',
          'pamhc2crops:candleberryseeditem',
          'pamhc2crops:canolaseeditem',
          'pamhc2crops:cantaloupeseeditem',
          'pamhc2crops:cassavaseeditem',
          'pamhc2crops:cattailseeditem',
          'pamhc2crops:cauliflowerseeditem',
          'pamhc2crops:celeryseeditem',
          'pamhc2crops:chiaseeditem',
          'pamhc2crops:chickpeaseeditem',
          'pamhc2crops:chilipepperseeditem',
          'pamhc2crops:cloudberryseeditem',
          'pamhc2crops:coffeebeanseeditem',
          'pamhc2crops:cornseeditem',
          'pamhc2crops:cottonseeditem',
          'pamhc2crops:cranberryseeditem',
          'pamhc2crops:cucumberseeditem',
          'pamhc2crops:eggplantseeditem',
          'pamhc2crops:elderberryseeditem',
          'pamhc2crops:flaxseeditem',
          'pamhc2crops:garlicseeditem',
          'pamhc2crops:gingerseeditem',
          'pamhc2crops:grapeseeditem',
          'pamhc2crops:greengrapeseeditem',
          'pamhc2crops:guaranaseeditem',
          'pamhc2crops:huckleberryseeditem',
          'pamhc2crops:jicamaseeditem',
          'pamhc2crops:juniperberryseeditem',
          'pamhc2crops:juteseeditem',
          'pamhc2crops:kaleseeditem',
          'pamhc2crops:kenafseeditem',
          'pamhc2crops:kiwiseeditem',
          'pamhc2crops:kohlrabiseeditem',
          'pamhc2crops:leekseeditem',
          'pamhc2crops:lentilseeditem',
          'pamhc2crops:lettuceseeditem',
          'pamhc2crops:lotusseeditem',
          'pamhc2crops:milletseeditem',
          'pamhc2crops:mulberryseeditem',
          'pamhc2crops:mustardseedsseeditem',
          'pamhc2crops:nettlesseeditem',
          'pamhc2crops:nopalesseeditem',
          'pamhc2crops:oatsseeditem',
          'pamhc2crops:okraseeditem',
          'pamhc2crops:onionseeditem',
          'pamhc2crops:papyrusseeditem',
          'pamhc2crops:parsnipseeditem',
          'pamhc2crops:peanutseeditem',
          'pamhc2crops:peasseeditem',
          'pamhc2crops:pineappleseeditem',
          'pamhc2crops:quinoaseeditem',
          'pamhc2crops:radishseeditem',
          'pamhc2crops:raspberryseeditem',
          'pamhc2crops:rhubarbseeditem',
          'pamhc2crops:riceseeditem',
          'pamhc2crops:rutabagaseeditem',
          'pamhc2crops:ryeseeditem',
          'pamhc2crops:scallionseeditem',
          'pamhc2crops:sesameseedsseeditem',
          'pamhc2crops:sisalseeditem',
          'pamhc2crops:sorghumseeditem',
          'pamhc2crops:soybeanseeditem',
          'pamhc2crops:spiceleafseeditem',
          'pamhc2crops:spinachseeditem',
          'pamhc2crops:strawberryseeditem',
          'pamhc2crops:sunchokeseeditem',
          'pamhc2crops:sweetpotatoseeditem',
          'pamhc2crops:taroseeditem',
          'pamhc2crops:tealeafseeditem',
          'pamhc2crops:tomatilloseeditem',
          'pamhc2crops:tomatoseeditem',
          'pamhc2crops:truffleseeditem',
          'pamhc2crops:turnipseeditem',
          'pamhc2crops:waterchestnutseeditem',
          'pamhc2crops:whitemushroomseeditem',
          'pamhc2crops:wintersquashseeditem',
          'pamhc2crops:wolfberryseeditem',
          'pamhc2crops:yuccaseeditem',
          'pamhc2crops:zucchiniseeditem'
        ]
      },
      { # pam crops
        priceKey: 4,
        itemsKey: [
          'pamhc2crops:agaveitem',
          'pamhc2crops:alfalfaitem',
          'pamhc2crops:aloeitem',
          'pamhc2crops:amaranthitem',
          'pamhc2crops:aridgarden',
          'pamhc2crops:arrowrootitem',
          'pamhc2crops:artichokeitem',
          'pamhc2crops:asparagusitem',
          'pamhc2crops:bakedarrowrootitem',
          'pamhc2crops:bakedcassavaitem',
          'pamhc2crops:bakedjicamaitem',
          'pamhc2crops:bakedparsnipitem',
          'pamhc2crops:bakedrutabagaitem',
          'pamhc2crops:bakedsunchokeitem',
          'pamhc2crops:bakedsweetpotatoitem',
          'pamhc2crops:bakedtaroitem',
          'pamhc2crops:bakedturnipitem',
          'pamhc2crops:bakedwaterchestnutitem',
          'pamhc2crops:barleyitem',
          'pamhc2crops:barrelcactusitem',
          'pamhc2crops:beanitem',
          'pamhc2crops:bellpepperitem',
          'pamhc2crops:blackberryitem',
          'pamhc2crops:blueberryitem',
          'pamhc2crops:bokchoyitem',
          'pamhc2crops:broccoliitem',
          'pamhc2crops:brusselsproutitem',
          'pamhc2crops:cabbageitem',
          'pamhc2crops:cactusfruititem',
          'pamhc2crops:calabashitem',
          'pamhc2crops:candleberryitem',
          'pamhc2crops:canolaitem',
          'pamhc2crops:cantaloupeitem',
          'pamhc2crops:cassavaitem',
          'pamhc2crops:cattailitem',
          'pamhc2crops:caulifloweritem',
          'pamhc2crops:celeryitem',
          'pamhc2crops:chiaitem',
          'pamhc2crops:chickpeaitem',
          'pamhc2crops:chilipepperitem',
          'pamhc2crops:cloudberryitem',
          'pamhc2crops:coffeebeanitem',
          'pamhc2crops:cornitem',
          'pamhc2crops:cottonitem',
          'pamhc2crops:cranberryitem',
          'pamhc2crops:cucumberitem',
          'pamhc2crops:eggplantitem',
          'pamhc2crops:elderberryitem',
          'pamhc2crops:flaxitem',
          'pamhc2crops:frostgarden',
          'pamhc2crops:garlicitem',
          'pamhc2crops:gingeritem',
          'pamhc2crops:grapeitem',
          'pamhc2crops:greengrapeitem',
          'pamhc2crops:guaranaitem',
          'pamhc2crops:huckleberryitem',
          'pamhc2crops:jicamaitem',
          'pamhc2crops:juniperberryitem',
          'pamhc2crops:juteitem',
          'pamhc2crops:kaleitem',
          'pamhc2crops:kenafitem',
          'pamhc2crops:kiwiitem',
          'pamhc2crops:kohlrabiitem',
          'pamhc2crops:leekitem',
          'pamhc2crops:lentilitem',
          'pamhc2crops:lettuceitem',
          'pamhc2crops:lotusitem',
          'pamhc2crops:milletitem',
          'pamhc2crops:mulberryitem',
          'pamhc2crops:mustardseedsitem',
          'pamhc2crops:nettlesitem',
          'pamhc2crops:nopalesitem',
          'pamhc2crops:oatsitem',
          'pamhc2crops:okraitem',
          'pamhc2crops:onionitem',
          'pamhc2crops:papyrusitem',
          'pamhc2crops:parsnipitem',
          'pamhc2crops:peanutitem',
          'pamhc2crops:peasitem',
          'pamhc2crops:pineappleitem',
          'pamhc2crops:quinoaitem',
          'pamhc2crops:radishitem',
          'pamhc2crops:raspberryitem',
          'pamhc2crops:rhubarbitem',
          'pamhc2crops:riceitem',
          'pamhc2crops:roastedgarlicitem',
          'pamhc2crops:roastedkohlrabiitem',
          'pamhc2crops:roastedleekitem',
          'pamhc2crops:roastedmushroomitem',
          'pamhc2crops:roastedonionitem',
          'pamhc2crops:roastedpeanutitem',
          'pamhc2crops:roastedradishitem',
          'pamhc2crops:roastedrhubarbitem',
          'pamhc2crops:roastedscallionitem',
          'pamhc2crops:rutabagaitem',
          'pamhc2crops:ryeitem',
          'pamhc2crops:scallionitem',
          'pamhc2crops:sesameseedsitem',
          'pamhc2crops:shadedgarden',
          'pamhc2crops:sisalitem',
          'pamhc2crops:soggygarden',
          'pamhc2crops:sorghumitem',
          'pamhc2crops:soybeanitem',
          'pamhc2crops:spiceleafitem',
          'pamhc2crops:spinachitem',
          'pamhc2crops:strawberryitem',
          'pamhc2crops:sunchokeitem',
          'pamhc2crops:sweetpotatoitem',
          'pamhc2crops:taroitem',
          'pamhc2crops:tealeafitem',
          'pamhc2crops:tomatilloitem',
          'pamhc2crops:tomatoitem',
          'pamhc2crops:tropicalgarden',
          'pamhc2crops:truffleitem',
          'pamhc2crops:turnipitem',
          'pamhc2crops:waterchestnutitem',
          'pamhc2crops:whitemushroomitem',
          'pamhc2crops:windygarden',
          'pamhc2crops:wintersquashitem',
          'pamhc2crops:wolfberryitem',
          'pamhc2crops:yuccaitem',
          'pamhc2crops:zucchiniitem'
        ]
      },
      { # pam saplings
        itemsKey: [
          "pamhc2trees:acorn_sapling",
          "pamhc2trees:almond_sapling",
          "pamhc2trees:apple_sapling",
          "pamhc2trees:apricot_sapling",
          "pamhc2trees:avocado_sapling",
          "pamhc2trees:banana_sapling",
          "pamhc2trees:breadfruit_sapling",
          "pamhc2trees:candlenut_sapling",
          "pamhc2trees:cashew_sapling",
          "pamhc2trees:cherry_sapling",
          "pamhc2trees:chestnut_sapling",
          "pamhc2trees:cinnamon_sapling",
          "pamhc2trees:coconut_sapling",
          "pamhc2trees:date_sapling",
          "pamhc2trees:dragonfruit_sapling",
          "pamhc2trees:durian_sapling",
          "pamhc2trees:fig_sapling",
          "pamhc2trees:gooseberry_sapling",
          "pamhc2trees:grapefruit_sapling",
          "pamhc2trees:guava_sapling",
          "pamhc2trees:hazelnut_sapling",
          "pamhc2trees:jackfruit_sapling",
          "pamhc2trees:lemon_sapling",
          "pamhc2trees:lime_sapling",
          "pamhc2trees:lychee_sapling",
          "pamhc2trees:mango_sapling",
          "pamhc2trees:maple_sapling",
          "pamhc2trees:nutmeg_sapling",
          "pamhc2trees:olive_sapling",
          "pamhc2trees:orange_sapling",
          "pamhc2trees:papaya_sapling",
          "pamhc2trees:paperbark_sapling",
          "pamhc2trees:passionfruit_sapling",
          "pamhc2trees:pawpaw_sapling",
          "pamhc2trees:peach_sapling",
          "pamhc2trees:pear_sapling",
          "pamhc2trees:pecan_sapling",
          "pamhc2trees:peppercorn_sapling",
          "pamhc2trees:persimmon_sapling",
          "pamhc2trees:pinenut_sapling",
          "pamhc2trees:pistachio_sapling",
          "pamhc2trees:plum_sapling",
          "pamhc2trees:pomegranate_sapling",
          "pamhc2trees:rambutan_sapling",
          "pamhc2trees:soursop_sapling",
          "pamhc2trees:spiderweb_sapling",
          "pamhc2trees:starfruit_sapling",
          "pamhc2trees:tamarind_sapling",
          "pamhc2trees:vanillabean_sapling",
          "pamhc2trees:walnut_sapling"
        ]
      },
      { # pam fruits
        priceKey: 4,
        itemsKey: [
          "pamhc2trees:acornitem",
          "pamhc2trees:almonditem",
          "pamhc2trees:apricotitem",
          "pamhc2trees:avocadoitem",
          "pamhc2trees:bananaitem",
          "pamhc2trees:breadfruititem",
          "pamhc2trees:candlenutitem",
          "pamhc2trees:cashewitem",
          "pamhc2trees:cherryitem",
          "pamhc2trees:chestnutitem",
          "pamhc2trees:cinnamonitem",
          "pamhc2trees:coconutitem",
          "pamhc2trees:dateitem",
          "pamhc2trees:dragonfruititem",
          "pamhc2trees:durianitem",
          "pamhc2trees:figitem",
          "pamhc2trees:gooseberryitem",
          "pamhc2trees:grapefruititem",
          "pamhc2trees:guavaitem",
          "pamhc2trees:hazelnutitem",
          "pamhc2trees:jackfruititem",
          "pamhc2trees:lemonitem",
          "pamhc2trees:limeitem",
          "pamhc2trees:lycheeitem",
          "pamhc2trees:mangoitem",
          "pamhc2trees:maplesyrupitem",
          "pamhc2trees:nutmegitem",
          "pamhc2trees:oliveitem",
          "pamhc2trees:orangeitem",
          "pamhc2trees:papayaitem",
          "pamhc2trees:passionfruititem",
          "pamhc2trees:pawpawitem",
          "pamhc2trees:peachitem",
          "pamhc2trees:pearitem",
          "pamhc2trees:pecanitem",
          "pamhc2trees:peppercornitem",
          "pamhc2trees:persimmonitem",
          "pamhc2trees:pinenutitem",
          "pamhc2trees:pistachioitem",
          "pamhc2trees:plumitem",
          "pamhc2trees:pomegranateitem",
          "pamhc2trees:rambutanitem",
          "pamhc2trees:roastedacornitem",
          "pamhc2trees:roastedalmonditem",
          "pamhc2trees:roastedcashewitem",
          "pamhc2trees:roastedchestnutitem",
          "pamhc2trees:roastedhazelnutitem",
          "pamhc2trees:roastedpecanitem",
          "pamhc2trees:roastedpinenutitem",
          "pamhc2trees:roastedpistachioitem",
          "pamhc2trees:roastedwalnutitem",
          "pamhc2trees:soursopitem",
          "pamhc2trees:starfruititem",
          "pamhc2trees:tamarinditem",
          "pamhc2trees:vanillabeanitem",
          "pamhc2trees:walnutitem"
        ]
      },
      { # not in collection
        priceKey: 32,
        productNumKey: 4,
        itemsKey: [
          'minecraft:vine',
          'minecraft:weeping_vines',
          'minecraft:twisting_vines',
          'biomesoplenty:willow_vine'
        ]
      },
      { # flora quests
        priceKey: 32,
        productNumKey: 4,
        itemsKey: cqlist.allFlora
      }
    ]
  },
  farmCategoryKey: {
    nameKey: "Animal Range",
    iconKey: "minecraft:leather",
    entryGroupsKey: [
      {
        priceKey: 32,
        itemsKey: [
          "create:blaze_burner",
          "alexsmobs:pupfish_locator",
          "alexsmobs:unsettling_kimono",
          "alexsmobs:squid_grapple",
          "alexsmobs:straddleboard"
        ]
      },
      { # meats
        priceKey: 2,
        productNumKey: 8,
        itemsKey: [
          "minecraft:beef",
          "minecraft:chicken",
          "minecraft:mutton",
          "minecraft:porkchop",
          "minecraft:rabbit",
          "alexsmobs:kangaroo_meat",
          "alexsmobs:moose_ribs",
          "alexsmobs:raw_catfish",
          "alexsmobs:lobster_tail",
          "alexsmobs:maggot",
          "alexsmobs:centipede_leg",
          "beachparty:raw_mussel_meat",
          "meadow:raw_bear_meat",
          "exoticbirds:raw_birdmeat",
          "alexsmobs:raw_catfish",
          "aquaculture:fish_fillet_raw",
          "alexsdelight:raw_bison",
          "alexsdelight:raw_bunfungus",
          "farmersdelight:ham",
          "delightful:animal_fat",
          "minecraft:rabbit_foot"
        ]
      },
      { # minecraft:arrow
        productNumKey: 4,
        itemsKey: ["minecraft:arrow"]
      },
      { # mob 2
        priceKey: 2,
        itemsKey: [
          "minecraft:feather",
          "minecraft:string"
        ]
      },
      { # mob 4
        priceKey: 4,
        itemsKey: [
          "minecraft:rotten_flesh",
          "minecraft:leather",
          "minecraft:rabbit_hide",
          "alexsmobs:kangaroo_hide",
          "minecraft:bone",
          "minecraft:slime_ball",
          "minecraft:bow",
          "minecraft:ink_sac"
        ]
      },
      {
        priceKey: 8,
        itemsKey: [
          "minecraft:spider_eye",
          "minecraft:gunpowder",
          "minecraft:prismarine_shard",
          "minecraft:prismarine_crystals",
          "minecraft:glow_ink_sac"
        ]
      },
      {
        priceKey: 24,
        itemsKey: [
          "minecraft:ender_pearl",
          "minecraft:blaze_rod",
          "minecraft:ghast_tear"
        ]
      },
      { # alexmobs items
        itemsKey: [
          "alexsmobs:fish_bones",
          "alexsmobs:ambergris",
          "alexsmobs:cachalot_whale_tooth",
          "alexsmobs:tarantula_hawk_wing_fragment"
        ]
      },
      {
        priceKey: 16,
        itemsKey: ["alexsmobs:skreecher_soul"]
      },
      {
        priceKey: 4,
        itemsKey: ["alexsmobs:bone_serpent_tooth"]
      },
      { # fish mercy trades
        priceKey: 64,
        itemsKey: cqlist.allFish
      },
      { # quest spawn eggs
        priceKey: 64,
        itemsKey: questCollectionReader.questSpawnEggs()
      },
      { # spawn eggs
        priceKey: 64,
        productNumKey: 1,
        itemsKey: questCollectionReader.nonQuestSpawnEggs([
          "alexsmobs:spawn_egg_alligator_snapping_turtle",
          "alexsmobs:spawn_egg_anaconda",
          "alexsmobs:spawn_egg_anteater",
          "alexsmobs:spawn_egg_bald_eagle",
          "alexsmobs:spawn_egg_banana_slug",
          "alexsmobs:spawn_egg_bison",
          "alexsmobs:spawn_egg_blobfish",
          "alexsmobs:spawn_egg_blue_jay",
          "alexsmobs:spawn_egg_bone_serpent",
          "alexsmobs:spawn_egg_bunfungus",
          "alexsmobs:spawn_egg_cachalot_whale",
          "alexsmobs:spawn_egg_caiman",
          "alexsmobs:spawn_egg_capuchin_monkey",
          "alexsmobs:spawn_egg_catfish",
          "alexsmobs:spawn_egg_centipede",
          "alexsmobs:spawn_egg_cockroach",
          "alexsmobs:spawn_egg_comb_jelly",
          "alexsmobs:spawn_egg_cosmaw",
          "alexsmobs:spawn_egg_cosmic_cod",
          "alexsmobs:spawn_egg_crimson_mosquito",
          "alexsmobs:spawn_egg_crocodile",
          "alexsmobs:spawn_egg_crow",
          "alexsmobs:spawn_egg_devils_hole_pupfish",
          "alexsmobs:spawn_egg_dropbear",
          "alexsmobs:spawn_egg_elephant",
          "alexsmobs:spawn_egg_emu",
          "alexsmobs:spawn_egg_endergrade",
          "alexsmobs:spawn_egg_enderiophage",
          "alexsmobs:spawn_egg_flutter",
          "alexsmobs:spawn_egg_fly",
          "alexsmobs:spawn_egg_flying_fish",
          "alexsmobs:spawn_egg_frilled_shark",
          "alexsmobs:spawn_egg_froststalker",
          "alexsmobs:spawn_egg_gazelle",
          "alexsmobs:spawn_egg_gelada_monkey",
          "alexsmobs:spawn_egg_giant_squid",
          "alexsmobs:spawn_egg_gorilla",
          "alexsmobs:spawn_egg_grizzly_bear",
          "alexsmobs:spawn_egg_guster",
          "alexsmobs:spawn_egg_hammerhead_shark",
          "alexsmobs:spawn_egg_hummingbird",
          "alexsmobs:spawn_egg_jerboa",
          "alexsmobs:spawn_egg_kangaroo",
          "alexsmobs:spawn_egg_komodo_dragon",
          "alexsmobs:spawn_egg_laviathan",
          "alexsmobs:spawn_egg_leafcutter_ant",
          "alexsmobs:spawn_egg_lobster",
          "alexsmobs:spawn_egg_maned_wolf",
          "alexsmobs:spawn_egg_mantis_shrimp",
          "alexsmobs:spawn_egg_mimic_octopus",
          "alexsmobs:spawn_egg_mimicube",
          "alexsmobs:spawn_egg_moose",
          "alexsmobs:spawn_egg_mudskipper",
          "alexsmobs:spawn_egg_mungus",
          "alexsmobs:spawn_egg_murmur",
          "alexsmobs:spawn_egg_orca",
          "alexsmobs:spawn_egg_platypus",
          "alexsmobs:spawn_egg_potoo",
          "alexsmobs:spawn_egg_raccoon",
          "alexsmobs:spawn_egg_rain_frog",
          "alexsmobs:spawn_egg_rattlesnake",
          "alexsmobs:spawn_egg_rhinoceros",
          "alexsmobs:spawn_egg_roadrunner",
          "alexsmobs:spawn_egg_rocky_roller",
          "alexsmobs:spawn_egg_seagull",
          "alexsmobs:spawn_egg_seal",
          "alexsmobs:spawn_egg_shoebill",
          "alexsmobs:spawn_egg_skelewag",
          "alexsmobs:spawn_egg_skreecher",
          "alexsmobs:spawn_egg_skunk",
          "alexsmobs:spawn_egg_snow_leopard",
          "alexsmobs:spawn_egg_soul_vulture",
          "alexsmobs:spawn_egg_spectre",
          "alexsmobs:spawn_egg_straddler",
          "alexsmobs:spawn_egg_stradpole",
          "alexsmobs:spawn_egg_sugar_glider",
          "alexsmobs:spawn_egg_sunbird",
          "alexsmobs:spawn_egg_tarantula_hawk",
          "alexsmobs:spawn_egg_tasmanian_devil",
          "alexsmobs:spawn_egg_terrapin",
          "alexsmobs:spawn_egg_tiger",
          "alexsmobs:spawn_egg_toucan",
          "alexsmobs:spawn_egg_triops",
          "alexsmobs:spawn_egg_tusklin",
          "alexsmobs:spawn_egg_underminer",
          "alexsmobs:spawn_egg_void_worm",
          "alexsmobs:spawn_egg_warped_mosco",
          "alexsmobs:spawn_egg_warped_toad",
          "aquaculture:arrau_turtle_spawn_egg",
          "aquaculture:box_turtle_spawn_egg",
          "aquaculture:starshell_turtle_spawn_egg",
          "artifacts:mimic_spawn_egg",
          "bakery:wandering_baker_spawn_egg",
          "meadow:brown_bear_spawn_egg",
          "meadow:water_buffalo_spawn_egg",
          "meadow:wooly_cow_spawn_egg",
          "minecraft:allay_spawn_egg",
          "minecraft:axolotl_spawn_egg",
          "minecraft:bat_spawn_egg",
          "minecraft:bee_spawn_egg",
          "minecraft:blaze_spawn_egg",
          "minecraft:camel_spawn_egg",
          "minecraft:cat_spawn_egg",
          "minecraft:cave_spider_spawn_egg",
          "minecraft:chicken_spawn_egg",
          "minecraft:cod_spawn_egg",
          "minecraft:cow_spawn_egg",
          "minecraft:creeper_spawn_egg",
          "minecraft:dolphin_spawn_egg",
          "minecraft:donkey_spawn_egg",
          "minecraft:drowned_spawn_egg",
          "minecraft:enderman_spawn_egg",
          "minecraft:endermite_spawn_egg",
          "minecraft:evoker_spawn_egg",
          "minecraft:fox_spawn_egg",
          "minecraft:frog_spawn_egg",
          "minecraft:ghast_spawn_egg",
          "minecraft:glow_squid_spawn_egg",
          "minecraft:goat_spawn_egg",
          "minecraft:guardian_spawn_egg",
          "minecraft:hoglin_spawn_egg",
          "minecraft:horse_spawn_egg",
          "minecraft:husk_spawn_egg",
          "minecraft:iron_golem_spawn_egg",
          "minecraft:llama_spawn_egg",
          "minecraft:magma_cube_spawn_egg",
          "minecraft:mooshroom_spawn_egg",
          "minecraft:mule_spawn_egg",
          "minecraft:ocelot_spawn_egg",
          "minecraft:panda_spawn_egg",
          "minecraft:parrot_spawn_egg",
          "minecraft:phantom_spawn_egg",
          "minecraft:pig_spawn_egg",
          "minecraft:piglin_brute_spawn_egg",
          "minecraft:piglin_spawn_egg",
          "minecraft:pillager_spawn_egg",
          "minecraft:polar_bear_spawn_egg",
          "minecraft:pufferfish_spawn_egg",
          "minecraft:rabbit_spawn_egg",
          "minecraft:ravager_spawn_egg",
          "minecraft:salmon_spawn_egg",
          "minecraft:sheep_spawn_egg",
          "minecraft:shulker_spawn_egg",
          "minecraft:silverfish_spawn_egg",
          "minecraft:skeleton_horse_spawn_egg",
          "minecraft:skeleton_spawn_egg",
          "minecraft:slime_spawn_egg",
          "minecraft:sniffer_spawn_egg",
          "minecraft:snow_golem_spawn_egg",
          "minecraft:spider_spawn_egg",
          "minecraft:squid_spawn_egg",
          "minecraft:stray_spawn_egg",
          "minecraft:strider_spawn_egg",
          "minecraft:tadpole_spawn_egg",
          "minecraft:trader_llama_spawn_egg",
          "minecraft:tropical_fish_spawn_egg",
          "minecraft:turtle_spawn_egg",
          "minecraft:vex_spawn_egg",
          "minecraft:villager_spawn_egg",
          "minecraft:vindicator_spawn_egg",
          "minecraft:wandering_trader_spawn_egg",
          "minecraft:witch_spawn_egg",
          "minecraft:wither_skeleton_spawn_egg",
          "minecraft:wolf_spawn_egg",
          "minecraft:zoglin_spawn_egg",
          "minecraft:zombie_horse_spawn_egg",
          "minecraft:zombie_spawn_egg",
          "minecraft:zombie_villager_spawn_egg",
          "minecraft:zombified_piglin_spawn_egg",
          "supplementaries:red_merchant_spawn_egg",
          "vinery:mule_spawn_egg",
          "vinery:wandering_winemaker_spawn_egg",
          "exoticbirds:bluejay_spawn_egg",
          "exoticbirds:booby_spawn_egg",
          "exoticbirds:budgerigar_spawn_egg",
          "exoticbirds:cardinal_spawn_egg",
          "exoticbirds:cassowary_spawn_egg",
          "exoticbirds:cockatoo_spawn_egg",
          "exoticbirds:crane_spawn_egg",
          "exoticbirds:duck_spawn_egg",
          "exoticbirds:flamingo_spawn_egg",
          "exoticbirds:gouldianfinch_spawn_egg",
          "exoticbirds:gull_spawn_egg",
          "exoticbirds:heron_spawn_egg",
          "exoticbirds:hummingbird_spawn_egg",
          "exoticbirds:kingfisher_spawn_egg",
          "exoticbirds:kiwi_spawn_egg",
          "exoticbirds:kookaburra_spawn_egg",
          "exoticbirds:lyrebird_spawn_egg",
          "exoticbirds:macaw_spawn_egg",
          "exoticbirds:magpie_spawn_egg",
          "exoticbirds:ostrich_spawn_egg",
          "exoticbirds:owl_spawn_egg",
          "exoticbirds:peafowl_spawn_egg",
          "exoticbirds:pelican_spawn_egg",
          "exoticbirds:penguin_spawn_egg",
          "exoticbirds:pigeon_spawn_egg",
          "exoticbirds:roadrunner_spawn_egg",
          "exoticbirds:robin_spawn_egg",
          "exoticbirds:swan_spawn_egg",
          "exoticbirds:toucan_spawn_egg",
          "exoticbirds:woodpecker_spawn_egg",
          'quark:crab_spawn_egg',
          'quark:forgotten_spawn_egg',
          'quark:foxhound_spawn_egg',
          'quark:shiba_spawn_egg',
          'quark:stoneling_spawn_egg',
          'quark:toretoise_spawn_egg',
          'quark:wraith_spawn_egg'
        ])
      },
      { # phoenix eggs
        priceKey: 500,
        itemsKey: [
          "exoticbirds:cloud_phoenix_spawn_egg",
          "exoticbirds:desert_phoenix_spawn_egg",
          "exoticbirds:ender_phoenix_spawn_egg",
          "exoticbirds:fire_phoenix_spawn_egg",
          "exoticbirds:nether_phoenix_spawn_egg",
          "exoticbirds:skeleton_phoenix_spawn_egg",
          "exoticbirds:snowy_phoenix_spawn_egg",
          "exoticbirds:twilight_phoenix_spawn_egg",
          "exoticbirds:water_phoenix_spawn_egg"
        ]
      }
    ]
  },
  miningCategoryKey: {
    nameKey: "Mineral Museum",
    iconKey: "minecraft:glowstone_dust",
    entryGroupsKey: [
      {
        productNumKey: 4,
        itemsKey: [
          "minecraft:emerald",
          "create:experience_nugget"
        ]
      },
      {
        priceKey: 4,
        itemsKey: ["minecraft:quartz"]
      },
      {
        priceKey: 6,
        itemsKey: ["minecraft:glowstone_dust"]
      },
      {
        priceKey: 64,
        itemsKey: ["quark:diamond_heart"]
      },
      { # blocks
        priceKey: 32,
        itemsKey: [
          "minecraft:ice",
          "minecraft:blackstone",
          "minecraft:end_stone",
          'minecraft:sea_lantern',
          'minecraft:shroomlight',
          'minecraft:ochre_froglight',
          'minecraft:pearlescent_froglight',
          'minecraft:verdant_froglight',
          # quark
          "quark:permafrost",
          "quark:permafrost",
          "quark:myalite",
          "quark:dusky_myalite",
          "quark:myalite_crystal",
          "quark:shale",
          "quark:jasper",
          "quark:limestone"
        ]
      },
      { # Collections
        priceKey: 64,
        itemsKey: [
          'quark:white_corundum',
          'quark:white_corundum_cluster',
          'quark:red_corundum',
          'quark:red_corundum_cluster',
          'quark:orange_corundum',
          'quark:orange_corundum_cluster',
          'quark:yellow_corundum',
          'quark:yellow_corundum_cluster',
          'quark:green_corundum',
          'quark:green_corundum_cluster',
          'quark:blue_corundum',
          'quark:blue_corundum_cluster',
          'quark:indigo_corundum',
          'quark:indigo_corundum_cluster',
          'quark:violet_corundum',
          'quark:violet_corundum_cluster',
          'quark:black_corundum',
          'quark:black_corundum_cluster'
        ]
      }
    ]
  }
}

enchantments = {
  "alexsmobs:board_return": {
    "maxLvCost": 32,
    "maxLv": 1
  },
  "alexsmobs:lavawax": {
    "maxLvCost": 32,
    "maxLv": 1
  },
  "alexsmobs:serpentfriend": {
    "maxLvCost": 32,
    "maxLv": 1
  },
  "alexsmobs:straddle_jump": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "create:capacity": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "create:potato_recovery": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:aqua_affinity": {
    "maxLvCost": 32,
    "maxLv": 1
  },
  "minecraft:bane_of_arthropods": {
    "maxLvCost": 32,
    "maxLv": 5
  },
  "minecraft:binding_curse": {
    "maxLvCost": 32,
    "maxLv": 1
  },
  "minecraft:blast_protection": {
    "maxLvCost": 32,
    "maxLv": 4
  },
  "minecraft:channeling": {
    "maxLvCost": 32,
    "maxLv": 1
  },
  "minecraft:depth_strider": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:efficiency": {
    "maxLvCost": 32,
    "maxLv": 5
  },
  "minecraft:feather_falling": {
    "maxLvCost": 32,
    "maxLv": 4
  },
  "minecraft:fire_aspect": {
    "maxLvCost": 32,
    "maxLv": 2
  },
  "minecraft:fire_protection": {
    "maxLvCost": 32,
    "maxLv": 4
  },
  "minecraft:flame": {
    "maxLvCost": 32,
    "maxLv": 1
  },
  "minecraft:fortune": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:frost_walker": {
    "maxLvCost": 32,
    "maxLv": 2
  },
  "minecraft:impaling": {
    "maxLvCost": 32,
    "maxLv": 5
  },
  "minecraft:infinity": {
    "maxLvCost": 32,
    "maxLv": 1
  },
  "minecraft:knockback": {
    "maxLvCost": 32,
    "maxLv": 2
  },
  "minecraft:looting": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:loyalty": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:luck_of_the_sea": {
    "maxLvCost": 32,
    "maxLv": 2
  },
  "minecraft:lure": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:mending": {
    "maxLvCost": 32,
    "maxLv": 1
  },
  "minecraft:multishot": {
    "maxLvCost": 32,
    "maxLv": 1
  },
  "minecraft:piercing": {
    "maxLvCost": 32,
    "maxLv": 4
  },
  "minecraft:power": {
    "maxLvCost": 32,
    "maxLv": 5
  },
  "minecraft:projectile_protection": {
    "maxLvCost": 32,
    "maxLv": 4
  },
  "minecraft:protection": {
    "maxLvCost": 32,
    "maxLv": 4
  },
  "minecraft:punch": {
    "maxLvCost": 32,
    "maxLv": 2
  },
  "minecraft:quick_charge": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:respiration": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:riptide": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:sharpness": {
    "maxLvCost": 32,
    "maxLv": 5
  },
  "minecraft:silk_touch": {
    "maxLvCost": 32,
    "maxLv": 1
  },
  "minecraft:smite": {
    "maxLvCost": 32,
    "maxLv": 5
  },
  "minecraft:soul_speed": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:sweeping": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:swift_sneak": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:thorns": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:unbreaking": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:vanishing_curse": {
    "maxLvCost": 32,
    "maxLv": 1
  },
  "supplementaries:stasis": {
    "maxLvCost": 32,
    "maxLv": 1
  },
  "utilitix:bell_range": {
    "maxLvCost": 32,
    "maxLv": 3
  }
}
