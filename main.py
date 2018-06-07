import pandas as pd
from readArticle import readArticle
from scienceTechFile import scienceTechFile


def main():
    #testurl = "http://theconversation.com/statesman-strongman-philosopher-autocrat-chinas-xi-is-a-man-who-contains-multitudes-92962"
    #readArticle(testurl, 0)

    curindex = 0
    indexes = []
    authors = []
    titles = []
    urls = []
    tags = []

    stindex = 0
    stindexes = []
    stauthors = []
    sttitles = []
    sturls = []

    df = pd.read_csv("tc_articles (7).csv")

    array = df.values.tolist()
    for list in array:
        indexes.append("{:0>3d}".format(curindex))
        authors.append(readArticle(list[1], curindex))
        titles.append(list[0])
        urls.append(list[1])
        tags.append(list[2])
        curindex += 1
        if list[2] == "Science + Technology":
            stauthor = scienceTechFile(list[1], stindex)
            if stauthor != "tooshort":
                stindexes.append("{:0>3d}".format(stindex))
                stauthors.append(stauthor)
                sttitles.append(list[0])
                sturls.append(list[1])
                stindex += 1

        print "{:.2f}".format(curindex/61.0) + "% done"

    print ("Done: " + str(curindex))

    data = {'Author': authors, 'Title': titles, 'URL': urls, 'Category' : tags}
    output = pd.DataFrame(data, index=indexes).rename_axis("Text #", axis=1)
    output.to_csv('conversationMetadata.txt', sep='\t', encoding='utf-8')

    stdata = {'Author': stauthors, 'Title': sttitles, 'URL': sturls}
    output = pd.DataFrame(stdata, index=stindexes).rename_axis("Text #", axis=1)
    output.to_csv('scitech_conversationMetadata.txt', sep='\t', encoding='utf-8')


if __name__ == "__main__":
    main()
