# -*- coding: utf-8 -*-
import random

CASES = ['simple'] * 5 + ['spare'] * 3 + ['strike'] + ['miss'] * 2

PLAYERS = ['Алексей', 'Дмитрий', 'Роман', 'Елена', 'Ринат', 'Наталия', 'Павел', 'Татьяна', 'Антон', 'Давид']

POSSIBLE_ERRORS = ['frames_count', 'pins_count', 'first_/', 'second_X', 'one_miss']


def _mess(mess, ff):
    print(mess, end='')
    ff.write(mess)


possible_errors = []
with open('tournament.txt', 'w') as ff:
    errors = 0
    for tour in range(1, 101):
        _mess(f'### Tour {tour}\n', ff)

        members = random.randint(2, 7) if tour > 5 else 5
        players = PLAYERS[:]
        team = []
        for _ in range(members):
            player = random.choice(players)
            team.append(player)
            players.remove(player)

        if not possible_errors:
            possible_errors = POSSIBLE_ERRORS[:]
            print('----------------------------------- possible_errors populated')
        can_error = tour > 10

        for member in team:
            result = ''
            error_on_player = can_error and possible_errors and random.randint(1, 17) == 1
            error_type = None
            if error_on_player:
                error_type = random.choice(possible_errors)
                possible_errors.remove(error_type)
                print(f'======================================== error_on_player {error_type}')
            if error_type == 'frames_count':
                errors += 1
                frames_count = random.randint(8, 13)
                print(f'--------------------------------------- error frames_count {frames_count}')
            else:
                frames_count = 10
            for frame in range(frames_count):
                frame_type = random.choice(CASES)
                error = error_on_player and random.randint(1, 5) == 1
                if frame_type == 'simple':
                    if error and error_type == 'pins_count':
                        first = random.randint(1, 9)
                        result += str(first)
                        second = 0
                        while first + second <= 10:
                            second = random.randint(1, 9)
                        result += '-' if second == 0 else str(second)
                        print(f'--------------------------------------- error pins_count {result}')
                        errors += 1
                    first = random.randint(0, 8)
                    result += '-' if first == 0 else str(first)
                    rest = 10 - first
                    second = random.randint(0, rest)
                    result += '-' if second == 0 else str(second)
                elif frame_type == 'strike':
                    if error and error_type == 'second_X':
                        result += '{}X'.format(random.choice('-123456789'))
                        print(f'------------------------------------------- second_X {result}')
                        errors += 1
                    else:
                        result += 'X'
                elif frame_type == 'spare':
                    if error and error_type == 'first_/':
                        result += '/{}'.format(random.choice('-123456789'))
                        print(f'------------------------------------------- first_/ {result}')
                        errors += 1
                    else:
                        first = random.randint(1, 9)
                        result += '-' if first == 0 else str(first)
                        result += '/'
                elif frame_type == 'miss':
                    if error and error_type == 'one_miss':
                        result += '-'
                        print(f'------------------------------------------- one_miss {result}')
                        errors += 1
                    else:
                        result += '--'
            _mess(f'{member}\t{result}\n', ff)
        _mess('winner is .........\n\n', ff)
    print(errors)
