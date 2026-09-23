# 13.23 References and further study

The references distinguish normative Python documentation, implementation material, foundational papers, and synthetic textbooks. Language guarantees should be checked against the documentation for the targeted Python release; implementation claims should be checked against the named interpreter and version.

### 13.23.1 Python specifications and implementation sources

1. Python Software Foundation. [*Python 3.12 Language Reference: Data Model*](https://docs.python.org/3.12/reference/datamodel.html). Equality, hashing, comparison, iteration, and object protocol rules.
2. Python Software Foundation. [*Python 3.12 Library Reference: Built-in Types*](https://docs.python.org/3.12/library/stdtypes.html). Sequence and mapping contracts, including list mutation.
3. Python Software Foundation. [*Sorting HOW TO, Python 3.12*](https://docs.python.org/3.12/howto/sorting.html). Stability, key functions, decorate–sort–undecorate, comparison functions, and implementation context.
4. Python Software Foundation. [*bisect — Array Bisection Algorithm, Python 3.12*](https://docs.python.org/3.12/library/bisect.html). Partition semantics, key handling, performance notes, and thread-safety boundary.
5. Python Software Foundation. [*heapq — Heap Queue Algorithm, Python 3.12*](https://docs.python.org/3.12/library/heapq.html). Heap invariant, priority-queue patterns, and merging.
6. Python Software Foundation. [*collections — Container Datatypes, Python 3.12*](https://docs.python.org/3.12/library/collections.html#collections.deque). Deque interface and endpoint complexity guidance.
7. Python Software Foundation. [*graphlib — Functionality to Operate with Graph-like Structures, Python 3.12*](https://docs.python.org/3.12/library/graphlib.html). Predecessor-oriented topological scheduling interface.
8. Python Software Foundation. [*functools — Higher-order Functions and Operations on Callable Objects, Python 3.12*](https://docs.python.org/3.12/library/functools.html). Caching and comparator adaptation.
9. Python Software Foundation. [*timeit — Measure Execution Time of Small Code Snippets, Python 3.12*](https://docs.python.org/3.12/library/timeit.html). Repetition, setup, and garbage-collection measurement policy.
10. Python Software Foundation. [*time — Time Access and Conversions, Python 3.12*](https://docs.python.org/3.12/library/time.html#time.perf_counter). Performance-counter contract and clock metadata.
11. Python Software Foundation. [*tracemalloc — Trace Memory Allocations, Python 3.12*](https://docs.python.org/3.12/library/tracemalloc.html). Snapshot and traced-peak semantics.
12. Python Software Foundation. [*dataclasses — Data Classes, Python 3.12*](https://docs.python.org/3.12/library/dataclasses.html). Generated equality, ordering, frozen instances, and hashing rules.
13. Peters, T. [*listsort.txt, CPython 3.12 source tree*](https://github.com/python/cpython/blob/3.12/Objects/listsort.txt). Engineering account of CPython’s adaptive stable merge sort. Implementation source, not language specification.
14. Python Software Foundation. [*dictobject.c, CPython 3.12 source tree*](https://github.com/python/cpython/blob/3.12/Objects/dictobject.c). CPython dictionary implementation and internal invariants.
15. Aumasson, J.-P. and Bernstein, D. J. [*PEP 456 — Secure and Interchangeable Hash Algorithm*](https://peps.python.org/pep-0456/). Hash-flooding threat model and CPython hash selection.

### 13.23.2 General algorithm analysis and data structures

16. Cormen, T. H., Leiserson, C. E., Rivest, R. L. and Stein, C. *Introduction to Algorithms*, 4th ed. MIT Press, 2022.
17. Knuth, D. E. *The Art of Computer Programming, Volume 1: Fundamental Algorithms*, 3rd ed. Addison-Wesley, 1997.
18. Knuth, D. E. *The Art of Computer Programming, Volume 3: Sorting and Searching*, 2nd ed. Addison-Wesley, 1998.
19. Aho, A. V., Hopcroft, J. E. and Ullman, J. D. *The Design and Analysis of Computer Algorithms*. Addison-Wesley, 1974.
20. Kleinberg, J. and Tardos, É. *Algorithm Design*. Pearson, 2006.
21. Dasgupta, S., Papadimitriou, C. H. and Vazirani, U. V. *Algorithms*. McGraw-Hill, 2008.
22. Sedgewick, R. and Wayne, K. *Algorithms*, 4th ed. Addison-Wesley, 2011.
23. Skiena, S. S. *The Algorithm Design Manual*, 3rd ed. Springer, 2020.
24. Mehlhorn, K. and Sanders, P. *Algorithms and Data Structures: The Basic Toolbox*. Springer, 2008.
25. Erickson, J. [*Algorithms*](https://jeffe.cs.illinois.edu/teaching/algorithms/). Open textbook, 2019.
26. Graham, R. L., Knuth, D. E. and Patashnik, O. *Concrete Mathematics*, 2nd ed. Addison-Wesley, 1994.
27. Flajolet, P. and Sedgewick, R. *Analytic Combinatorics*. Cambridge University Press, 2009.
28. Knuth, D. E. “Big Omicron and Big Omega and Big Theta.” *SIGACT News* 8(2), 18–24, 1976. [doi:10.1145/1008328.1008329](https://doi.org/10.1145/1008328.1008329).
29. Tarjan, R. E. “Amortized Computational Complexity.” *SIAM Journal on Algebraic and Discrete Methods* 6(2), 306–318, 1985. [doi:10.1137/0606031](https://doi.org/10.1137/0606031).
30. Sleator, D. D. and Tarjan, R. E. “Self-Adjusting Binary Search Trees.” *Journal of the ACM* 32(3), 652–686, 1985. [doi:10.1145/3828.3835](https://doi.org/10.1145/3828.3835).
31. Akra, M. and Bazzi, L. “On the Solution of Linear Recurrence Equations.” *Computational Optimization and Applications* 10, 195–210, 1998. [doi:10.1023/A:1018373005182](https://doi.org/10.1023/A:1018373005182).
32. Okasaki, C. *Purely Functional Data Structures*. Cambridge University Press, 1998.

### 13.23.3 Sorting, selection, and hashing

33. Hoare, C. A. R. “Quicksort.” *The Computer Journal* 5(1), 10–16, 1962. [doi:10.1093/comjnl/5.1.10](https://doi.org/10.1093/comjnl/5.1.10).
34. Williams, J. W. J. “Algorithm 232: Heapsort.” *Communications of the ACM* 7(6), 347–348, 1964. [doi:10.1145/512274.512284](https://doi.org/10.1145/512274.512284).
35. Floyd, R. W. “Algorithm 245: Treesort 3.” *Communications of the ACM* 7(12), 701, 1964. [doi:10.1145/355588.365103](https://doi.org/10.1145/355588.365103).
36. Blum, M., Floyd, R. W., Pratt, V., Rivest, R. L. and Tarjan, R. E. “Time Bounds for Selection.” *Journal of Computer and System Sciences* 7(4), 448–461, 1973. [doi:10.1016/S0022-0000(73)80033-9](https://doi.org/10.1016/S0022-0000(73)80033-9).
37. Floyd, R. W. and Rivest, R. L. “Expected Time Bounds for Selection.” *Communications of the ACM* 18(3), 165–172, 1975. [doi:10.1145/360680.360691](https://doi.org/10.1145/360680.360691).
38. McIlroy, P. M. “Optimistic Sorting and Information Theoretic Complexity.” *Proceedings of the Fourth Annual ACM-SIAM Symposium on Discrete Algorithms*, 467–474, 1993.
39. Carter, J. L. and Wegman, M. N. “Universal Classes of Hash Functions.” *Journal of Computer and System Sciences* 18(2), 143–154, 1979. [doi:10.1016/0022-0000(79)90044-8](https://doi.org/10.1016/0022-0000(79)90044-8).
40. Fredman, M. L., Komlós, J. and Szemerédi, E. “Storing a Sparse Table with \(O(1)\) Worst Case Access Time.” *Journal of the ACM* 31(3), 538–544, 1984. [doi:10.1145/828.1884](https://doi.org/10.1145/828.1884).
41. Pagh, R. and Rodler, F. F. “Cuckoo Hashing.” *Journal of Algorithms* 51(2), 122–144, 2004. [doi:10.1016/j.jalgor.2003.12.002](https://doi.org/10.1016/j.jalgor.2003.12.002).
42. Bloom, B. H. “Space/Time Trade-offs in Hash Coding with Allowable Errors.” *Communications of the ACM* 13(7), 422–426, 1970. [doi:10.1145/362686.362692](https://doi.org/10.1145/362686.362692).

### 13.23.4 Trees and disjoint sets

43. Adelson-Velsky, G. M. and Landis, E. M. “An Algorithm for the Organization of Information.” *Soviet Mathematics Doklady* 3, 1259–1263, 1962.
44. Bayer, R. and McCreight, E. “Organization and Maintenance of Large Ordered Indexes.” *Acta Informatica* 1, 173–189, 1972. [doi:10.1007/BF00288683](https://doi.org/10.1007/BF00288683).
45. Guibas, L. J. and Sedgewick, R. “A Dichromatic Framework for Balanced Trees.” *19th Annual Symposium on Foundations of Computer Science*, 8–21, 1978. [doi:10.1109/SFCS.1978.3](https://doi.org/10.1109/SFCS.1978.3).
46. Pugh, W. “Skip Lists: A Probabilistic Alternative to Balanced Trees.” *Communications of the ACM* 33(6), 668–676, 1990. [doi:10.1145/78973.78977](https://doi.org/10.1145/78973.78977).
47. Tarjan, R. E. “Efficiency of a Good But Not Linear Set Union Algorithm.” *Journal of the ACM* 22(2), 215–225, 1975. [doi:10.1145/321879.321884](https://doi.org/10.1145/321879.321884).
48. Sleator, D. D. and Tarjan, R. E. “A Data Structure for Dynamic Trees.” *Journal of Computer and System Sciences* 26(3), 362–391, 1983. [doi:10.1016/0022-0000(83)90006-5](https://doi.org/10.1016/0022-0000(83)90006-5).

### 13.23.5 Graph algorithms

49. Dijkstra, E. W. “A Note on Two Problems in Connexion with Graphs.” *Numerische Mathematik* 1, 269–271, 1959. [doi:10.1007/BF01386390](https://doi.org/10.1007/BF01386390).
50. Moore, E. F. “The Shortest Path Through a Maze.” In *Proceedings of an International Symposium on the Theory of Switching*, 285–292. Harvard University Press, 1959.
51. Kahn, A. B. “Topological Sorting of Large Networks.” *Communications of the ACM* 5(11), 558–562, 1962. [doi:10.1145/368996.369025](https://doi.org/10.1145/368996.369025).
52. Tarjan, R. “Depth-First Search and Linear Graph Algorithms.” *SIAM Journal on Computing* 1(2), 146–160, 1972. [doi:10.1137/0201010](https://doi.org/10.1137/0201010).
53. Sharir, M. “A Strong-Connectivity Algorithm and Its Applications in Data Flow Analysis.” *Computers & Mathematics with Applications* 7(1), 67–72, 1981. [doi:10.1016/0898-1221(81)90008-0](https://doi.org/10.1016/0898-1221(81)90008-0).
54. Bellman, R. “On a Routing Problem.” *Quarterly of Applied Mathematics* 16(1), 87–90, 1958. [doi:10.1090/qam/102435](https://doi.org/10.1090/qam/102435).
55. Ford, L. R., Jr. “Network Flow Theory.” RAND Corporation Paper P-923, 1956.
56. Floyd, R. W. “Algorithm 97: Shortest Path.” *Communications of the ACM* 5(6), 345, 1962. [doi:10.1145/367766.368168](https://doi.org/10.1145/367766.368168).
57. Warshall, S. “A Theorem on Boolean Matrices.” *Journal of the ACM* 9(1), 11–12, 1962. [doi:10.1145/321105.321107](https://doi.org/10.1145/321105.321107).
58. Hart, P. E., Nilsson, N. J. and Raphael, B. “A Formal Basis for the Heuristic Determination of Minimum Cost Paths.” *IEEE Transactions on Systems Science and Cybernetics* 4(2), 100–107, 1968. [doi:10.1109/TSSC.1968.300136](https://doi.org/10.1109/TSSC.1968.300136).
59. Kruskal, J. B. “On the Shortest Spanning Subtree of a Graph and the Traveling Salesman Problem.” *Proceedings of the American Mathematical Society* 7(1), 48–50, 1956. [doi:10.1090/S0002-9939-1956-0078686-7](https://doi.org/10.1090/S0002-9939-1956-0078686-7).
60. Prim, R. C. “Shortest Connection Networks and Some Generalizations.” *Bell System Technical Journal* 36(6), 1389–1401, 1957. [doi:10.1002/j.1538-7305.1957.tb01515.x](https://doi.org/10.1002/j.1538-7305.1957.tb01515.x).

### 13.23.6 Greedy methods, dynamic programming, and complexity

61. Huffman, D. A. “A Method for the Construction of Minimum-Redundancy Codes.” *Proceedings of the IRE* 40(9), 1098–1101, 1952. [doi:10.1109/JRPROC.1952.273898](https://doi.org/10.1109/JRPROC.1952.273898).
62. Bellman, R. *Dynamic Programming*. Princeton University Press, 1957.
63. Wagner, R. A. and Fischer, M. J. “The String-to-String Correction Problem.” *Journal of the ACM* 21(1), 168–173, 1974. [doi:10.1145/321796.321811](https://doi.org/10.1145/321796.321811).
64. Hirschberg, D. S. “A Linear Space Algorithm for Computing Maximal Common Subsequences.” *Communications of the ACM* 18(6), 341–343, 1975. [doi:10.1145/360825.360861](https://doi.org/10.1145/360825.360861).
65. Held, M. and Karp, R. M. “A Dynamic Programming Approach to Sequencing Problems.” *Journal of the Society for Industrial and Applied Mathematics* 10(1), 196–210, 1962. [doi:10.1137/0110015](https://doi.org/10.1137/0110015).
66. Edmonds, J. “Matroids and the Greedy Algorithm.” *Mathematical Programming* 1, 127–136, 1971. [doi:10.1007/BF01584082](https://doi.org/10.1007/BF01584082).
67. Cook, S. A. “The Complexity of Theorem-Proving Procedures.” *Proceedings of the Third Annual ACM Symposium on Theory of Computing*, 151–158, 1971. [doi:10.1145/800157.805047](https://doi.org/10.1145/800157.805047).
68. Karp, R. M. “Reducibility Among Combinatorial Problems.” In *Complexity of Computer Computations*, 85–103. Plenum Press, 1972. [doi:10.1007/978-1-4684-2001-2_9](https://doi.org/10.1007/978-1-4684-2001-2_9).
69. Garey, M. R. and Johnson, D. S. *Computers and Intractability: A Guide to the Theory of NP-Completeness*. W. H. Freeman, 1979.
70. Turing, A. M. “On Computable Numbers, with an Application to the Entscheidungsproblem.” *Proceedings of the London Mathematical Society* s2-42(1), 230–265, 1937. [doi:10.1112/plms/s2-42.1.230](https://doi.org/10.1112/plms/s2-42.1.230).
71. Motwani, R. and Raghavan, P. *Randomized Algorithms*. Cambridge University Press, 1995.
72. Mitzenmacher, M. and Upfal, E. *Probability and Computing*, 2nd ed. Cambridge University Press, 2017.
73. Knuth, D. E., Morris, J. H., Jr. and Pratt, V. R. “Fast Pattern Matching in Strings.” *SIAM Journal on Computing* 6(2), 323–350, 1977. [doi:10.1137/0206024](https://doi.org/10.1137/0206024).
74. Karp, R. M. and Rabin, M. O. “Efficient Randomized Pattern-Matching Algorithms.” *IBM Journal of Research and Development* 31(2), 249–260, 1987. [doi:10.1147/rd.312.0249](https://doi.org/10.1147/rd.312.0249).
75. Aho, A. V. and Corasick, M. J. “Efficient String Matching: An Aid to Bibliographic Search.” *Communications of the ACM* 18(6), 333–340, 1975. [doi:10.1145/360825.360855](https://doi.org/10.1145/360825.360855).

---
