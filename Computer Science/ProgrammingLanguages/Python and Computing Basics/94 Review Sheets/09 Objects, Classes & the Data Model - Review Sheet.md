# 9.21 Common misconceptions consolidated

The following false statements are plausible because each compresses several mechanisms into a familiar metaphor. The correction after each statement should be read as a compact diagnostic rule.

### 9.21.1 Classes, instances, identity, and construction

1. **“A class is a blueprint but not an object.”** A Python class is an object, ordinarily an instance of <code>type</code>, with identity, attributes, bases, an MRO, and callable construction behaviour.
2. **“Every object is an instance of <code>object</code> in exactly the same sense.”** Ordinary classes derive from <code>object</code>, while instance relationships can also be customised or virtual. Ask which runtime relation and protocol are relevant.
3. **“The class statement merely declares a shape.”** Its body executes immediately in a prepared namespace and can compute, fail, or cause effects.
4. **“Class body code runs for every instance.”** It runs during class creation; ordinary per-instance initialisation occurs through <code>__new__</code> and <code>__init__</code> when the class is called.
5. **“<code>__init__</code> creates the object.”** <code>__new__</code> produces it. <code>__init__</code> receives an already created instance and must return <code>None</code>.
6. **“Every call to a class yields a fresh instance of that class.”** A metaclass can customise calls, and <code>__new__</code> can return cached or different objects. Such behaviour requires an explicit identity contract.
7. **“If <code>__new__</code> succeeds, <code>__init__</code> always runs.”** An unusual return outside the required instance relation can skip the expected initialiser; an exception also terminates construction.
8. **“Constructor arguments belong only to <code>__init__</code>.”** Ordinary class calling can pass them through metaclass <code>__call__</code> to both <code>__new__</code> and <code>__init__</code>.
9. **“An object’s class is permanently described by the variable annotation holding it.”** An annotation informs tools; runtime dispatch follows the actual object and <code>type</code> relationships.
10. **“Equal objects are the same object.”** Equality is a programmable value relation; identity means one object and is tested with <code>is</code>.
11. **“A frozen object is deeply immutable.”** Preventing field rebinding does not freeze mutable objects reachable through its fields.
12. **“Private attributes are enforced by double underscores.”** Name mangling reduces accidental subclass collision; determined code can still reach the mangled binding.

### 9.21.2 Attributes, methods, and descriptors

13. **“Attributes reside inside an object as one flat table.”** Lookup can combine data descriptors, instance dictionaries, non-data descriptors, class namespaces, base-class MROs, and fallback hooks.
14. **“Class attributes are copied into each new instance.”** Instances normally find the shared class binding through lookup until an allowed instance binding shadows it.
15. **“Changing a mutable class attribute changes the class but not existing instances.”** Instances finding that same object observe its mutation unless they shadow the name or another protocol intervenes.
16. **“Assignment to <code>obj.name</code> always writes <code>obj.__dict__</code>.”** A data descriptor, slot, or custom <code>__setattr__</code> can mediate or reject assignment.
17. **“An entry in <code>obj.__dict__</code> always wins.”** A data descriptor with the same name has higher retrieval precedence.
18. **“A method is copied and given <code>self</code> when the instance is made.”** A class-owned function is a descriptor; access through an instance creates a bound-method object as needed.
19. **“<code>self</code> is a reserved word.”** It is a strong convention for the first instance-method parameter; binding depends on descriptors, not spelling.
20. **“A static method is faster because it is static.”** <code>staticmethod</code> changes binding semantics, not an optimisation guarantee.
21. **“A class method is run only once per class.”** It is an ordinarily callable method whose first bound argument is the dynamic class.
22. **“A property is a method with omitted parentheses.”** It is a descriptor participating in attribute lookup. Attribute syntax should still have a defensible access-cost and side-effect contract.
23. **“A property without a setter is non-data.”** Property objects implement data-descriptor behaviour even when assignment is rejected, so an instance entry cannot ordinarily shadow retrieval.
24. **“A descriptor contains every instance’s value in its own simple field.”** The descriptor is shared; values may be stored in each instance, slots, weak mappings, external systems, or computed dynamically.
25. **“<code>__set_name__</code> runs whenever a descriptor is assigned to a class.”** Ordinary type construction invokes it for objects in the original class namespace. Later attachment needs explicit handling.
26. **“<code>__getattr__</code> intercepts all reads.”** It is a fallback for missing attributes; <code>__getattribute__</code> participates in all ordinary reads.
27. **“<code>hasattr</code> safely inspects without executing behaviour.”** It performs retrieval, can invoke arbitrary user code, and interprets <code>AttributeError</code> as absence.

### 9.21.3 Encapsulation, inheritance, and polymorphism

28. **“Encapsulation means no external code can mutate state.”** In Python it primarily assigns responsibility and exposes a controlled cooperative interface; it is not a hostile-code sandbox.
29. **“A leading underscore makes an attribute inaccessible.”** It communicates non-public API intent by convention.
30. **“Getters and setters automatically improve encapsulation.”** Accessors that merely mirror public storage add ceremony; a boundary is useful when it owns an invariant, abstraction, or change policy.
31. **“Inheritance is the normal mechanism for code reuse.”** Inheritance asserts a type/substitutability relation. Composition, delegation, or a function can reuse behaviour without that claim.
32. **“If <code>isinstance(child, Base)</code> is true, substitution is proven.”** The runtime nominal relation does not prove preservation of preconditions, postconditions, invariants, exceptions, or history constraints.
33. **“A subtype may reject more inputs because it is more specialised.”** Strengthening a base method’s preconditions breaks callers entitled to use the base contract.
34. **“A subtype may return less information if its implementation is simpler.”** Weakening promised postconditions breaks substitutability.
35. **“Overriding a method means copying and replacing it everywhere.”** The subclass binds another attribute; MRO lookup selects it for suitable receivers while the base implementation continues to exist.
36. **“Calling a base method directly and using <code>super</code> are equivalent.”** A named base freezes one route; <code>super</code> continues after a definition site in the receiver’s MRO.
37. **“<code>super()</code> calls the immediate parent.”** In a multiple-inheritance MRO it can call a sibling relative to the defining class.
38. **“Python searches one parent tree completely, then the next.”** C3 constructs one monotonic linearisation that keeps shared ancestors after their subclasses.
39. **“A legal MRO proves the bases work together.”** It proves consistent precedence only, not compatible signatures, state ownership, or behavioural laws.
40. **“One call to <code>super</code> guarantees every base runs.”** Every intervening implementation must continue the cooperative chain exactly as its contract requires.
41. **“A mixin is any small base class.”** A disciplined mixin contributes a narrow capability under explicit host and cooperation requirements; size alone is irrelevant.
42. **“Composition eliminates coupling.”** It makes collaborators and ownership explicit, but their interfaces and lifecycle still create intentional coupling.
43. **“Duck typing means there is no interface.”** Structural use still depends on operations and behavioural laws; only nominal declaration is unnecessary.

### 9.21.4 Special methods and operator protocols

44. **“Dunder methods are ordinary methods with funny names.”** They are ordinary attributes syntactically, but language syntax often looks them up specially on types and imposes result/fallback rules.
45. **“Calling <code>obj.__len__()</code> is always equivalent to <code>len(obj)</code>.”** The built-in owns special lookup, type checks, and error semantics; direct calling can observe different shadowing or invalid results.
46. **“Any integer from <code>__len__</code> is accepted.”** Length must satisfy the protocol’s non-negative integer and platform-size constraints.
47. **“Truth testing only calls <code>__bool__</code>.”** If absent, Python can use <code>__len__</code>; if both are absent, ordinary objects are truthy.
48. **“An iterable and iterator are synonyms.”** An iterable produces an iterator; an iterator is the stateful object whose <code>__next__</code> advances and exhausts.
49. **“Returning <code>NotImplemented</code> reports an unfinished method to the caller.”** It asks a cooperative operator protocol to try another route.
50. **“<code>NotImplementedError</code> and <code>NotImplemented</code> are interchangeable.”** One is an exception terminating the current call; the other is a sentinel value used by selected dispatch protocols.
51. **“The left operand always receives first operator dispatch.”** A strict right-hand subtype with a distinct reflected method can receive priority.
52. **“A reflected subtraction method computes receiver minus argument.”** It implements the original expression order: in <code>right.__rsub__(left)</code>, compute <code>left - right</code>.
53. **“<code>+=</code> necessarily mutates.”** It tries an in-place method and may otherwise compute an ordinary result and rebind the left target.
54. **“If augmented assignment raises, nothing changed.”** An inner mutable object can be changed before a later target rebinding fails; compound syntax is not transactional.
55. **“Implementing <code>__eq__</code> automatically gives a valid hash.”** Mutable or value-equal objects need an explicit hash policy; equal hashable objects must have equal hashes.
56. **“Operator syntax decides the mathematics.”** A type must choose meanings, coercions, closure, result types, and algebraic laws; syntax supplies dispatch only.
57. **“Returning a plausible result is enough.”** Special protocols include error, aliasing, resource, algebraic, and interoperability contracts as well as result shape.

### 9.21.5 Slots, metaclasses, and class lifecycle

58. **“Slots declare statically typed fields.”** They request named runtime storage descriptors; they do not constrain value types without additional policy.
59. **“Slots make instances immutable.”** Slot values can ordinarily be reassigned, and referenced objects can mutate.
60. **“Slots make attributes private.”** They constrain ordinary storage names, not access authority.
61. **“A slotted base forces all subclasses to have no dictionary.”** A subclass without its own slot declaration ordinarily gains a dictionary.
62. **“Slots always save a known number of bytes.”** Savings vary with interpreter, layout, key sharing, population, inheritance, and measurement boundary.
63. **“Shallow <code>getsizeof</code> compares complete object memory.”** Separately allocated dictionaries and referenced graphs may be excluded.
64. **“Every class has metaclass <code>type</code> exactly.”** Custom metaclasses are subclasses of <code>type</code>; <code>type(C)</code> may be such a subclass.
65. **“A metaclass is needed whenever classes are created dynamically.”** The three-argument <code>type</code>, factory functions, decorators, and ordinary closures cover many dynamic cases.
66. **“Metaclass <code>__new__</code> constructs ordinary instances.”** It constructs class objects; metaclass <code>__call__</code> later participates when those class objects construct instances.
67. **“<code>__prepare__</code> receives an already completed class.”** It supplies the namespace before the class body executes.
68. **“A metaclass conflict is only a syntax issue.”** It signals incompatible class-governance inheritance; a combined metaclass must reconcile policies, not merely types.
69. **“<code>__init_subclass__</code> runs on each instance.”** It runs on the newly created subclass during class creation.
70. **“A class decorator runs before the metaclass.”** It receives the object after metaclass construction and subclass hooks, then its return is bound.
71. **“Class decorators are inherited automatically.”** Their transformed attributes may be inherited, but the decorator call applies only to the annotated class statement.
72. **“Metaprogramming removes boilerplate for free.”** It moves work into implicit lifecycle machinery, increasing requirements for ordering, diagnostics, typing, introspection, failure recovery, and tests.
