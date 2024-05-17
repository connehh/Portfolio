def main():
    total = 0
    try:
        numbersfile = open('numbers.txt', 'r')

        line = numbersfile.readline(1)

        while line != '':
            amount = int(line)
            if (amount % 2) != 0:
                total += amount

            line = numbersfile.readline()

        print(f"this is the total: {total}")
        numbersfile.close()

    except FileNotFoundError as a:
        print(a)
    except ValueError as b:
        print(b)


if __name__ == '__main__':
    main()
