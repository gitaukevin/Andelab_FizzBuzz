def words(phrase):
  My_list=phrase.split()
  clever=set(My_list)
  dictonary={}
  for clever in My_list:
    dictonary[clever]=My_list.count(clever)
  return dictonary