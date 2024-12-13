#from Day1HistorianHysteria import 
import Day1Part1 as Day1


# Day 1 puzzle answer was 1651298.

"""
Your analysis only confirmed what everyone feared: the two lists of location IDs are indeed very different.

Or are they?

The Historians can't agree on which group made the mistakes or how to read most of the Chief's handwriting, 
but in the commotion you notice an interesting detail: 
- a lot of location IDs appear in both lists! 
- Maybe the other numbers aren't location IDs at all but rather misinterpreted handwriting.

This time, you'll need to figure out exactly how often each number from the left list appears in the right list. 
Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.

similarity score = num_left x frequency on right

Here are the same example lists again:

3   4
4   3
2   5
1   3
3   9
3   3

For these example lists, here is the process of finding the similarity score:

The first number in the left list is 3. It appears in the right list three times, so the similarity score increases by 3 * 3 = 9.
The second number in the left list is 4. It appears in the right list once, so the similarity score increases by 4 * 1 = 4.
The third number in the left list is 2. It does not appear in the right list, so the similarity score does not increase (2 * 0 = 0).
The fourth number, 1, also does not appear in the right list.
The fifth number, 3, appears in the right list three times; the similarity score increases by 9.
The last number, 3, appears in the right list three #times; the similarity score again increases by 9.
So, for these example lists, the similarity score at the end of this process is 31 (9 + 4 + 0 + 0 + 9 + 9).

Once again consider your left and right lists. What is their similarity score?
"""

#list1, list2 = Day1.getDay1Lists(Day1.PRACTICE_INPUT_FILE)
list1, list2 = Day1.getDay1Lists(Day1.INPUT_FILE)


list1.sort()
list2.sort()



def getCountDictionary(list1, list2):
    i = 0
    j = 0
    count = 0
    count_dict = {num: 0 for num in list1}  # Initialize all counts to 0

    while i < len(list1) and j < len(list2):  # Corrected bounds for list2

        while i < len(list1) and j < len(list2) and list2[j] > list1[i]:
            i += 1

        while i < len(list1) and j < len(list2) and list2[j] < list1[i]:
            j += 1

        while i < len(list1) and j < len(list2) and list2[j] == list1[i]:
            count_dict[list1[i]] += 1
            j += 1

    return count_dict


def calcSimilarityScore(list1, list2):
    similarity_score = 0
    similarities = getCountDictionary(list1, list2)

    for num in list1:
        product = num * similarities.get(num, 0)  # Safely get the count, default to 0
        similarity_score += product

    return similarity_score


list1, list2 = Day1.getDay1Lists(Day1.INPUT_FILE)

list1.sort()
list2.sort()

print(calcSimilarityScore(list1, list2))

# The answer is 21306195