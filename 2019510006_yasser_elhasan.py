#gloabal variable
stop_words = ['able', 'about', 'above', 'abroad', 'according', 'accordingly', 'across',
              'actually', 'adj', 'after', 'afterwards', 'again', 'against', 'ago', 'ahead',
              "ain't", 'all', 'allow', 'allows', 'almost', 'alone', 'along', 'alongside',
              'already', 'also', 'although', 'always', 'am', 'amid', 'amidst', 'among',
              'amongst', 'an', 'and', 'another', 'any', 'anybody', 'anyhow', 'anyone',
              'anything', 'anyway', 'anyways', 'anywhere', 'apart', 'appear', 'appreciate',
              'appropriate', 'are', "aren't", 'around', 'as', "a's", 'aside', 'ask',
              'asking', 'associated', 'at', 'available', 'away', 'awfully', 'back',
              'backward', 'backwards', 'be', 'became', 'because', 'become', 'becomes',
              'becoming', 'been', 'before', 'beforehand', 'begin', 'behind', 'being',
              'believe', 'below', 'beside', 'besides', 'best', 'better', 'between',
              'beyond', 'both', 'brief', 'but', 'by', 'came', 'can', 'cannot', 'cant',
              "can't", 'caption', 'cause', 'causes', 'certain', 'certainly', 'changes',
              'clearly', "c'mon", 'co', 'co.', 'com', 'come', 'comes', 'concerning',
              'consequently', 'consider', 'considering', 'contain', 'containing',
              'contains', 'corresponding', 'could', "couldn't", 'course', "c's", 'currently',
              'dare', "daren't", 'definitely', 'described', 'despite', 'did', "didn't",
              'different', 'directly', 'do', 'does', "doesn't", 'doing', 'done', "don't", 'down',
              'downwards', 'during', 'each', 'edu', 'eg', 'eight', 'eighty', 'either', 'else',
              'elsewhere', 'end', 'ending', 'enough', 'entirely', 'especially', 'et', 'etc',
              'even', 'ever', 'evermore', 'every', 'everybody', 'everyone', 'everything',
              'everywhere', 'ex', 'exactly', 'example', 'except', 'fairly', 'far', 'farther',
              'few', 'fewer', 'fifth', 'first', 'five', 'followed', 'following', 'follows',
              'for', 'forever', 'former', 'formerly', 'forth', 'forward', 'found', 'four', 'from',
              'further', 'furthermore', 'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes',
              'going', 'gone', 'got', 'gotten', 'greetings', 'had', "hadn't", 'half', 'happens',
              'hardly', 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll",
              'hello', 'help', 'hence',
              'her', 'here', 'hereafter', 'hereby', 'herein', "here's", 'hereupon', 'hers',
              'herself', "he's", 'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how',
              'howbeit', 'however', 'hundred', "i'd", 'ie', 'if', 'ignored', "i'll", "i'm",
              'immediate', 'in', 'inasmuch', 'inc', 'inc.', 'indeed', 'indicate', 'indicated',
              'indicates', 'inner', 'inside', 'insofar', 'instead', 'into', 'inward', 'is',
              "isn't", 'it', "it'd", "it'll", 'its', "it's", 'itself', "i've", 'just', 'k',
              'keep', 'keeps', 'kept', 'know', 'known', 'knows', 'last', 'lately', 'later',
              'latter', 'latterly', 'least', 'less', 'lest', 'let', "let's", 'like', 'liked',
              'likely', 'likewise', 'little', 'look', 'looking', 'looks', 'low', 'lower', 'ltd',
              'made', 'mainly', 'make', 'makes', 'many', 'may', 'maybe', "mayn't", 'me', 'mean',
              'meantime', 'meanwhile', 'merely', 'might', "mightn't", 'mine', 'minus', 'miss',
              'more', 'moreover', 'most', 'mostly', 'mr', 'mrs', 'much', 'must', "mustn't", 'my',
              'myself', 'name', 'namely', 'nd', 'near', 'nearly', 'necessary', 'need', "needn't",
              'needs', 'neither', 'never', 'neverf', 'neverless', 'nevertheless', 'new', 'next',
              'nine', 'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone', 'no-one',
              'nor', 'normally', 'not', 'nothing', 'notwithstanding', 'novel', 'now', 'nowhere',
              'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'on', 'once', 'one',
              'ones', "one's", 'only', 'onto', 'opposite', 'or', 'other', 'others', 'otherwise',
              'ought', "oughtn't", 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall',
              'own', 'particular', 'particularly', 'past', 'per', 'perhaps', 'placed', 'please',
              'plus', 'possible', 'presumably', 'probably', 'provided', 'provides', 'que',
              'quite', 'qv', 'rather', 'rd', 're', 'really', 'reasonably', 'recent', 'recently',
              'regarding', 'regardless', 'regards', 'relatively', 'respectively', 'right',
              'round', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second', 'secondly',
              'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves',
              'sensible', 'sent', 'serious', 'seriously', 'seven', 'several', 'shall', "shan't",
              'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'since', 'six', 'so',
              'some', 'somebody', 'someday', 'somehow', 'someone', 'something', 'sometime',
              'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specified', 'specify',
              'specifying', 'still', 'sub', 'such', 'sup', 'sure', 'take', 'taken', 'taking',
              'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that', "that'll",
              'thats', "that's", "that've", 'the', 'their', 'theirs', 'them', 'themselves',
              'then', 'thence', 'there', 'thereafter', 'thereby', "there'd", 'therefore',
              'therein', "there'll", "there're", 'theres', "there's", 'thereupon', "there've",
              'these', 'they', "they'd", "they'll", "they're", "they've", 'thing', 'things',
              'think', 'third', 'thirty', 'this', 'thorough', 'thoroughly', 'those', 'though',
              'three', 'through', 'throughout', 'thru', 'thus', 'till', 'to', 'together', 'too',
              'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', "t's",
              'twice', 'two', 'un', 'under', 'underneath', 'undoing', 'unfortunately', 'unless',
              'unlike', 'unlikely', 'until', 'unto', 'up', 'upon', 'upwards', 'us', 'use',
              'used', 'useful', 'uses', 'using', 'usually', 'v', 'value', 'various', 'versus',
              'very', 'via', 'viz', 'vs', 'want', 'wants', 'was', "wasn't", 'way', 'we', "we'd",
              'welcome', 'well', "we'll", 'went', 'were', "we're", "weren't", "we've", 'what',
              'whatever', "what'll", "what's", "what've", 'when', 'whence', 'whenever', 'where',
              'whereafter', 'whereas', 'whereby', 'wherein', "where's", 'whereupon', 'wherever',
              'whether', 'which', 'whichever', 'while', 'whilst', 'whither', 'who', "who'd",
              'whoever', 'whole', "who'll", 'whom', 'whomever', "who's", 'whose', 'why', 'will',
              'willing', 'wish', 'with', 'within', 'without', 'wonder', "won't", 'would', "wouldn't",
              'yes', 'yet', 'you', "you'd", "you'll", 'your', "you're", 'yours', 'yourself',
              'yourselves', "you've", 'zero', 'a', "how's", 'i', "when's",
              "why's", 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
              't', 'u', 'uucp', 'w', 'x', 'y', 'z', 'I', 'www', 'amount', 'bill', 'bottom', 'call',
              'computer', 'con', 'couldnt', 'cry', 'de', 'describe', 'detail', 'due', 'eleven', 'empty',
              'fifteen', 'fifty', 'fill', 'find', 'fire', 'forty', 'front', 'full', 'give', 'hasnt',
              'herse', 'himse', 'interest', 'itseâ€\u200c', 'mill', 'move', 'myseâ€\u200c', 'part',
              'put', 'show', 'side', 'sincere', 'sixty', 'system', 'ten', 'thick', 'thin', 'top',
              'twelve', 'twenty', 'abst', 'accordance', 'act', 'added', 'adopted', 'affected', 'affecting',
              'affects', 'ah', 'announce', 'anymore', 'apparently', 'approximately', 'aren', 'arent',
              'arise', 'auth', 'beginning', 'beginnings', 'begins', 'biol', 'briefly', 'ca', 'date',
              'ed', 'effect', 'et-al', 'ff', 'fix', 'gave', 'giving', 'heres', 'hes', 'hid', 'home',
              'id', 'im', 'immediately', 'importance', 'important', 'index', 'information', 'invention',
              'itd', 'keys', 'kg', 'km', 'largely', 'lets', 'line', "'ll", 'means', 'mg', 'million',
              'ml', 'mug', 'na', 'nay', 'necessarily', 'nos', 'noted', 'obtain', 'obtained', 'omitted',
              'ord', 'owing', 'page', 'pages', 'poorly', 'possibly', 'potentially', 'pp', 'predominantly',
              'present', 'previously', 'primarily', 'promptly', 'proud', 'quickly', 'ran', 'readily', 'ref',
              'refs', 'related', 'research', 'resulted', 'resulting', 'results', 'run', 'sec', 'section',
              'shed', 'shes', 'showed', 'shown', 'showns', 'shows', 'significant', 'significantly',
              'similar', 'similarly', 'slightly', 'somethan', 'specifically', 'state', 'states', 'stop',
              'strongly', 'substantially', 'successfully', 'sufficiently', 'suggest', 'thered', 'thereof',
              'therere', 'thereto', 'theyd', 'theyre', 'thou', 'thoughh', 'thousand', 'throug', 'til',
              'tip', 'ts', 'ups', 'usefully', 'usefulness', "'ve", 'vol', 'vols', 'wed', 'whats',
              'wheres', 'whim', 'whod', 'whos', 'widely', 'words', 'world', 'youd', 'youre']


#this function to remove the punctuations from the text
def remove_punctuations(line):
    for character in "‌‌âœ[-+=1234567890’'\"(){}<>\\[]:,‒–—―…!.«»-‐™?‘’“”;/⁄␠·&@*•^¤¢$€£¥₩₪†‡°¡¿¬#№%‰‱¶′§~¨_|¦⁂☞∴‽※":
        line = line.replace(character, "")
    return line

#this function is used to sort the element of a dictionary depending on our need
# and returns it as sorted list
def sort_dictionary(dictionary):
    sorted_values = []
    for key in dictionary:
        sorted_values.append((dictionary[key], key))
    sorted_values = sorted(sorted_values)
    sorted_values = sorted_values[::-1]
    return sorted_values


def Word_Order_Frequency_One_Book(book, word_order, file_output):
    try:
        read_book = open(book, "r", encoding="utf-8")
    except IOError:
        print("Error!! File is not found, Please try with a correct file name.")
        return 0

    file = open(file_output, "w", encoding="utf-8")

    if (word_order == 1):
        word_count_dic = {}#this dictionary is to have words with their frequency.

        for line in read_book:
            line = remove_punctuations(line).lower()#remove punctuations
            words = line.split()#each line from the text is sepleted and its words are added to the list

            words = [word for word in words if word not in stop_words]

            for word in words:
               #adding words and frequencies to the dictionary
                if word not in word_count_dic:
                    word_count_dic[word] = 0
                word_count_dic[word] += 1

        top_words = sort_dictionary(word_count_dic)[:100]#contains the top 100 words which are sorted

        file.write("| WORD           |  WORD        |\n"
              "| ORDER          |  ORDER       |\n"
              "| FREQUENCY      |  SEQUENCE    |\n")
        file.write('-------------------------------------------------------------'+ '\n')
        for tuple_freq in top_words:
            count, word = tuple_freq#words and their frequencies are sorted as tuples

            file.write(' {:4d}{:12s}{:s}{:2s}{:s} '.format(count," ","|"," ", word)+'\n')
    elif (word_order == 2):#this part (elif) does the same task like the last part,but the different is
        #instead of searching for 1 words , it searchs for 2.
        word_count_dic = {}


        for line in read_book:
            line = remove_punctuations(line).lower()
            words = line.split()

            words = [word for word in words if word not in stop_words]
            twoWords = []
            for i in range(len(words) - 1):
                twoWords.append(tuple(words[i:i + 2]))

            words = twoWords
            for word in words:

                if word not in word_count_dic:
                    word_count_dic[word] = 0
                word_count_dic[word] += 1

        top_words = sort_dictionary(word_count_dic)[:100]
        file.write("| WORD           |  WORD        |\n"
                   "| ORDER          |  ORDER       |\n"
                   "| FREQUENCY      |  SEQUENCE    |\n")
        file.write('-------------------------------------------------------------' + '\n')

        for tuple_freq in top_words:


            count, word = tuple_freq
            phrase = word[0] + " " + word[1]
            file.write(' {:4d}{:12s}{:s}{:2s}{:s} '.format(count," ","|"," ", phrase)+'\n')


    else:
        print("Error !! Please try again with correct parameters .")
    print("done!!")


def Word_Order_Frequency_Two_Books(book1, book2, word_order, file_output):
    try:
        read_book = open(book1, "r")
        read_book2 = open(book2, "r")
    except IOError:
        print("Error!! File is not found, Please try with a correct file name.")
        return 0

    output = open(file_output, "w")

    if (word_order == 1):

        word_count_dic = {} # this dictionary from the first book.

        for line in read_book:
            line = remove_punctuations(line).lower()
            words = line.split()

            words = [word for word in words if word not in stop_words]

            for word in words:
             # adding words to the dictionary with their frequencies from book 1.
                if word not in word_count_dic:
                    word_count_dic[word] = 0
                word_count_dic[word] += 1



        word_count_dic2 = {}# this dictionary from the second book.
        for line in read_book2:
            line = remove_punctuations(line).lower()
            words2 = line.split()

            words2 = [word for word in words2 if word not in stop_words]

            for word in words2:
                # adding words to the dictionary with their frequencies from book 2.

                if word not in word_count_dic2:
                    word_count_dic2[word] = 0
                word_count_dic2[word] += 1
        top_words = sort_dictionary(word_count_dic)[:1000]
        top_words2 = sort_dictionary(word_count_dic2)[:1000]

        AllWords = {}# the common words between the two books


        for i in range(len(top_words)):
            for j in range(len(top_words2)):
                if (top_words[i][1] == top_words2[j][1]):
                    AllWords.update(
                        {top_words[i][1]: {"freq1": top_words[i][0], "freq2": top_words2[j][0],
                                           "sum": top_words[i][0] + top_words2[j][0]}})

        sortedDic = []#sorting common words depending on the sum of frequencies
        for key in AllWords:
            sortedDic.append(
                (AllWords[key]["sum"], AllWords[key]["freq1"], AllWords[key]["freq2"], key))

        sortedDic = sorted(sortedDic)[::-1]
        counter = 1
        output.write("| TOTAL     | BOOK 1    | BOOK 2    | WORD     |\n"
              "| ORDER     | ORDER     | ORDER     | ORDER    |\n"
              "| FREQUENCY | FREQUENCY | FREQUENCY | SEQUENCE |\n"
              )
        output.write("----------------------------------------------------------------\n")
        for key in range(len(sortedDic)):

            output.write(
                "{:5d}{:7}{:}{:1}{:3d}{:7}{:}{:1}{:3d}{:7}{:}{:1}{:10}".format(sortedDic[key][0]," ","|"," ", sortedDic[key][1]," ","|"," ", sortedDic[key][2]," ","|"," ",
                                                        sortedDic[key][3]) + "\n")
            if (counter == 100):
                break
            counter += 1


    elif (word_order == 2):#this part does the same task like the last previous part (if word order==1)
        #but it searchs for two words instead of one word.
        word_count_dic = {}

        for line in read_book:
            line = remove_punctuations(line).lower()
            words = line.split()

            words = [word for word in words if word not in stop_words]
            twoWords = []
            for i in range(len(words) - 1):
                twoWords.append(tuple(words[i:i + 2]))

            words = twoWords
            for word in words:
                # word = word.lower()

                if word not in word_count_dic:
                    word_count_dic[word] = 0
                word_count_dic[word] += 1

        word_count_dic2 = {}
        for line in read_book2:
            line = remove_punctuations(line).lower()
            words2 = line.split()

            words2 = [word for word in words2 if word not in stop_words]
            twoWords = []
            for i in range(len(words2) - 1):
                twoWords.append(tuple(words2[i:i + 2]))

            words2 = twoWords

            for word in words2:

                if word not in word_count_dic2:
                    word_count_dic2[word] = 0
                word_count_dic2[word] += 1
        top_words = sort_dictionary(word_count_dic)[:1000]
        top_words2 = sort_dictionary(word_count_dic2)[:1000]

        AllWords = {}

        for i in range(len(top_words)):
            for j in range(len(top_words2)):
                if (top_words[i][1] == top_words2[j][1]):
                    AllWords.update(
                        {top_words[i][1]: {"freq1": top_words[i][0], "freq2": top_words2[j][0],
                                           "sum": top_words[i][0] + top_words2[j][0]}})

        sortedDic = []
        for key in AllWords:
            sortedDic.append(
                (AllWords[key]["sum"], AllWords[key]["freq1"], AllWords[key]["freq2"], key))

        sortedDic = sorted(sortedDic)[::-1]
        counter = 1
        output.write("| TOTAL     | BOOK 1    | BOOK 2    | WORD     |\n"
                     "| ORDER     | ORDER     | ORDER     | ORDER    |\n"
                     "| FREQUENCY | FREQUENCY | FREQUENCY | SEQUENCE |\n"
                     )
        output.write("----------------------------------------------------------------\n")
        for key in range(len(sortedDic)):
            phrase = sortedDic[key][3][0] + " " + sortedDic[key][3][1]
            output.write(
                "{:5d}{:7}{:}{:1}{:3d}{:7}{:}{:1}{:3d}{:7}{:}{:1}{:10}".format(sortedDic[key][0], " ", "|", " ",
                                                                               sortedDic[key][1], " ", "|", " ",
                                                                               sortedDic[key][2], " ", "|", " ",
                                                                               phrase) + "\n")

            if (counter == 100):
                break
            counter += 1


    else:
        print("Error !! Please try again with correct parameters .")
    print("done!!")


#Word_Order_Frequency_One_Book("book_1.txt",2, "output.txt")
#Word_Order_Frequency_Two_Books("book_1.txt", "book_2.txt",2, "output.txt")
#print("done!!")