#7
def get_even_list(yourlist):
    for number in yourlist:
        if int(number) % 2 == 1:
            yourlist.remove(number)
    return yourlist
#8
even_list = get_even_list([ 1 , 2 , 5 , - 10 , 9 , 6 ])
if set (even_list) == set ([ 2 , - 10 , 6 ]):
    print ( "Your function is correct" )
else :
    print ( "Ooops, bugs detected" )