# an array list
# Sarah A. and Stefany A.

gluten_ls = dict([["flour","black bean puree"],["breadcrumbs","ground flaxseed or crushed potato chips"],["flour tortillas","corn tortillas"]])
sugar_ls = dict([["chocolate chips","cacao nibs"]])
dairy_ls = dict([["butter","avocado puree or olive oil"],["milk","rice, soy, oat, or almond milk"],["heavy cream","coconut milk"],["cheese","soy cheese"],["cream cheese","dairy-free cream cheese"],["sour cream","dairy-free sour cream"]])
vegan_ls = dict([["butter","avocado puree or olive oil"],["milk","almond milk"], ["heavy cream","coconut milk"],["ground beef","textured vegetable protein"]])
lowso_ls = dict([["salt","herbs, citrus juice, or garlic powder"],["breadcrumbs","rolled oats"]])
lgi_ls = dict([["rice","wild rice"],["penne","cheese tortellini"],["white bread","sourdough bread"]])
ibs_ls = dict([["milk","rice, soy, or oat milk"],["cheese","soy cheese"],["cream cheese","dairy-free cream cheese"],["sour cream","dairy-free sour cream"],["ground beef","textured vegetable protein"],["mayonnaise","fat-free mayonnaise"],["salad dressing","fat-free salad dressing"]])


    #join the sentence so that only one variable is edited
    #sentc.join

def recur_replace(key, file, dictionary_lst):
    if key == len(dictionary_lst):
        return "Done"
    else:
        value_ls=[]
        for val in dictionary_lst.itervalues():
            value_ls.append(val)
        for i in value_ls[:]:
            print("inner ",file.replace(key, i))
            value_ls.remove(i)
            print(value_ls)
        dictionary_lst.pop(key) 
        # Key Error - you already popped the butter when you want to pop it again
        return recur_replace(key, file, dictionary_lst)


def main(dictionary_lst):
    filename = "cookies.txt"

    #print("THIS IS THE DICT TYPE",type(dictionary_lst))
    #sentenc_arr = [] #not sure if you need this
    word_ls = []
    #just reading through the file
    file_token = open(filename, "r")
    for file in file_token:
        body = file.split("-")
        for line in body: #body is all sentences
            sentc = line.split(",")
            #sentc is only a single sentence, last one
            #new_body = "".join(sentc)
            #print(sentc)
            #sentenc_arr.append(sentc)

    #join the sentence so that only one variable is edited
    #print(type(sentc))
    #print("THIS IS THE OLD FILE VARIABLE", file)
    new_file = " ".join(body)
    #new_file = []
    ##print("THIS IS THE JOINED SENTENCES", new_file)
    '''value = dictionary_lst.values()
    print("this are the value of dict ", value)
    key = dictionary_lst.get(key)
    print("this are the key of dict", key) '''
    for key in dictionary_lst.iterkeys():
            recur_replace(key, new_file, vegan_ls)

    print("outer ", new_file)


main(vegan_ls)
