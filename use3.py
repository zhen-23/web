from test1 import calculate_sum

def main():
    try:
        num = int(input("請輸入一個正整數 N: "))
        result = calculate_sum(num)
        print(f"從 1 累加到 {num} 的結果為: {result}")
    except ValueError:
        print("錯誤：請輸入有效的整數！")

if __name__ == "__main__":
    main()