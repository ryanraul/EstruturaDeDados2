

def miniMaxSum(arr):
   max_value = max(arr)
   min_value = min(arr)
   max_sum = 0
   min_sum = 0
   aux_max = 0
   aux_min = 0

   for value in arr:
      if value != max_value or aux_max == 1:            
         min_sum += value
      else:
         aux_max = 1
      if value != min_value or aux_min == 1:
         max_sum += value
      else:
         aux_min = 1
   print(min_sum, max_sum)

   

arr = [1,3,5,7,9]
miniMaxSum(arr)