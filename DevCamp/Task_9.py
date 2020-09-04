def main():
    s = input('Enter a String: ')

    s = s.lower()

    if s == s[::-1]:
        print('Yes')

    else:
        print('No')

main()
