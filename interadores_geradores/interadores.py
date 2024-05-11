class FileRead:
    def __init__(self, file_name):
        self.file = open(file_name,  encoding="utf8")

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if line != '':
            return line
        else:
            self.file.close()
            raise StopIteration


for l in FileRead('HISTORIC.txt'):
    print(l)

