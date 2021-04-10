import pandas

# with open("de.txt", encoding="utf-8") as file:
#     lines = file.readlines()
#
# words = []
#
# for line in lines:
#     line = line.strip()
#     row = line.split(sep=" ")
#     words.append(row)
#
# words_pandas = pandas.DataFrame(words)
# print(words_pandas)

french = pandas.read_csv("french_words.csv")
french.French.to_clipboard()