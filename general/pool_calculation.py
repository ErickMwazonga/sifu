from collections import defaultdict


def pool_calculation(player1, player2, GAME_AMOUNT):
    total_games = player1 + player2
    BOSS_POOL_AMOUNT = 20
    WINNER_TAKE_HOME = GAME_AMOUNT - BOSS_POOL_AMOUNT
    BOSS_POOL = 'BOSS_POOL'

    results = defaultdict(int)

    for i in range(total_games):
        winner = 'A' if i < player1 else 'B'
        loser = 'B' if i < player1 else 'A'

        results[winner] += WINNER_TAKE_HOME
        results[loser] -= GAME_AMOUNT
        results[BOSS_POOL] += BOSS_POOL_AMOUNT

    return results


def run():
    GAME_AMOUNT = int(input('Enter the Game amount e.g. 50: '))
    player_1_wins = int(input('Enter player 1 wins e.g. 5: '))
    player_2_wins = int(input('Enter player 2 wins e.g. 2: '))

    calculations = pool_calculation(player_1_wins, player_2_wins, GAME_AMOUNT)

    print('\nLETS TALK MONEY')
    print('-' * 20)
    for k, v in calculations.items():
        print(f'{k}: {v}')

    print('-' * 20, '\n')


if __name__ == '__main__':
    run()
