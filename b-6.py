import random

def main():
    dice_num = int(input("サイコロの面の数は?: "))
    dice_count = int(input("何回振りますか?: "))
    dice_list = []
    for i in range(dice_count):
        dice_list.append(random.randint(1, dice_num))
    print(dice_list)

if __name__ == "__main__":
    main()
