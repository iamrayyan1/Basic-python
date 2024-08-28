def main():
    temperatures = []

    print("Enter the daily temperatures for the month: ")
    for _ in range(30):
        temp = int(input())
        temperatures.append(temp)

    print(f"Average Temperature for Month: {avg_temp(temperatures)}")

    low, high = high_low_temp(temperatures)
    print(f"Lowest Temperature: {low}\nHighest Temperature: {high}")

    sorted_list = sort_list(temperatures)
    print(f"Sorted Temperatures: {sorted_list}")

    day_remove = int(input("Enter the day number (1-30) to remove its temperature: "))
    updated_list = remove(temperatures, day_remove)
    print(f"Updated Temperatures after removing day {day_remove}: {updated_list}")



def avg_temp(temperatures):
    total = sum(temperatures)
    avg = total / len(temperatures)
    return avg



def high_low_temp(temperatures):
    low = float('inf')
    high = float('-inf')

    for temp in temperatures:
        if temp < low:
            low = temp
        if temp > high:
            high = temp

    return low, high



def sort_list(temperatures):
    sorted_list = temperatures[:]
    for i in range(len(sorted_list)):
        for j in range(0, len(sorted_list) - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    return sorted_list


def remove(temperatures, day):
    temperatures.pop(day - 1)
    return temperatures


main()
