import wget

batches = ["a", "b", "c", "d", "e-f", "g", "h", "i-j", "k", "l", "m", "n-o", "p-q", "r", "s", "t", "u-v", "w", "x-y-z"]

counter = 0

for batch in batches:
    url = "http://www.atrilcoral.com/Partituras_ABC/{}.zip".format(batch)
    location = "/{}.zip".format(counter)
    wget.download(url)
    counter += 1
