import urllib2
from bs4 import BeautifulSoup

#count + newText.count(' ') <=500

def fixFile(file):
    lines = []
    with open(file, "r") as text_file:
        for line in text_file:
            if line[0] == ' ':
                line = line[1:]
            if line != "\n":
                lines.append(line)

    with open(file, "w") as text_file:
        for line in lines:
            text_file.write(line)

def scienceTechFile(url, number):
    try:
        html = urllib2.urlopen(url)
    except:
        return "failed"
    shouldPrint = False
    wordCount = 0
    soup = BeautifulSoup(html, 'html.parser')
    cclicense = soup.find("a", {"class" : "license-logo"})
    author = soup.find("meta", {"name" : "author"})['content']
    with open("scitech_conversation"+"{:0>3d}".format(number)+".txt", "w") as text_file:
        for line in soup.find_all(['p', 'h3']):
            if "Write an article and join a growing community of more than" in str(line):
                #print "Works"
                shouldPrint = False
            if shouldPrint == True:
                if line.string == None:
                    for string in line.stripped_strings:
                        if wordCount + string.count(' ') + 1 > 360:
                            shouldPrint = False
                        elif string[0] not in ['.', ',', '!', '?', '"', "'"]:# and string[0] != string[0].upper():
                            text_file.write(' ')
                        text_file.write(string.encode('utf-8'))
                        wordCount += string.count(' ') + 1
                else:
                    if wordCount + line.string.count(' ') + 1 > 360:
                        shouldPrint = False
                    elif line.name == 'h3' and "You might also like" in str(line):
                        shouldPrint = False
                    elif line.name == 'h3' and "Languages" in str(line):
                        0
                    else:
                        text_file.write(line.string.encode('utf-8'))
                        wordCount += line.string.count(' ') + 1
                text_file.write("\n")
            elif cclicense in line:
                shouldPrint = True
    fixFile("scitech_conversation"+"{:0>3d}".format(number)+".txt")
    if wordCount < 300:
        return "tooshort"
    return author