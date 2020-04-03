This README contains explanations for all the files, explaining what they contain, and what it does.

# commoner-occupations.json

The listed occupations are occupations that commoners can pick up. The occupations are all decorative, as they have no real meaning in the town.

The value on the side is their Support Value; this number shows how many families one worker can support with their job. For example, one baker can provide enough bread for 25 families, while one bookseller would be able to provide a town of 1575 with a sufficient amount of books.

# inventory.json

The listed items are all items that an NPC could have in their inventory.

# menu.json

Every food item has two values. All values are required.

The `chanceOfBeingAvailable` is a number between 0 and 1, where 0 represents 0% and 1 means 100%. Every tavern has this chance to have the item.

The `prices` contain values for each type tavern. The prices range from `Squalid` to `Aristocratic`. The higher the class, the higher the price - but also the better the food is prepared. Currently, quality of food is not relevant in the project. However, this is planned to become a feature in the future.

# occupations.json

All relevant classes/jobs are displayed here. They have a few features:

* Value `n` stands for the absolute maximum that a neighbourhood may contain of the class. How often this limit occurs, strongly depends on the `e` value;
* Value `e` stands for the expected (average) amount that the class will occur in the town. The amount is distributed according to the binomial distribution;
* Value `family` stands for whether the class can have a family. The family will all be commoners, due to performance reasons;
* Value `shop` stands for whether the class owns a shop. If the value is `null`, they do not own a shop. If the value is a text string, that's the name of the shop.

_(A neighbourhood is the smallest town unit available. A tiny town often exists of either 1 or 2 neighbourhoods.)_

# races.json

All existing classes exist here. New classes cannot be added as of yet, but existing classes can be removed if wished. Each race has a few features:

* Value `density` is a weight to the class, representing how often they appear in the town. In other words, for every 800,000 humans, you'll find about 10 Water Genasi;
* Value `age` contains 3 more values:
    - Value `maturesAt` determines the maximum age of minors. Children of families are always below this age, and humanoids below this age cannot get children. _(I don't care whether it'd be realistic or not. There's no teenage pregnancies or child abuse in these towns, sorry.)_
    - Value `livesUntil` determines how old the humanoids get. At this age, they'll just die, I guess.
    - Value `becomesParentUntil` determines the maximum age at which the humanoids can have children. Make sure this is at least twice the `maturesAt` value, else it'll raise errors. This value is meant to prevent an 80-year-old human couple from having three biological newborns.

# reviews.json

All store descriptions are located in this file. Whenever a class owns a shop, _(barkeep/tavern excluded)_ their store will have a random description taken from the list.


