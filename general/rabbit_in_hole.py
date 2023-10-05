'''
Rabbit in the Hole
1. https://observablehq.com/@julesblm/rabbit-in-the-hole
2. https://www.youtube.com/watch?v=XEt09iK8IXs

In Ben Awad's 'coding interview' with React Core team member Dan Abramov
he posed Dan the following tricky coding interview question:

There are 100 holes 🕳️ in a line, and there's a rabbit 🐰 hiding in one of the holes

You can only look in one hole at a time, and every time you look in a hole,
the rabbit jumps to an adjacent hole. Find the rabbit

A good solution finds the right algorithm with the best O,
bonus points for providing the exact number of worst case searches for 100 holes
'''

import random

class RabbitHole:

	NO_OF_HOLES: int = 100

	def __init__(self) -> None:
		self.current_move: int = 0
		self.rabbit_position: int = self.set_initial_rabbit_position()

	def set_initial_rabbit_position(self) -> int:
		position: int = random.randint(0, 99)
		return position

	def get_next_rabbit_next_move(self) -> int:
		if self.rabbit_position == 0:
			return self.rabbit_position + 1

		if self.rabbit_position >= self.NO_OF_HOLES:
			return self.rabbit_position - 1

		rabbit_next_random_move: int = random.choice([1, -1])
		return self.rabbit_position + rabbit_next_random_move

	def set_initial_state(self) -> None:
		rabbit_at_even_postion: bool = not self.rabbit_position % 2
		self.current_move = self.current_move if rabbit_at_even_postion else 1

	def chase_rabbit(self) -> None:
		'''There's a guarantee that the rabbit will be found'''

		while True:
			found: bool = self.current_move == self.rabbit_position

			if found:
				print(f'The chase is over at {self.current_move}')
				return

			self.current_move += 1
			self.rabbit_position = self.get_next_rabbit_next_move()


	def main(self) -> None:
		self.set_initial_state()
		self.chase_rabbit()

rabbitHole = RabbitHole()
rabbitHole.main()
