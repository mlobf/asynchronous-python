import asyncio


async def test(delay):
    await asyncio.sleep(delay)
    print('esperando')

async def run():

    t1 = asyncio.create_task(test(10))
    t2 = asyncio.create_task(test(10))
    t3 = asyncio.create_task(test(10))
    t4 = asyncio.create_task(test(10))
    t5 = asyncio.create_task(test(10))
    t6 = asyncio.create_task(test(10))
    t7 = asyncio.create_task(test(10))
    t8 = asyncio.create_task(test(10))

    await t1
    await t2
    await t3
    await t4
    await t5
    await t6
    await t7
    await t8

    print('finalizou')



if __name__ == '__main__':
    asyncio.run(run(), debug=True)

