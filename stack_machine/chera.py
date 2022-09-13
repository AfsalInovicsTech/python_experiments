

with open("sample.txt") as f:
    for i in f:
        cleaned_line = i.replace(' ', '')
        print(cleaned_line)
