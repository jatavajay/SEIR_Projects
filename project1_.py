# Description:This Program Extracts title, body text , word frequency and links from given URL and compare similarity between two documents.

import sys  #load System module 
from bs4 import BeautifulSoup #its job is to parse html page and download data
import urllib.request  #urlib is main module while request is sub module

if len(sys.argv)>3: #sys.argv gets input from cmd line 
    print("You have entered %d url, please enter only one or two url" %(len(sys.argv)-1))
    sys.exit()
else:
    if len(sys.argv)==3: # sys.argv is list of cmd line argument which always contain first element as file name.
        print("Programme name is: ", sys.argv[0]) 
        url1=sys.argv[1]
        url2=sys.argv[2]
        print("url1 is: %s and url2 is: %s" % (url1, url2))
    elif len(sys.argv)==2:  
        url1=sys.argv[1]
        print("url1 is: ", sys.argv[1])
        print("Programme name is: ", sys.argv[0])
    else:
        print("No url entered in command line argument")
        sys.exit()  #stop and exit program

try:  #checking whether both url's are valid or not
    response1 = urllib.request.urlopen(url1) ##server send html content of website in bytes format which get stored in response
    if len(sys.argv)==3:
        response2=urllib.request.urlopen(url2)
except:
    print("You have entered Invalid URL")
    sys.exit()
 
# print(response1)  #it will shows object info not actual content
# print(response.read())  #print binary data of computer format, not normal text
def basic_info(pageContent):  # pageContent contains decoded data in normal text
    soup=BeautifulSoup(pageContent,"html.parser")
    print("Title of entered site is : ", soup.title.text)
    bodyText=soup.body.text
    print("Body of entered site is : ", bodyText)

    allLinks=soup.find_all("a")
    print("External links found are:")
    for link in allLinks:
        print(link.get("href"))

    bodyTextLst=bodyText.split()
    for i in range (len(bodyTextLst)):
        bodyTextLst[i]=bodyTextLst[i].lower()
    return bodyTextLst


from collections import Counter # inbuilt method to store frequency(like dictionary) in a in counter object {counter is subcls of dictionary}.
def count_frequency(lst):
    word_freq = Counter(lst)
    print("word frequencies are:", word_freq)
    return word_freq


def polynomial_hash(word):
    p = 53
    m = 2**64  #modulus m to prevent integer overflow
    hash_value = 0
    power = 1
    for ch in word:
        hash_value = (hash_value + ord(ch) * power) % m #ord(ch) gives ascci num of char
        power = (power * p) % m
    return hash_value


def sim_Hash(freqlst):
    bit_size = 64
    vector = [0] * bit_size
    for word in freqlst:
        hash_val=polynomial_hash(word)
        binary_num = format(hash_val, '064b') #convert decimal to 64 bit binary num (including leading 0's)
        weight=freqlst[word]
        for i in range (len(vector)):
            if binary_num[i]=='0':
                vector[i]-=weight
            else:
                vector[i]+=weight
    fingerprint=''
    for bit in vector:
        if bit>0:
            fingerprint+='1'
        else:
            fingerprint+='0'
    return fingerprint


#checking how many bits are common in both document's fingerprints.
def check_similarity(fingerPrint1,fingerPrint2): 
    common_bit=0
    for i in range (64):
        if fingerPrint1[i]==fingerPrint2[i]:
            common_bit+=1
    similar=(common_bit/64)*100
    return ("url1: %s is %.2f%% similar to url2: %s" % (url1, similar, url2))


# show result based on how many url user has given in command line argument.
if len(sys.argv)==3:
    pageContent1 = response1.read().decode()  #decode data binary to text format
    bodyTextLst = basic_info(pageContent1) 
    wordFreqLst = count_frequency(bodyTextLst)
    fingerPrint1 = sim_Hash(wordFreqLst)
    print("fingerprint of first document is :", fingerPrint1)

    pageContent2 = response2.read().decode()
    bodyTextLst2 = basic_info(pageContent2)
    wordFreqLst2 = count_frequency(bodyTextLst2)
    fingerPrint2 = sim_Hash(wordFreqLst2)
    print("fingerprint of second document is :", fingerPrint2)
    print(check_similarity(fingerPrint1, fingerPrint2))
else:
    pageContent1 = response1.read().decode()  
    bodyTextLst = basic_info(pageContent1) 
    wordFreqLst = count_frequency(bodyTextLst)
    fingerPrint1 = sim_Hash(wordFreqLst)
    print("fingerprint of this document is :", fingerPrint1)

print("Thank You! for using my program..")