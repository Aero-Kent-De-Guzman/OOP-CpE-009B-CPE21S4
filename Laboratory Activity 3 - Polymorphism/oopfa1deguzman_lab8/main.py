from FileReaderWriter import FileReaderWriter
from CSVFileReaderWriter import CSVFileReaderWriter
from JSONFileReaderWriter import JSONFileReaderWriter
from TextFileReaderWriter import TextFileReaderWriter

df = FileReaderWriter()
df.read()
df.write()

c = CSVFileReaderWriter()
c.read("sample.csv")
c.write(filepath= "sample2.csv", data=["Hello","World"])

j = JSONFileReaderWriter()
j.read("sample.json")
j.write(data=['foo', {'bar': ('baz', None, 1.0, 2)}], filepath="sample2.json")

file = TextFileReaderWriter()
file.read("test.txt")
x = input('Please enter anything to overwrite the .txt file : \n')
file.write(filepath = "test.txt", data = x)
file.read("test.txt")