import csv

try:
    with open('exemple.csv', 'w', newline='') as file:
        write = csv.writer(file)
        write.writerow(['nome', 'idade'])
        write.writerow(['iuri', 30])
        write.writerow(['caio', 28])
except Exception as error:
    print(error)


try:
    with open('exemple.csv', 'r', encoding='utf-8') as file:
        reading = csv.reader(file)
        for line in reading:
            print(line)
except Exception as error:
    print(error)
