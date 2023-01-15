# Explanation 4

## Rationale
For the Active Directory exercise, I used recursion to search groups and thier nested groups for members. If a match is found we short circuit immediately and return to the caller.

## Runtime Analysis
`is_user_in_group` has a time complexity of `O(n)` and a space complexity of `O(n)`. In the worse case, where the user is not a member of the provided group or its children thus requiring an exhaustive search, the runtime scales linearly with group depth and member list size (n). The memory footprint scales linearly as well, specifically with group recursion depth (n).