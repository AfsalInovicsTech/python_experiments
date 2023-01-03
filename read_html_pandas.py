

import pandas
dfs = pandas.read_html("https://www.stackscale.com/blog/most-popular-programming-languages/")
print(dfs[0])
