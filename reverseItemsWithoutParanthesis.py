'''
You have a text that some of the words in reverse order.
The text also contains some words in the correct order, and they are wrapped in parenthesis.
Write a function fixes all of the words and,
remove the parenthesis that is used for marking the correct words.

Your function should return the same text defined in the constant CORRECT_ANSWER
'''


INPUT = ("nhoJ (Griffith) nodnoL saw (an) (American) ,tsilevon "
         ",tsilanruoj (and) laicos .tsivitca ((A) reenoip (of) laicremmoc "
         "noitcif (and) naciremA ,senizagam (he) saw eno (of) (the) tsrif "
         "(American) srohtua (to) emoceb (an) lanoitanretni ytirbelec "
         "(and) nrae a egral enutrof (from) ).gnitirw")

CORRECT_ANSWER = "John Griffith London was an American novelist, journalist, and social activist. (A pioneer of commercial fiction and American magazines, he was one of the first American authors to become an international celebrity and earn a large fortune from writing.)"


def fix_text(mystr):
    #boş bir string yapısı oluşturdum..
    my_str_new = ""
    
    #gelen stringi bir listeye her bir boşluktan sonrasını virgülle ayırdım.
    my_list = mystr.split(' ')
    
    #my_list eleman sayısı kadar indexlerde gezmek için ve işlem yapmak için for yapısı.
    for i in range(len(my_list)):
        # her bir indexin kendi içinde ilk indexi parantez değilse 
        tut = my_list[i][0]
        if tut != '(':
            #koşul sağlandıysa her bir elementi ters çevir
            my_str_new +=''.join(my_list[i][::-1])
        else:
            #koşul sağlanmadıysa, yani parantezli bir yapı varsa o yapının 1. indexinden son indexine kadar(dahil değil) alıp direkt
            #olduğu gibi ters çevirmeden parantezleri de almamış olarak joinledim.
            my_str_new +=''.join(my_list[i][1:-1])
        
        #her bir kelimededen sonra boşluk eklemesi yaptım
        my_str_new +=" "
    
    #çıktıyı görmek için...
    print(my_str_new)
    
    return my_str_new



if __name__ == "__main__":
    print("Correct!" if fix_text(INPUT) == CORRECT_ANSWER else "Sorry, it does not match with the correct answer.")