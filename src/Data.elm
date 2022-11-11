module Data exposing (defaultOccupations)

import Dict

{-| All default occupations that a commoner can have. -}
defaultOccupations : Dict.Dict String Int
defaultOccupations =
    Dict.fromList
        [ ( "Baker"                     ,  25 )
        , ( "Shoemaker"                 ,  37 )
        , ( "Furrier"                   ,  62 )
        , ( "Household helper"          ,  62 )
        , ( "Tailor"                    ,  62 )
        , ( "Barber"                    ,  87 )
        , ( "Unlicensed Doctor"         ,  87 )
        , ( "Jeweler"                   , 100 )
        , ( "Old cloth seller"          , 100 )
        , ( "Pastry baker"              , 125 )
        , ( "Mason"                     , 125 )
        , ( "Carpenter"                 , 137 )
        , ( "Ostler"                    , 150 )
        , ( "Porter"                    , 150 )
        , ( "Weaver"                    , 150 )
        , ( "Chandler"                  , 175 )
        , ( "Mercer"                    , 175 )
        , ( "Cooper"                    , 175 )
        , ( "Cobbler"                   , 180 )
        , ( "Watercarrier"              , 212 )
        , ( "Scabbardmaker"             , 212 )
        , ( "Wine-seller"               , 225 )
        , ( "Hatmaker"                  , 237 )
        , ( "Saddler"                   , 250 )
        , ( "Chicken butcher"           , 250 )
        , ( "Pursemaker"                , 275 )
        , ( "Soapmaker"                 , 275 )
        , ( "Goldsmith"                 , 300 )
        , ( "Butcher"                   , 300 )
        , ( "Farrier"                   , 300 )
        , ( "Fishmonger"                , 300 )
        , ( "Beer seller"               , 350 )
        , ( "Buckle Maker"              , 350 )
        , ( "Plasterer"                 , 350 )
        , ( "Spice Merchant"            , 350 )
        , ( "Hedge-Mage"                , 350 )
        , ( "Painter"                   , 375 )
        , ( "Hunter"                    , 400 )
        , ( "Licensed doctor"           , 425 )
        , ( "Roofer"                    , 450 )
        , ( "Locksmith"                 , 475 )
        , ( "Bather"                    , 475 )
        , ( "Ropemaker"                 , 475 )
        , ( "Inn"                       , 500 )
        , ( "Tanner"                    , 500 )
        , ( "Copyist"                   , 500 )
        , ( "Sculptor"                  , 500 )
        , ( "Rugmaker"                  , 500 )
        , ( "Dyer"                      , 500 )
        , ( "Harness-Maker"             , 500 )
        , ( "Bleacher"                  , 525 )
        , ( "Hay Merchant"              , 575 )
        , ( "Cutler"                    , 575 )
        , ( "Glovemaker"                , 600 )
        , ( "Woodcarver"                , 600 )
        , ( "Woodseller"                , 600 )
        , ( "Herald"                    , 600 )
        , ( "Lorimer"                   , 600 )
        , ( "Penmaker"                  , 650 )
        , ( "Horse Trainer"             , 700 )
        , ( "Bookbinder"                , 750 )
        , ( "Stationer (Ink/Pen Maker)" , 700 )
        , ( "Spurrer"                   , 800 )
        , ( "Dung Carter"               , 800 )
        , ( "Costermonger"              , 800 )
        , ( "Fortune Teller"            , 900 )
        , ( "Chirurgeon"                , 900 )
        , ( "Silversmith"               , 920 )
        , ( "Illuminator"               , 975 )
        , ( "Coppersmith"               , 1100 )
        , ( "Master of Hounds"          , 1200 )
        , ( "Leech Collector"           , 1300 )
        , ( "Tinsmith"                  , 1400 )
        , ( "Castellan"                 , 1500 )
        , ( "Bookseller"                , 1575 )
        , ( "Composer"                  , 1600 )
        , ( "Limeburner"                , 1600 )
        , ( "Ale-conner"                , 1700 )
        , ( "Amanuensis"                , 1800 )
        , ( "Gong Farmer"               , 1800 )
        , ( "Coiner"                    , 1900 )
        , ( "Philosopher"               , 2000 )
        , ( "Noble"                     , 3000 )
        ]

{-| All default items that a commoner can have in their inventory. -}
defaultInventory : List String
defaultInventory =
    [ "Bag of 20 caltrops"
    , "Ball of twine"
    , "Bottle of ink"
    , "Bracelet or anklet worth 25gp"
    , "Bracelet or anklet worth 250gp"
    , "Brass shears"
    , "Candle"
    , "Comb"
    , "Brush"
    , "Component pouch"
    , "Deck of playing cards"
    , "1d4 dice"
    , "Flute"
    , "Gemstone worth 10gp"
    , "Gemstone worth 50gp"
    , "Gemstone worth 100gp"
    , "Gemstone worth 500gp"
    , "Holy symbol"
    , "Key"
    , "Laundry ticket"
    , "Letter in a sealed envelope"
    , "Necklace worth 25gp"
    , "Necklace worth 250gp"
    , "Notebook of names and addresses"
    , "Pocket mirror"
    , "Potion of healing in a vial"
    , "Pouch containing 6cp"
    , "Pouch containing 11cp and 1sp"
    , "Pouch containing 15cp, 3sp, and 1gp"
    , "Pouch containing 7cp, 5sp, and 2gp"
    , "Pouch containg 2cp, 4sp and 5gp"
    , "Pouch containing 3sp and 10gp"
    , "Pouch of herbs"
    , "Pouch of 20 sling bullets"
    , "Ring or earring worth 25gp"
    , "Ring or earring worth 250gp"
    , "Saltshaker"
    , "Pepper mill"
    , "Signet ring"
    , "Silk handkerchief"
    , "Smoking pipe"
    , "Spectacles"
    , "Spool of thread"
    , "Spyglass"
    , "String of 1d4 harbor moons (platinum-and-electrum coins worth 50gp each in major human cities)"
    , "String of 2d6 taols (brass coins worth 2gp each in major human cities)"
    , "The Code Legal written on a folded scroll"
    , "Tinderbox"
    , "Tiny box of tobacco"
    , "Vial of perfume"
    , "Vial of cologne"
    , "Vial of basic poison"
    ]


