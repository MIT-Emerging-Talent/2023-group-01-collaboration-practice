# This code will randomize the orginal array order and will save it into a new variable 
# without affecting the orignal array
import random

def randomize_array(original_array):
    shuffled_array = original_array.copy()
    random.shuffle(shuffled_array)
    return shuffled_array

# Example usage
original_array = [1, 2, 3, 4, 5]
randomized_array = randomize_array(original_array)

print("Original Array:", original_array)
print("Randomized Array:", randomized_array)
