"""
LeetCode Problem 40: Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.
The solution set must not contain duplicate combinations.

Example:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
"""

from typing import List


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    """
    Find all unique combinations that sum to target.
    
    Approach: Backtracking with sorting and duplicate handling
    Time Complexity: O(2^n)
    Space Complexity: O(n) for recursion stack
    """
    result = []
    candidates.sort()  # Sort to handle duplicates easily
    
    def backtrack(start: int, current_combination: List[int], remaining: int):
        """
        Backtracking helper function.
        
        Args:
            start: Starting index for next iteration
            current_combination: Current combination being built
            remaining: Remaining sum needed
        """
        # Base case: if remaining sum is 0, we found a valid combination
        if remaining == 0:
            result.append(current_combination[:])  # Add a copy
            return
        
        # If remaining is negative, stop exploring this path
        if remaining < 0:
            return
        
        # Explore candidates
        for i in range(start, len(candidates)):
            # Skip duplicates: if current candidate equals previous one
            # and we didn't use the previous one, skip this one
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            
            # Skip if candidate is greater than remaining sum
            if candidates[i] > remaining:
                break  # No point checking further (array is sorted)
            
            # Choose: add candidate to combination
            current_combination.append(candidates[i])
            
            # Explore: recurse with updated parameters
            backtrack(i + 1, current_combination, remaining - candidates[i])
            
            # Unchoose: backtrack
            current_combination.pop()
    
    backtrack(0, [], target)
    return result


# Test cases
if __name__ == "__main__":
    # Test case 1
    candidates1 = [10, 1, 2, 7, 6, 1, 5]
    target1 = 8
    print(f"Input: candidates = {candidates1}, target = {target1}")
    print(f"Output: {combinationSum2(candidates1, target1)}")
    print()
    
    # Test case 2
    candidates2 = [2, 5, 2, 1, 2]
    target2 = 5
    print(f"Input: candidates = {candidates2}, target = {target2}")
    print(f"Output: {combinationSum2(candidates2, target2)}")
    print()
    
    # Test case 3
    candidates3 = [1]
    target3 = 1
    print(f"Input: candidates = {candidates3}, target = {target3}")
    print(f"Output: {combinationSum2(candidates3, target3)}")

