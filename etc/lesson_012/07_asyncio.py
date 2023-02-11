# -*- coding: utf-8 -*-
import asyncio
import random
from collections import defaultdict

FISH = (None, 'плотва', 'окунь', 'лещ')


async def fishing(name, worms):
    catch = defaultdict(int)
    for worm in range(worms):
        print(f'{name}: Червяк № {worm} - Забросил, ждем...', flush=True)
        await asyncio.sleep(0.1)
        fish = random.choice(FISH)
        if fish is None:
            print(f'{name}: Тьфу, сожрали червяка...', flush=True)
        else:
            print(f'{name}: Ага, у меня {fish}', flush=True)
            catch[fish] += 1
    print(f'Итого рыбак {name} поймал:')
    for fish, count in catch.items():
        print(f'    {fish} - {count}')


async def main():
    humans = ['Васек', 'Колян', 'Петрович', 'Хмурый', 'Клава']
    fishers = [fishing(name=name, worms=10) for name in humans]
    await asyncio.gather(*fishers)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
