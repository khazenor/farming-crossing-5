ServerEvents.recipes(event => {

    event.remove({ id: "minecraft:campfire" })
    event.shapeless(
        "minecraft:campfire", [
        "#minecraft:logs",
        "#minecraft:logs",
        "minecraft:stick",
        "minecraft:stick"])
    event.shapeless(
        "minecraft:campfire", [
        "minecraft:charcoal",
        "minecraft:charcoal"])

    event.remove({ id: "minecraft:melon" })
    event.shapeless("minecraft:melon", [
        "minecraft:melon_slice", "minecraft:melon_slice",
        "minecraft:melon_slice","minecraft:melon_slice"
    ])
    event.shapeless("4x minecraft:melon_slice", ["minecraft:melon"])
    event.shapeless('4x minecraft:clay_ball', ['minecraft:clay'])

    event.shapeless("minecraft:feather",["#c:eggs","#c:eggs","#c:eggs","#c:eggs"])

    // concrete conversion
    event.shapeless('minecraft:black_concrete', ['minecraft:black_concrete_powder'])
    event.shapeless('minecraft:blue_concrete', ['minecraft:blue_concrete_powder'])
    event.shapeless('minecraft:brown_concrete', ['minecraft:brown_concrete_powder'])
    event.shapeless('minecraft:cyan_concrete', ['minecraft:cyan_concrete_powder'])
    event.shapeless('minecraft:gray_concrete', ['minecraft:gray_concrete_powder'])
    event.shapeless('minecraft:green_concrete', ['minecraft:green_concrete_powder'])
    event.shapeless('minecraft:light_blue_concrete', ['minecraft:light_blue_concrete_powder'])
    event.shapeless('minecraft:light_gray_concrete', ['minecraft:light_gray_concrete_powder'])
    event.shapeless('minecraft:lime_concrete', ['minecraft:lime_concrete_powder'])
    event.shapeless('minecraft:magenta_concrete', ['minecraft:magenta_concrete_powder'])
    event.shapeless('minecraft:orange_concrete', ['minecraft:orange_concrete_powder'])
    event.shapeless('minecraft:pink_concrete', ['minecraft:pink_concrete_powder'])
    event.shapeless('minecraft:purple_concrete', ['minecraft:purple_concrete_powder'])
    event.shapeless('minecraft:red_concrete', ['minecraft:red_concrete_powder'])
    event.shapeless('minecraft:white_concrete', ['minecraft:white_concrete_powder'])
    event.shapeless('minecraft:yellow_concrete', ['minecraft:yellow_concrete_powder'])

    event.shapeless('4x minecraft:nether_wart', ['minecraft:nether_wart_block'])
    
    event.shapeless('minecraft:cobblestone', ['minecraft:cobbled_deepslate'])

    event.shaped('4x minecraft:chest', [
        'AAA',
        'A A',
        'AAA'
    ], {
        A: '#minecraft:logs'
    })
    event.shaped('16x minecraft:stick', [
        'A',
        'A'
    ], {
        A: '#minecraft:logs'
    })

    event.shaped('minecraft:bell',[
        'LLL',
        'FGF',
        'F F'
    ], {
        L: '#minecraft:logs',
        F: '#minecraft:fences',
        G: 'minecraft:gold_block'
    })
})