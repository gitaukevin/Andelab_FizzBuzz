#the function should be words. let's define it
def words(phrase):
  My_list=phrase.split() #My_list contains the phrase to be split. slipt () works in this manner>>>> phrase.split(str="", num=string.count(str))
  clever=set(My_list) #puts the variavle clever as a set of the length of the variable My_list
  dictonary={} #this is the variable to set counts in
  for clever in My_list:
    dictonary[clever]=My_list.count(clever)
  return dictonary 