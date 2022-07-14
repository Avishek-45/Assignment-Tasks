# Given Dictionary:

# Global Variables

chest = {
'42': 'It is the Answer to Life the Universe and Everything.',
'666': 'If you would be a real seeker after truth, it is necessary that at least once in your life you doubt, as far as possible, all things.',
'8': 'It is wrong always, everywhere and for everyone, to believe anything upon insufficient evidence.',
'13': 'The Truth is in the Heart.',
'0': 'Freedom is secured not by the fulfilling of ones desires, but by the removal of desire.',
'9': 'The unexamined life is not worth living.',
'76': 'Life is a series of natural and spontaneous changes.',
'70': 'God is dead! He remains dead! And we have killed him.'
}
sorted_chest = {}


def sort(array):
    """Sorting the array by using quicksort Algorithm."""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return sort(less)+equal+sort(greater)
    else:  
        return array

def Question1():
  chest_key_list = [int(i) for i in chest.keys()]
  sorted_list = sort(chest_key_list)
  sorted_chest_dict = {f'{i}':chest[f'{i}'] for i in sorted_list}
  # print(f"The sorted dictionary by its keys => \n{sorted_chest_dict}")
  global sorted_chest
  sorted_chest = sorted_chest_dict

def Question2():
  dict_keys = list(sorted_chest.keys())
  first_value = sorted_chest[dict_keys[0]]
  second_value = sorted_chest[dict_keys[1]]
  last_value = sorted_chest[dict_keys[-1]]
  second_last_value = sorted_chest[dict_keys[-2]]
  return [dict_keys[0], dict_keys[1] , dict_keys[-1] , dict_keys[-2]]

def Question3():
  required_keys = Question2()
  question3_result = " ".join(sorted_chest[i] for i in required_keys)
  # print(f"The answer of Question 3: {question3_result}")
  return question3_result

def Question4():
  sentence = Question3()
  spl = sentence.split(" ")
  lists = []
  for i in spl:
    lists.append(i[0])
    lists.append(i[-1])
  question4_result = "".join(map(str,lists))
  # print(f"The answer of Question 4: {question4_result}")
  return question4_result
    
def Question5():
  string = Question4()
  length = len(string)
  array = [i for i in string[0:length].lower() if i.isalpha()]
  # distinct_alphabets = set(array)
  res = {}

  for i in array:
    if i in res:
      res[i] += 1
    else:
      res[i] = 1
  sorted_values = sort(list(res.values()))
  new_dict = {}
  for i in sorted_values[::-1][0:5]:
    keys = [k for k, v in res.items() if v == i]
    for i in keys:
      new_dict[i] = res[i]
  
  # print(f'The number of occurrences of top 5 letters are : \n {new_dict}')

  return list(new_dict.values())

def Question7():
  a =  [52,51,61,71,56] #Given in Question num 6
  b = Question5()
  c=[]
  for x in range(0,5):
      c.append(a[x]+b[x])
  # print(f"The answer of Question 7 is: {c}")
  return c

def Question8():
  array = Question7()
  final_result = "".join([chr(i) for i in array])
  print(f'The final result is: `{final_result}`')

Question1()
Question2()
Question3()
Question4()
Question5()
Question7()
Question8()