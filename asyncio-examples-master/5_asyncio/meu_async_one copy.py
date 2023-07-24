import asyncio


async def test(delay):
    await asyncio.sleep(delay)
    print('esperando')

async def run():
    mylist = range(100000)
    final_list = []

    for _ in mylist:
        _ = asyncio.create_task(test(5))
        final_list.append(_)


    for x in final_list:
        await x

    print('rodou')





if __name__ == '__main__':
    asyncio.run(run(), debug=True)

