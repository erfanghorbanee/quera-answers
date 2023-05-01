from bs4 import BeautifulSoup


def process(name):
    f = open(name, "r")
    document = BeautifulSoup(f.read(), "html.parser")
    t = document.find_all("a")
    # print(document.prettify())
    return len(t)
