
import asyncio
async def fun1(x):
    await asyncio.sleep(3)
    print('число в квадрате')
    print(x**2)
    print('fun1 завершена')


async def fun2(x):
    await asyncio.sleep(3)
    print('квадратный корень из числа')
    print(x**0.5)
    print('fun2 завершена')

import csv

async def sav():
    await asyncio.sleep(4)
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([z**2, z**0.5])
async def sav2():
    await asyncio.sleep(5)
    with open('output.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


print("введи число")
z = int (input())
async def main():

    x = int (z) 
    task1 = asyncio.create_task(fun1(x))
    task2 = asyncio.create_task(fun2(x))
    task3 = asyncio.create_task(sav())
    task4 = asyncio.create_task(sav2())
    await task1
    await task2
    await task3
    await task4
asyncio.run(main())