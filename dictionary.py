# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

phone_book = {}

for i in range(n):
        name, phone_num = map(str,input().split())
        name = name.lower()
        phone_book[name] = phone_num

queries = 0

while queries in range(n):
        query = input().lower()
        if query in phone_book:
            print(query + "=" + phone_book.get(query))
        else:
            print("Not found")

        queries += 1
