#rank_compiler.py
#takes input speech from f
#and a comparison corpus from g
#and outputs to h
#which compiles in the following format:
#word + '\t' + str(listRank)+'\t' + str(list%-ile)+'\t' + str(docRank)+'\t'+ str(doc%-ile) +'\t' + str(distFromtarget) +'\n'
#where distFtarget is the square of the Euclidean distance from the 100th %-ile of the speech and 0% of the corpus
fname="word_frequency_trump_inaug_pruned89.txt"
#gname="most_frequent_5k_words.txt"
gname="word_frequency_all_presidents.txt"
hname="rank_rank_trump_vs_all_presidents_pruned89.txt"

f = open(fname)#speech to investigate
g = open(gname)#comparison corpus

h=open(hname,'w')
print(hname)
i=0

list_word=[]
list_rank=[]
for line in g:#making a copy of the reference list
    if i==0:
        i+=1
        continue
    try:
        word, listRank = line.split()[2],int(line.split()[0])
    except:
        continue
    
    list_word.append(word.lower())
    #print ("list_word adding" + word)
    list_rank.append(listRank)
    if word=="heavenly" or word =="suspended":
        print (line)

    i+=1
g.close()
i=0
h.write(" " + '\t' + " " + '\n')
print ("HERE")
rankList=[]
for line in f:
    try:
        rankList.append(int(line.split()[0]))
        #print (int(line.split()[0]))
    except:
        continue
f.close()

maxRank=max(rankList)
#print ("maxrank obama speech" + '\t' +str(maxRank))
maxListrank=max(list_rank)

f = open(fname)

for line in f:#opening up doc
    if i==0:
        i+=1
        continue
    #docRank, word = int(line.split()[0]),line.split()[1]
    docRank, wordcount, word = int(line.split()[0]),line.split()[1],line.split()[2]
    #print("Doc rank:" +'\t' + str(docRank))
    #print("Max rank:" +'\t' + str(maxRank))
    #print("Max rank:" +'\t' + str(int(docRank)/int(maxRank)))
    #print (word)
    found=0# found in the reference list of words
    docPercentile=100-docRank/maxRank*100.
    if word in list_word:
        listRank=list_rank[list_word.index(word)]
        listPercentile=100-listRank/maxListrank*100.
        distFromtarget=listPercentile*listPercentile+(100-docPercentile)*(100-docPercentile)
        stringtowrite=word + '\t' + str(listRank)+'\t' +  str(listPercentile)+'\t' + str(docRank) + '\t' +str(docPercentile) +\
        '\t' + str(distFromtarget)+'\n'
        #print (stringtowrite)
        h.write(stringtowrite)
        found=1
        #print ("MATCH")
        continue
    if found==0:
        listPercentile=0
        distFromtarget=listPercentile*listPercentile+(100-docPercentile)*(100-docPercentile)
        stringtowrite=word + '\t' + "5001" + '\t' + "0"  +'\t' + str(docRank)+'\t' +str(docPercentile)+'\t' + str(distFromtarget)+'\n'
        h.write(stringtowrite)
    i+=1
h.close()
