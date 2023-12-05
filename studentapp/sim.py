from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

num=['0','1','2','3','4','5','6','7','8','9']
def mark_generation(ans,oans):


    ps = PorterStemmer()


    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(ans.lower())


    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            lis = []
            my_string = w
            only_characters = ""

            for char in my_string:
                if char.isalpha():
                    if char != "-" and char != "-" and char not in num:
                        only_characters += char
                    else:
                        lis.append(only_characters)
                        only_characters = ""
                elif char == " ":
                    lis.append(only_characters)
                    only_characters = ""
            else:
                lis.append(only_characters)
            # print(only_characters)
            # Output: "HelloWorld"
            for ww in lis:
                if len(ww) >= 3:
                    w = ps.stem(w)

                    filtered_sentence.append(w)
    word_tokens = word_tokenize(oans.lower())


    filtered_sentence1 = []

    for w in word_tokens:
        if w not in stop_words:
            lis = []
            my_string = w
            only_characters = ""

            for char in my_string:
                if char.isalpha():
                    if char != "-" and char != "-" and char not in num:
                        only_characters += char
                    else:
                        lis.append(only_characters)
                        only_characters = ""
                elif char == " ":
                    lis.append(only_characters)
                    only_characters = ""
            else:
                lis.append(only_characters)
            # print(only_characters)
            # Output: "HelloWorld"
            for ww in lis:
                if len(ww) >= 3:
                    w = ps.stem(w)

                    filtered_sentence1.append(w)

    X_set = set(filtered_sentence)
    Y_set = set(filtered_sentence1)
    l1=[]
    l2=[]
    # form a set containing keywords of both strings
    rvector = X_set.union(Y_set)
    for w in rvector:
        if w in X_set:
            l1.append(1)  # create a vector
        else:
            l1.append(0)
        if w in Y_set:
            l2.append(1)
        else:
            l2.append(0)
    c = 0

    # cosine formula
    for i in range(len(rvector)):
        c += l1[i] * l2[i]
    cosine = c / float((sum(l1) * sum(l2)) ** 0.5)
    print("similarity: ", cosine)
    return cosine

mark_generation("good","bad")