"modules organize our code into files. just like sections in a market."
"fruits veggies etc."

# def lbs_to_kg(weight):
#    return weight * 0.45
#
# def kg_to_lbs(weight):
#    return weight / 0.45


"#two functions for converting"
"#we can put these 2 into 2 modules and import anytime"

import converter

converter.kg_to_lbs(70)
converter.lbs_to_kg(205)

# we can import a specific FUNC or CLASS from a module
from converter import kg_to_lbs
kg_to_lbs(70)

from converter import lbs_to_kg
lbs_to_kg(100)