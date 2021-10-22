# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
from unittest import main


rect = shape_calculator.Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

rect.get_picture()

# sq = shape_calculator.Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)

# sq2 = shape_calculator.Square(4)
# sq2.set_height(5)
# print(sq2)
sq3 = shape_calculator.Square(2)
sq3.set_side(3)
print(sq3.get_picture())


# Run unit tests automatically
main(module='test_module', exit=False)