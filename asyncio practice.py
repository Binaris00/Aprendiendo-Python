import asyncio

async def hola_mundo():
    print("HOLAAAAA")
    await asyncio.sleep(10)
    print("Mundo")

async def no():
    print("no")
    

if __name__ == "__main__":
    asyncio.run(hola_mundo())
    asyncio.run(no())