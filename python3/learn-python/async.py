import asyncio
import time
#aiohttp


start_time = time.time()

async def find_divisibles(inrange, div_by):
    print("Finding nums in range {} divisible by {}".format(inrange, div_by))

    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)

        if i % 500000 == 0:
            await  asyncio.sleep(0.0001)

    print("Done w/ nums in range {} divisible by {}".format(inrange, div_by))
    return located

async def main():
    divs1 = loop.create_task(find_divisibles(102348, 4342))
    divs2 = loop.create_task(find_divisibles(1433245, 13))
    divs3 = loop.create_task(find_divisibles(123400, 7))

    await asyncio.wait([divs1, divs2, divs3])
    return divs1, divs2, divs3

if __name__ == "__main__":
    # Initialize our event loop
    try:
        loop = asyncio.get_event_loop()
        d1, d2, d3 = loop.run_until_complete(main())
        # loop.set_debug(1)
        print(d1.result())
    except Exception as e:
        pass
    finally:
        loop.close()

    print("--- %s seconds ---" % (time.time() - start_time))
