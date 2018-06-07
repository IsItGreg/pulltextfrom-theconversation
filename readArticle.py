import urllib2
from bs4 import BeautifulSoup

def fixFile(file):
    lines = []
    with open(file, "r") as text_file:
        for line in text_file:
            if line[0] == ' ':
                line = line[1:]
            lines.append(line)

    with open(file, "w") as text_file:
        for line in lines:
            text_file.write(line)


def readArticle(url, number):
    try:
        html = urllib2.urlopen(url)
    except:
        return "failed"
    shouldPrint = False
    soup = BeautifulSoup(html, 'html.parser')
    cclicense = soup.find("a", {"class" : "license-logo"})
    author = soup.find("meta", {"name" : "author"})['content']
    with open("conversation"+"{:0>3d}".format(number)+".txt", "w") as text_file:
        for line in soup.find_all(['p', 'h2', 'h3']):
            if "Write an article and join a growing community of more than" in str(line):
                #print "Works"
                shouldPrint = False
            if shouldPrint == True:
                if line.string == None:
                    for string in line.stripped_strings:
                        if string[0] not in ['.', ',', '!', '?', '"', "'"]:# and string[0] != string[0].upper():
                            text_file.write(' ')
                        text_file.write(string.encode('utf-8'))
                else:
                    if line.name == 'h3' and "You might also like" in str(line):
                        shouldPrint = False
                    elif line.name == 'h2':
                        text_file.write(line.string.encode('utf-8').upper())
                    else:
                        text_file.write(line.string.encode('utf-8'))
                text_file.write("\n")
            elif cclicense in line:
                shouldPrint = True
    fixFile("conversation"+"{:0>3d}".format(number)+".txt")
    return author


