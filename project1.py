def checkWord(word2,word1):
    for i in word2:
        if i not in word1 or word2.count(i) > word1.count(i) :
            return False
    return True

def main():
    word1 = ""
    word2 = ""
    result = False
    while word1 != "last" and word2 != "last":
        print("Enter first word:")
        word1 = input()   
        print("Enter second word:")
        word2 = input() 
        if len(word1) <= len(word2):
            result = checkWord(word1,word2)
        else :
            result = checkWord(word2,word1)

        print("=>",result,"\n")
       
main()