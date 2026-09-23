# 9.22 Exercises

The problems are cumulative. “Predict” means write the outcome and justify it from namespaces and protocols before executing code. “Prove” means state assumptions, derive the claim, and supply tests as evidence; a few passing examples alone are not a proof of all inputs.

### 9.22.1 Objects, classes, and namespaces

1. For the expressions <code>type(3)</code>, <code>type(int)</code>, <code>isinstance(3, int)</code>, <code>isinstance(int, type)</code>, and <code>issubclass(bool, int)</code>, predict each result and draw the two distinct instance/inheritance relations involved.
2. Define a class containing one integer class attribute. Create two instances, assign the same attribute name on one instance, and draw all three namespaces before and after assignment.
3. Delete the shadowing instance attribute from Exercise 2. Predict what retrieval yields and explain why deletion appears to “restore” a value without copying anything.
4. Bind the same mutable list as a class attribute and mutate it through one instance. Account for every reference and observation through the other instance.
5. Repair Exercise 4 by constructing per-instance lists. Then deliberately share one list between two instances through constructor arguments and explain why the repair cannot prevent explicit aliasing.
6. Write a function that receives an arbitrary object and reports its dynamic type, class MRO when applicable, instance dictionary when present, and raw class namespace entry for a requested name without triggering descriptor access. State every case it cannot safely or completely inspect.
7. Show that assigning a new class attribute after instances exist changes lookup on those instances. Add an instance shadow and determine which objects observe each later class rebinding.
8. Create a class body containing a loop that generates three class attributes. Explain when the loop runs, where its loop variable remains bound, and why instance construction does not repeat it.
9. Demonstrate that a method body does not automatically close over a class-local constant. Repair the method using instance/class attribute lookup and separately using a module constant; compare override behaviour.
10. Use <code>vars</code> on an instance, its class, and the metaclass. Classify returned mappings by ownership and mutability; do not mutate a mapping proxy.
11. Construct two distinct class objects with the same <code>__name__</code>. Prove that names do not establish type identity, and analyse the resulting representations.
12. Integration with Chapters 5 and 8: represent the object/class/metaclass relationships as a graph of nodes and typed edges using only dictionaries and tuples, then write pure query functions for “instances of” and “subclasses of.” Explain how this model differs from Python’s programmable runtime checks.

### 9.22.2 Methods, binding, and receiver semantics

13. Retrieve the same method through a class and an instance. Inspect <code>__func__</code> and <code>__self__</code> where available and reconstruct the bound call by calling the raw function explicitly.
14. Store a bound method in a variable, delete the original instance name, and show whether the instance remains reachable. Explain the lifetime edge.
15. Assign a plain function to one instance under an existing method name. Predict whether automatic receiver binding occurs and explain the non-data-descriptor precedence responsible.
16. Assign a function to a class after class creation and invoke it through an instance. Compare this with Exercise 15.
17. Implement the same operation as an instance method, class method, static method, and module function. For each, state the receiver or dependency it can access implicitly and select the truthful design.
18. Inherit a class method factory and call it through a subclass. Verify the dynamic class constructed. Then replace <code>cls(...)</code> with a named base call and identify the extensibility defect.
19. Create a static method that does not conceptually belong to the class. Move it to a module-level function and assess discoverability, coupling, and substitution; justify one location.
20. Shadow a non-data function descriptor on one instance, then make a data descriptor with the same retrieval behaviour. Demonstrate why the latter cannot be shadowed by ordinary assignment.
21. Pass an unbound class function as a callback. Specify the signature the callback consumer must use and compare it with passing a bound method.
22. Store bound methods from one thousand short-lived instances in a list. Explain and measure why the instances remain alive until the list is cleared.
23. Build a callback wrapper using <code>weakref.WeakMethod</code>. Define what should happen when the receiving instance has been collected.
24. Integration with Chapter 8: write a decorator that preserves metadata and works on an instance method. Trace decoration time, descriptor binding time, wrapper call time, and the identities of <code>self</code> and the original function.

### 9.22.3 Encapsulation, invariants, and record types

25. Define a bank-account invariant in pence using integers. Implement deposit and withdrawal so rejected operations leave state unchanged. Test zero, negative, boundary, and excessive values.
26. Expose the account balance through a read-only property. Attempt ordinary assignment and direct dictionary insertion under the public name; explain each outcome from descriptor precedence.
27. Add transaction history to the account. Decide whether callers receive the mutable internal list, an immutable snapshot, or an iterator, and prove the invariant consequences of your choice.
28. Implement a temperature property that accepts numeric values but rejects non-finite floating-point values. Explain why a simple comparison against absolute zero is insufficient for NaN.
29. Refactor a class containing trivial getters and setters. Retain only boundaries owning validation or representation change and justify the resulting public API.
30. Create a frozen dataclass containing a list. Demonstrate shallow mutability, then redesign with a tuple and state whether elements themselves can still contain mutable graphs.
31. Compare a manually written value class with an equivalent dataclass. List every generated method and field option on which equality, ordering, hashing, representation, and matching depend.
32. Design a value type whose normalised representation is established in <code>__post_init__</code>. Use <code>object.__setattr__</code> under a frozen dataclass and prove idempotence of normalisation.
33. Create a class that exposes a defensive copy of mutable state. Measure the copying cost and propose an immutable view or query interface when state is large.
34. Define an invariant spanning two fields, such as <code>start <= end</code>. Show how separately writable property setters can make valid transitions impossible or pass through invalid intermediate states; replace them with an atomic update method.
35. Design <code>repr</code>, <code>str</code>, and exception messages for an object holding an authentication secret. Write capture tests across logging, container representation, failed validation, and debugging helpers to show where redaction is and is not guaranteed.
36. Integration with Chapter 7: expose a mapping-like read-only view over private state. Specify whether it is live or snapshot-based, its iteration order, equality meaning, and behaviour under concurrent internal mutation.

### 9.22.4 Construction, allocation, and lifecycle

37. Add event logging to <code>__new__</code> and <code>__init__</code>. Predict order, receiver classes, and argument flow for base and subclass construction.
38. Make <code>__init__</code> return an integer deliberately. Record the exception and explain why constructors return through class call machinery rather than the initialiser’s return value.
39. Write an immutable <code>str</code> subtype that strips surrounding whitespace and case-folds in <code>__new__</code>. Test construction, equality, hashing, representation, and repeated normalisation.
40. Have <code>__new__</code> return an existing cached instance of the same class. Determine whether <code>__init__</code> runs again and identify the corruption risk from new arguments.
41. Have <code>__new__</code> return an object of an unrelated class. Observe whether the original <code>__init__</code> runs and document why such a factory is usually clearer as a named function.
42. Implement a flyweight for immutable RGB colours. Specify cache ownership, key normalisation, weak versus strong retention, concurrency, copying, pickling, and subclass policy.
43. Construct an object whose initialiser fails after allocating an external mock resource. Prove cleanup behaviour and redesign with a context manager or factory that prevents leakage.
44. Demonstrate the danger of calling an overridable method from a base <code>__init__</code> before subclass fields exist. Repair by changing lifecycle or making the called operation non-overridable.
45. Implement a two-phase object with explicit states <code>NEW</code>, <code>READY</code>, and <code>CLOSED</code>. Reject illegal transitions and test every edge, repeated call, and failure midway through preparation.
46. Use a class method as a parsing constructor returning either a valid instance or a documented exception. Separate syntax parsing from invariant validation and compare with overloading <code>__init__</code> for several input formats.
47. Trace how <code>copy.copy</code> and <code>copy.deepcopy</code> construct a class with nontrivial invariants. Customise only if default graph-copy semantics violate the domain; prove alias preservation in the deep copy.
48. Integration with Chapters 6 and 11: create a resource-owning object usable only under <code>with</code>. Specify construction failure, entry failure, body exception, exit failure, idempotent closure, and prohibition of use after close.

### 9.22.5 Inheritance and behavioural subtyping

49. Write a base method contract as preconditions, postconditions, mutations, and exceptions. Implement two valid subtypes and one that strengthens a precondition; construct a caller that exposes the violation.
50. Create a subtype that weakens a postcondition while retaining the same annotation. Explain why type-checking the signature cannot prove substitution.
51. Create a mutable base whose invariant is undermined by a subtype exposing a new mutator. Identify the history constraint that inheritance violated.
52. Show a subtype that raises a broader exception than the base contract permits. Explain how a base-typed caller’s recovery logic fails.
53. Analyse the rectangle/square mutability problem. Provide one immutable value design and one composition design, and compare which subtype claims remain valid.
54. Implement a subtype that returns a more specific result object while preserving the base postcondition. Explain covariance informally and verify caller compatibility.
55. Override a method with an incompatible keyword name. Show how a caller using the base’s documented keyword fails despite positional tests passing.
56. Mark a method and class as final in annotations. Demonstrate that runtime Python does not ordinarily enforce the marker, then configure a static checker to report misuse.
57. Use <code>Self</code> for a fluent immutable builder. Ensure an inherited method returns the dynamic subtype and compare with a hard-coded base return.
58. Define an abstract base class with one abstract method containing a cooperative default body. Implement a concrete subclass that calls the abstract body through <code>super</code> and explain why abstract does not mean bodyless.
59. Register an unrelated class as a virtual subclass of an ABC. Show effects on <code>issubclass</code> and the absence of ABC methods in its MRO.
60. Compare an ABC, a structural protocol, and a capability test for the same interface. State what each validates at definition, static analysis, and runtime.
61. Refactor a “utility inheritance” relationship into a helper function. Identify whether any remaining subtype or state relationship justifies inheritance.
62. Locate a concrete built-in collection whose subclassing permits invariant bypass through inherited operations. Prefer an appropriate <code>collections</code> wrapper or composition and test every mutating route.
63. Write a substitution test suite parameterised over implementations. Ensure tests cover values, effects, exceptions, ordering, resource behaviour, and repeated calls rather than only method presence.
64. Integration with Chapter 6: define a subtype whose iterator is single-use while the base promises repeatable traversal. Construct a generic consumer that demonstrates the behavioural break.

### 9.22.6 Composition, delegation, protocols, and patterns

65. Refactor a report generator that constructs its filesystem writer internally. Inject a minimal writing protocol and supply in-memory and filesystem adapters.
66. Draw the ownership graph for Exercise 65. State who constructs, closes, replaces, and shares every component.
67. Implement narrow explicit delegation for a storage service. Add a method to the target and prove it is not accidentally exposed by the wrapper.
68. Implement broad <code>__getattr__</code> forwarding for comparison. Catalogue the larger accidental API and show why <code>len</code> is still not forwarded.
69. Build an Adapter that converts a legacy method’s parameters and exception vocabulary into a new protocol. Prove that the adapter does not leak legacy exceptions promised to be hidden.
70. Build a design-pattern Decorator that measures calls around a component without changing the component’s source. Distinguish it from <code>@</code> syntax and state concurrency requirements of accumulated metrics.
71. Implement three Strategy objects for retry delay. Inject one into a coordinator and test policy independently from effect execution.
72. Replace conditional checks for an absent logger with a Null Object. Compare branches, observability, configuration mistakes, and testing.
73. Construct a cycle of two components requiring each other in their constructors. Break the cycle by extracting a lower-level protocol or coordinator and explain the resulting dependency direction.
74. Apply the Law of Demeter to a call chain traversing four objects. Refactor without merely adding forwarding methods everywhere; assign the operation to the owner of the relevant invariant.
75. Define a structural protocol containing a property and method. Implement it without inheriting and demonstrate static substitution plus runtime behaviour.
76. Split a broad protocol into reader and writer capabilities. Show that a read-only consumer can now accept more implementations and cannot statically invoke mutation.
77. Use a callable protocol for strategies with required keyword-only parameters. Compare with <code>Callable</code> and explain why the protocol expresses more shape.
78. Integration with Chapter 8: create a generic repository protocol whose read-only type parameter can be covariant but whose write parameter cannot. Demonstrate an unsafe assignment prevented by invariant typing.

### 9.22.7 Core special-method protocols

79. Implement a finite collection with coherent <code>__len__</code>, <code>__iter__</code>, <code>__contains__</code>, <code>__getitem__</code>, and <code>__reversed__</code>. Prove the coherence equations from §9.12 for representative states.
80. Return <code>-1</code>, a float, and an excessively large integer from separate <code>__len__</code> implementations. Record built-in behaviour and explain the violated contract.
81. Define only <code>__getitem__</code> with integer indexing and observe legacy iteration fallback. Then define <code>__iter__</code> explicitly and justify why explicit protocol support is clearer.
82. Implement an object that is both iterable and its own iterator. Demonstrate exhaustion and explain why a repeatable container should normally return a separate iterator.
83. Build a generator-backed traversal and show exactly when body execution begins, state is suspended, and <code>StopIteration</code> terminates the protocol.
84. Implement slice handling by inspecting <code>slice.start</code>, <code>stop</code>, and <code>step</code>, then normalise with <code>slice.indices</code>. Test negative and omitted bounds.
85. Add <code>__contains__</code> to a sorted collection using binary search. Compare semantic equality and complexity with iteration fallback.
86. Implement <code>__reversed__</code> for a linked representation without first materialising a list; if that is impossible under chosen links, explain the representation tradeoff honestly.
87. Create a callable stateful object and compare its identity, stored state, signature introspection, and pickling with a closure implementing the same computation.
88. Implement <code>__index__</code> for an exact integer-like value. Distinguish its contract from lossy <code>__int__</code> conversion by using it in slicing.
89. Design <code>__repr__</code>, <code>__str__</code>, and <code>__format__</code> for a measurement with units. Support two documented format specifications and reject unknown ones.
90. Implement a synchronous context manager whose <code>__exit__</code> suppresses exactly one documented exception type. Test subclasses of that exception and unrelated failures.
91. Implement an asynchronous context manager around a mock asynchronous resource. Prove acquisition and cleanup order on normal return, body exception, and cancellation.
92. Define <code>__copy__</code> and <code>__deepcopy__</code> for an object graph with a shared child. Use the memo mapping so the deep copy preserves internal alias topology.
93. Customise pickle reduction for a validated immutable value. Round-trip it, change its module/class availability, and explain why pickle is unsuitable for untrusted input or durable schema evolution by default.
94. Subclass <code>dict</code> and implement <code>__missing__</code>. Show which direct access invokes it and which operations such as <code>get</code> may not.
95. Build a protocol-law table for a custom collection: operation, lookup method, valid return, fallback, exception, complexity, mutation, and coherence law.
96. Integration with Chapters 6 and 7: implement a lazy filtered view over a mutable mapping. Define whether iteration is live or snapshot-based and test mutation during traversal.

### 9.22.8 Cooperative operators, equality, and hashing

97. Implement immutable two-dimensional vector addition, scalar multiplication in both operand orders, unary negation, equality, and hashing. Return <code>NotImplemented</code> for unsupported pairs.
98. Add event logs to left and reflected operator methods for unrelated types, equal types, and a strict subtype. Predict and verify dispatch order in every case.
99. Implement reflected subtraction and division. Write asymmetric test values that would reveal accidental operand reversal.
100. Return <code>False</code> rather than <code>NotImplemented</code> from an unsupported equality branch. Construct another type whose reflected equality would have recognised the pair, and show the lost cooperation.
101. Raise <code>NotImplementedError</code> from an arithmetic method and compare its trace with returning <code>NotImplemented</code>. Explain why the right operand loses its opportunity.
102. Implement mutable <code>__iadd__</code> and intentionally omit its return. Observe the original object through an alias and the rebound left variable; repair and specify identity semantics.
103. Reproduce the tuple-containing-list augmented-assignment puzzle. Decompose retrieval, in-place mutation, and failed item storage into distinct steps.
104. Create a money value based on <code>Decimal</code>. Reject mixed currencies, define quantisation ownership, and keep exchange conversion as a separately supplied policy object.
105. Define an exact rational type interoperating with integers. Specify promotion, normalisation, zero denominator, reflected operations, and equal-hash behaviour across equal integer values.
106. Test identity, associativity, and commutativity for an operation. Provide one domain where each law fails and ensure tests do not falsely demand it.
107. Model a partial order such as task prerequisites. Explain why generic sorting cannot express incomparability reliably; expose a named comparison returning a three- or four-way result.
108. Integration with Chapter 7: use custom equal/hashable keys in a dictionary, mutate a field participating in a deliberately defective hash, and explain why the entry becomes operationally lost without leaving storage.

### 9.22.9 Multiple inheritance and cooperative <code>super</code>

109. Compute by hand the C3 linearisation of a diamond, showing every merge candidate and rejected head. Verify with <code>__mro__</code>.
110. Build the contradictory <code>X/Y</code> precedence graph from §9.14. State the unsatisfiable constraints before executing the failing class definition.
111. Add cooperative methods to a diamond and prove the shared root runs exactly once. Then replace one <code>super</code> call with a named base call and identify skipped or duplicated work.
112. In a method defined on the left base, evaluate <code>super(Left, child)</code>. Identify the next class from the receiver’s MRO and explain why it need not be a base of <code>Left</code>.
113. Create one non-cooperative class in a five-class MRO. Log calls and locate precisely where traversal terminates.
114. Implement cooperative keyword-consuming initialisers across three mixins. Test missing, duplicated, misspelled, and leftover arguments at the <code>object</code> endpoint.
115. Replace the <code>**kwargs</code> constructor chain with an explicit configuration dataclass and component construction. Compare static visibility and extension cost.
116. Design a mixin requiring a host protocol. Express the requirement with a protocol or abstract method and prove that the mixin owns no conflicting instance state.
117. Attempt multiple inheritance from two stateful slotted bases. Record layout failure where it occurs and redesign with one component held by the other.
118. Write cooperative class methods and show that <code>cls</code> remains the dynamic receiver while <code>super</code> changes the definition lookup point.
119. Inspect an abstract base with a virtual registered subclass. Prove that <code>super</code> does not traverse the virtual base because registration does not alter <code>__mro__</code>.
120. Integration design review: given logging, caching, authentication, storage, and reporting responsibilities, choose mixin, decorator, proxy, injected component, or ordinary function for each. Defend each choice using state ownership, substitutability, and lifecycle.

### 9.22.10 Descriptors and general attribute access

121. Implement a positive-number descriptor using per-instance dictionary storage. Support class access, unset errors, assignment validation, and prohibited deletion.
122. Reuse the descriptor under two names intentionally and expose its single-name metadata defect. Repair with independent descriptor objects or owner/name-specific metadata.
123. Inherit a descriptor and log the <code>owner</code> passed for base and subclass access. Distinguish original <code>__set_name__</code> owner from dynamic retrieval owner.
124. Implement a generic typed descriptor with overloads for class and instance access. Run a static checker against correct and incorrect assignments.
125. Adapt a descriptor to a slotted class using a dedicated private slot. Avoid recursive access and demonstrate unset behaviour.
126. Build an external-storage descriptor with <code>WeakKeyDictionary</code>. Test collection of managed instances and explain required weak-reference/hash semantics.
127. Implement a non-data caching descriptor. Test first computation, shadowing, explicit invalidation, mutation of source data, and simultaneous first access.
128. Make a descriptor getter accidentally raise <code>AttributeError</code> internally while the owner defines <code>__getattr__</code>. Observe masking and repair the exception boundary.
129. Use <code>inspect.getattr_static</code> and ordinary <code>getattr</code> on functions, properties, and custom descriptors. Catalogue raw versus dynamically bound results.
130. Write a safe <code>__getattribute__</code> audit wrapper using <code>object.__getattribute__</code>. Add a secret field and design a redaction policy; measure the overhead.
131. Write a constrained <code>__getattr__</code> namespace. Ensure misspellings raise <code>AttributeError</code>, operational backend failures remain distinct, and <code>hasattr</code> behaves honestly.
132. Implement lazy fallback caching and then force re-entrant access during computation. Add an explicit “computing” sentinel or lock and specify recursive behaviour.
133. Construct a narrow read-only proxy over a sequence. Implement every promised special method on the proxy type and show which target behaviours remain intentionally hidden.
134. Add <code>__setattr__</code> validation for a naming convention. Compare its broad effects with per-field descriptors, including inheritance and typo cases.
135. Implement freeze-after-initialisation, then subclass it. Expose the subclass-initialisation problem and redesign using an explicit finalisation phase or immutable value construction.
136. Integration with Chapter 8: write decorators for descriptor methods that preserve exception meaning and do not change descriptor classification. Explain why adding <code>__set__</code> dynamically to one descriptor instance does not ordinarily make it a data descriptor.

### 9.22.11 Slots, metaclasses, and class hooks

137. Compare ordinary and slotted point populations using a representative allocation measurement. Include dictionaries and disclose interpreter/platform conditions.
138. Derive the instance layout of a slotted base, a subclass without slots, a subclass with new slots, and an empty-slot subclass. Verify which instances have dictionaries.
139. Add <code>__dict__</code> and <code>__weakref__</code> slots separately. Test dynamic attributes and weak references under all four combinations.
140. Serialize a slotted class with a naive <code>__dict__</code>-based tool and expose data loss. Repair through an explicit state protocol.
141. Build a class dynamically with three-argument <code>type</code>. Match its module, qualified name, method binding, bases, and descriptor notification to a source-defined counterpart.
142. Write a recording metaclass that logs <code>__prepare__</code>, <code>__new__</code>, <code>__init__</code>, and <code>__call__</code>. Explain separate class-creation and instance-creation traces.
143. Make a prepared namespace reject duplicate user fields while accepting necessary compiler-managed bindings. Test decorated methods and annotations.
144. Write a metaclass invariant that distinguishes locally declared from inherited attributes. Supply two separate policies and tests proving the difference.
145. Construct a metaclass conflict from two bases. Create a cooperative combined metaclass, then inspect whether its policies are semantically compatible rather than stopping at successful creation.
146. Implement a singleton metaclass for study. Attack it with different later arguments, subclasses, threads, copying, pickling, and test reset; replace it with an explicit lifetime owner.
147. Customise <code>__instancecheck__</code> structurally. Demonstrate false positives from a callable with the wrong signature and compare a static protocol.
148. Record descriptor <code>__set_name__</code>, base <code>__init_subclass__</code>, metaclass hooks, and two class decorators. Predict the exact order before running.
149. Implement cooperative <code>__init_subclass__</code> hooks consuming independent class keywords. Leave one unconsumed and explain the endpoint error.
150. Register subclasses through <code>__init_subclass__</code>. Test duplicate import/reload, local test classes, abstract intermediates, and explicit unregister policy.
151. Implement the same opt-in transformation as a class decorator. Stack it with registration in both orders and identify registry/name divergence if one decorator replaces the class.
152. Attach a descriptor in a class decorator. Demonstrate missing automatic <code>__set_name__</code>, notify explicitly, and decide whether a metaclass or source declaration is a better lifecycle.

### 9.22.12 Capstone investigations

153. Design a measurement domain containing immutable units, validated readings, a storage protocol, and several reporting implementations. Use no inheritance solely for reuse. Supply object graph, constructors, invariants, equality/hash proof, representations, and substitution tests.
154. Build a small expression tree with literal, unary, and binary nodes. Compare a nominal class hierarchy using polymorphic evaluation with a tagged-data representation using pattern matching. Analyse extension by new node type versus new operation.
155. Implement an event-processing pipeline with cooperative mixins, then reimplement it using composed stage objects. Compare explicit order, state ownership, independent testing, runtime reconfiguration, and failure rollback.
156. Build a schema mini-framework using descriptors and <code>__init_subclass__</code>, not a metaclass. Then identify one genuine requirement that would force namespace preparation and add the narrowest metaclass necessary.
157. Design a capability-secure façade around an administrative object. Expose only read operations through explicit delegation; show why underscore conventions and <code>__getattr__</code> forwarding would fail the authority goal. State limits inside one Python process.
158. Perform an object-model forensic analysis of a mature standard-library class. Inspect its MRO, raw class dictionaries, descriptors, generated methods, slots, equality/hash policy, representations, and construction hooks without relying on undocumented CPython fields.
159. Integration with Chapters 1–8: for one method call, trace physical references conceptually, Python objects and bindings, expression evaluation order, call frames, MRO lookup, descriptor binding, mutation, exception propagation, and eventual reachability. Mark where each earlier simplified model is refined.
160. Research-grade design report: implement a versioned plugin system with explicit discovery, safe import assumptions, subclass validation, structural runtime interface checks, registry isolation, duplicate/version resolution, unload policy, concurrent access control, and comprehensive lifecycle event tests. Explain why in-process plugins cannot be treated as untrusted sandboxes and identify the process boundary needed for isolation.
