# Contents

Contents
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4 How to read this handbook
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5 Which algorithm should I use?
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7 From scratch to production
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9 Complexity cheat sheets
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11 1. Searching
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11 linear_search
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12 binary_search
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13 lower_bound
. . . . . . . . . . . . . . . . . . . . . . . . . . . 14 binary_search_on_answer
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 2. Sorting
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 bubble_sort
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16 selection_sort
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17 insertion_sort
. . . . . . . . . . . . . . . . . . . . . . . . . . . 18 merge_two_sorted_lists
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19 merge_sort
. . . . . . . . . . . . . . . . . . . . . . . . . . . 19 _partition_around_pivot
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20 _quick_sort_range
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20 quick_sort
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 21 _sift_down_max_heap
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21 heap_sort
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22 counting_sort
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23 radix_sort
. . . . . . . . . . . . . . . . . . . . . . . . . . 24 quickselect_kth_smallest
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25 3. Data structures the algorithms rely on
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25 MinHeap
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27 UnionFind
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29 Trie
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30 TreeNode
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31 bst_insert
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32 bst_search
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32 traverse_in_order
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 33 traverse_pre_order
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 33 traverse_post_order
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 34 traverse_level_order
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35 tree_height
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 35 is_balanced_brackets
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36 4. Graphs
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 36 breadth_first_search
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37 reconstruct_path
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 38 depth_first_search
. . . . . . . . . . . . . . . . . . . . . . . . . 39 depth_first_search_iterative
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 40 connected_components
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41 topological_sort
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42 dijkstra
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44 bellman_ford
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46 floyd_warshall
. . . . . . . . . . . . . . . . . . . . . . . . . 47 kruskal_minimum_spanning_tree
. . . . . . . . . . . . . . . . . . . . . . . . . . 48 prim_minimum_spanning_tree
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49 a_star_search
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50 5. Dynamic programming
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 50 fibonacci_memoised
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 51 fibonacci_bottom_up
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52 knapsack_01
. . . . . . . . . . . . . . . . . . . . . . . . . . 53 longest_common_subsequence
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54 edit_distance
. . . . . . . . . . . . . . . . . . . . . . 55 longest_increasing_subsequence_length
. . . . . . . . . . . . . . . . . . . . . . . . . . 56 minimum_coins_for_amount
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 57 maximum_subarray_sum
CS Algorithms Toolkit
2
