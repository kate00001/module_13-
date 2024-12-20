import asyncio


async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования")

    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f"Силач {name} поднял {i} шар")

    print(f"Силач {name} закончил соревнования")


async def start_tournament():
    tasks = [
        start_strongman("Екатерина", 1),
        start_strongman("Амина", 2),
        start_strongman("Качок", 3),
    ]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(start_tournament())
