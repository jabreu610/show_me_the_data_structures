# Explanation 2

## Rationale
For the Finding Files exercise, I leverage a simple Python list as a stacl for managing directory tree traversal via depth first search.  

## Runtime Analysis
The `find_files` funciton has a time complexity of O(n) and a space complexity of O(n). `find_files` traverses the directory tree seeking to compare the leaf nodes, files, to the provided query. This scales linearly with the number of subdirectories / files present in the input path. As for space, we leverage a stack to manage traversal. In the worst case we'd need to keep a reference to every subdirectory / file under the provided input path. 