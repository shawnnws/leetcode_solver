from openai import Completion
import openai
import os

from openai.openai_object import OpenAIObject

openai_key: str = os.getenv("SHAWN_OPENAI_KEY", "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")
openai.api_key = openai_key


def get_leetcode_answer(leetcode_question: str) -> str:
    completion_object: Completion = Completion()
    leetcode_solution: OpenAIObject = completion_object.create(
        model="code-davinci-002",
        prompt=f"""
Please provide the best time and space complexity Python Code Solution for the Leetcode Question below. Explain the solution with comment

===
Leetcode Question:
1. Two Sum
Easy

37318

1186

Add to List

Share
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
---
Python Code Solution:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums_with_index: List[Tuple[int, int]] = sorted(enumerate(nums), key=lambda index_num_tuple: index_num_tuple[1])
        
        left: int = 0
        right: int = len(sorted_nums_with_index) - 1
            
        while sorted_nums_with_index[left][1] + sorted_nums_with_index[right][1] != target:
            if sorted_nums_with_index[left][1] + sorted_nums_with_index[right][1] < target:
                left += 1
            else:
                right -= 1
        
        return [sorted_nums_with_index[left][0], sorted_nums_with_index[right][0]]

===
Leetcode Question:
{leetcode_question}
---
Python Code Solution:

""",
        max_tokens=1000,
        temperature=0,
    )
    solution_text: str = leetcode_solution["choices"][0]["text"]
    return solution_text


if __name__ == "__main__":
    print(get_leetcode_answer(
        leetcode_question="""
    2. Add Two Numbers
    Medium

    21252

    4184

    Add to List

    Share
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.



    Example 1:


    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.
    Example 2:

    Input: l1 = [0], l2 = [0]
    Output: [0]
    Example 3:

    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]


    Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.
    """
    ))