class Polindrome:

    def reverse(self,word):
        print((word[ : : -1]))

    def IsPolindrome(self,word):
        if(word==word[ : : -1]):
           print("True")
        else:
            print("False")
           
ab=Polindrome()
word=input("Enter any word ")
ab.reverse(word)
ab.IsPolindrome(word)