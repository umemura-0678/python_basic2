def data_total(data_list):
    total = 0
    for data in data_list:
        total += data
    return total


def data_max(data_list):
    max_d = data_list[0]
    for data in data_list:
        if data > max_d:
            max_d = data
    return max_d


def data_min(data_list):
    min_d = data_list[0]
    for data in data_list:
        if data < min_d:
            min_d = data
    return min_d


def data_average(data_list):
    return int(data_total(data_list) / len(data_list))


def main():
    data = input("データを入力してください(スペース区切り) > ")
    data_list = [int(i) for i in data.split()]
    print(f"合計値: {data_total(data_list)}")
    print(f"最大値: {data_max(data_list)}")
    print(f"最小値: {data_min(data_list)}")
    print(f"平均値: {data_average(data_list)}")


if __name__ == "__main__":
    main()
