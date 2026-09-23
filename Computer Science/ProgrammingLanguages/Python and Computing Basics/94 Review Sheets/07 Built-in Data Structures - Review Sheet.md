# 7.16 Common misconceptions consolidated

1. **“Lists are linked lists because they are called lists.”** CPython lists are dynamic arrays of object references.
2. **“Tuple means recursively immutable.”** Only the tuple’s reference sequence cannot change; referred objects may be mutable.
3. **“Dictionary keys are found by hash alone.”** Hash selects candidates; equality distinguishes colliding keys.
4. **“A set has whatever order it displayed once.”** Sets publish no semantic iteration order.
5. **“Copying a container copies all its elements.”** Ordinary `.copy()` and slicing are shallow.
6. **“Big-O tells exact speed.”** It describes growth under a model, omitting constants and operation-specific costs.
7. **“Expected (O(1)) means worst-case constant.”** Hash structures can have linear worst cases.
8. **“An immutable structure is automatically hashable.”** Every component participating in equality and hashing must satisfy the hash contract.
9. **“A dictionary view is a list snapshot.”** Views reflect the live mapping.
10. **“One built-in operation’s apparent atomicity protects a multi-step invariant.”** Compound transitions require an owning synchronisation or transactional boundary.
11. **“Dictionary insertion order means keys are sorted.”** Insertion order records key-insertion history; it applies no comparison-based ordering.
12. **“Reassigning a dictionary key moves it to the end.”** Replacing an existing value retains the key’s position. Delete and reinsert to establish a new insertion position, only when that is the intended semantics.
13. **“A hash uniquely identifies a key.”** Many unequal keys may share a hash. Equality resolves candidates under the hash-table algorithm.
14. **“Hashability means an object can never mutate.”** Hashability requires stable hash/equality behaviour while stored; unrelated internal state can in principle mutate, though such designs demand care.
15. **“An immutable outer object freezes everything reachable.”** Tuple and frozenset immutability controls their own membership, not arbitrary state inside referenced hashable objects.
16. **“Converting to a set only removes duplicate occurrences.”** It also removes ordering and retains representatives according to equality/hash equivalence, potentially collapsing values of different types.
17. **“A set’s arbitrary pop is random sampling.”** Arbitrary means no caller-visible selection guarantee, not a documented probability distribution.
18. **“Subset operators sort sets.”** Inclusion is a partial order. Two sets may be incomparable, so <code>&lt;</code> does not mean lexicographic precedence.
19. **“Set algebra permits arbitrary reordering of Python expressions.”** Mathematical membership laws do not erase operand evaluation effects, allocation, or representation-type differences.
20. **“Frozenset always represents an undirected edge.”** It enforces unordered uniqueness but not cardinality two, distinct endpoints, valid node types, or graph membership.
21. **“One code point is one visible character.”** Grapheme clusters and display cells are separate units.
22. **“String length is encoded byte length.”** <code>len(str)</code> counts code points; encoded bytes depend on the codec and content.
23. **“Raw strings contain raw or unprocessed data.”** Raw notation changes source-level escape handling; the runtime object is an ordinary string.
24. **“String strip removes a prefix or suffix.”** Its argument is a collection of boundary characters. Use <code>removeprefix</code> or <code>removesuffix</code> for exact affixes.
25. **“Split has one obvious meaning.”** Whitespace splitting and explicit-separator splitting have distinct empty-field and delimiter contracts.
26. **“Lowercasing is universal caseless comparison.”** Case folding, normalization, locale, script, and protocol policies remain distinct.
27. **“Unicode normalization is harmless cleanup.”** Compatibility normalization can erase distinctions; even canonical normalization changes code-point representation and must be applied consistently.
28. **“A numeric Unicode predicate proves integer parsing will succeed.”** Classification predicates and parser grammars are not identical.
29. **“Text equality is a safe secret comparison.”** Ordinary equality is not a constant-time cryptographic comparison primitive.
30. **“Repeated string concatenation is guaranteed linear because CPython optimizes it.”** Selected implementation optimisations are not the portable semantic cost model; join gives a robust output-linear construction pattern.
31. **“Every sequence is a list-like mutable array.”** Range is arithmetic, strings and tuples are immutable, bytes index to integers, and deque favours endpoints.
32. **“A deque is a faster list.”** It improves endpoint operations but gives up list strengths such as efficient arbitrary indexing and slicing.
33. **“A bounded deque can always manage window eviction automatically.”** Coordinated indexes often need the evicted item, requiring explicit eviction logic.
34. **“Materialising an iterator is merely a performance choice.”** It changes finiteness requirements, error timing, effects, memory, latency, and snapshot semantics.
35. **“Sorting heterogeneous values should just work somehow.”** Without a meaningful common ordering, automatic cross-type order would be arbitrary; derive a domain key.
36. **“The key function is called on every comparison.”** Python’s sorting API computes one key per element in an ordinary sort, then compares stored keys.
37. **“Reverse after ascending sort is the same as stable reverse sorting.”** Reversing the result also reverses equal-key groups; <code>reverse=True</code> preserves their relative order.
38. **“NaNs sort like very large or very small numbers.”** Ordinary NaN comparisons are unordered. Placement needs an explicit compound key.
39. **“Binary search makes list insertion logarithmic.”** It finds the position logarithmically, but shifting a list suffix remains linear.
40. **“Deep copy always creates the independent value wanted.”** Copy hooks, external resources, identity-sensitive entities, and domain ownership can make deep copying inappropriate or incomplete.
41. **“A list of lists is automatically a matrix.”** It may be ragged, aliased, empty without column metadata, or contain invalid element types.
42. **“Defaultdict reads never mutate.”** Missing-key subscription invokes the factory and inserts a value; <code>get</code> ordinarily does not.
43. **“Denormalized indexes are harmless caches.”** They duplicate facts and require coordinated maintenance, rebuild, or transactional semantics.
44. **“sys.getsizeof gives total memory.”** It normally reports shallow implementation-defined size and omits the general reachable graph.
45. **“Garbage collection knows when data is no longer useful.”** It knows reachability, not application utility. Unneeded but reachable caches, tracebacks, and frames remain live.
46. **“A falling object count must lower process RSS immediately.”** Allocators may retain freed storage, native memory may dominate, and operating-system measurements answer different questions.
47. **“Immutable records make a whole shared system thread-safe.”** Publication, cross-record invariants, indexes, external resources, and ordering still need a concurrency model.
48. **“A RuntimeError during dictionary iteration rolled back the mutation.”** Detection may occur after a structural change; it is not a transaction.
49. **“A lock belongs to one variable.”** Locks protect semantic invariants, often spanning several containers and operations.
50. **“Passing a dictionary to another process shares it.”** Ordinary process transfer serialises/copies state; explicit shared facilities have different semantics and costs.
51. **“Type annotations enforce every nested invariant at runtime.”** They neither automatically validate runtime values nor express most cross-element domain relationships.
52. **“If all operations are expected O(1), the composite update is O(1).”** Per-record tags, callbacks, allocation, resizing, eviction work, and output size can make the transition scale with additional dimensions.
