#!/usr/bin/env python3

# Created by: Donggeun Lim
# Created on: Jan 2019
# This program prints mixed list fist list and second list


def get_mix_list(first_str, second_str):
    mix_list = []

    first_list = first_str.split(" ")
    second_list = second_str.split(" ")
    for count in range(len(first_list) + len(second_list)):
        if count % 2 == 0:
           mix_list.append(first_list[int(count/2)])
        else:
            mix_list.append(second_list[int((count-1)/2)])

    return mix_list


def main():

    first_str = input("Enter the fist list: ")
    second_str = input("Enter the second list: ")
    print("")

    mix_list = get_mix_list(first_str, second_str)

    print("Mixed list: ", end="")
    for index in mix_list:
        print(index, end=" ")
    # print(mix_list)


if __name__ == "__main__":
    main()
