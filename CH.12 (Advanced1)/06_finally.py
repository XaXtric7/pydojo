def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:  # finally return ke bawjood bhi chalta hai..
        print("Hey I am inside of finally")


main()
