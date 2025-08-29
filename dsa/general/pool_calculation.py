from dataclasses import dataclass
from collections import defaultdict

class PoolTable:

	BOSS_POOL_AMOUNT = 20
	BOSS_POOL = 'BOSS_POOL'

	def __init__(self):
		self.GAME_AMOUNT = 0
		self.player_1_wins = 0
		self.player_2_wins = 0

	def initalize(self):
		self.game_amount = int(input('Enter the Game amount e.g. 50: '))
		self.player_1_wins = int(input('Enter player 1 wins e.g. 5: '))
		self.player_2_wins = int(input('Enter player 2 wins e.g. 2: '))

	def pool_calculation(self):
		total_games = self.player_1_wins + self.player_2_wins
		winner_take_home = self.GAME_AMOUNT - self.BOSS_POOL_AMOUNT

		results = defaultdict(int)

		for i in range(total_games):
			winner = 'A' if i < self.player_1_wins else 'B'
			loser = 'B' if i < self.player_1_wins else 'A'

			results[winner] += winner_take_home
			results[loser] -= self.GAME_AMOUNT
			results[self.BOSS_POOL] += self.BOSS_POOL_AMOUNT

		return results
	


	def run(self):
		self.initalize()
		calculations = self.pool_calculation()

		print('\nLETS TALK MONEY')
		print('-' * 20)
		for k, v in calculations.items():
			print(f'{k}: {v}')

		print('-' * 20, '\n')


if __name__ == '__main__':
    poolTable = PoolTable()
    poolTable.run()
