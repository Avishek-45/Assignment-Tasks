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


# Question Number (1):

def sort(array):
    """Sort the array by using quicksort."""

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
  print(f"The sorted dictionary by its keys => \n{sorted_chest_dict}")
  global sorted_chest
  sorted_chest = sorted_chest_dict

def Question2():
  dict_keys = list(sorted_chest.keys())
  first_value = sorted_chest[dict_keys[0]]
  second_value = sorted_chest[dict_keys[1]]
  last_value = sorted_chest[dict_keys[-1]]
  second_last_value = sorted_chest[dict_keys[-2]]
  print(first_value)
  print(second_value)
  print(last_value)
  print(second_last_value)

Question1()
Question2()
# print(sorted_chest)

