# 5.20 Common misconceptions consolidated

1. **“A variable contains a value.”** In the useful Python model, a namespace binds a name to an object. Containers themselves retain references to objects.
2. **“Assignment copies the object.”** Assignment binds a target after evaluation. Copying requires an explicit operation or type-specific construction.
3. **“Immutable means nobody can observe change beneath it.”** An immutable container can refer to mutable objects; its own structure remains fixed while reachable objects change.
4. **“`is` is a faster spelling of `==`.”** `is` tests identity; `==` asks for value equality. They answer different questions.
5. **“An `id` permanently identifies a value.”** Identity belongs to one object lifetime; implementations may reuse returned integers later.
6. **“Floats are random or broken.”** They implement finite binary approximations under deterministic rounding rules.
7. **“A string is an array of characters, each one byte.”** Python `str` stores Unicode text conceptually as code points; encoding determines bytes, and perceived characters may span code points.
8. **“False, zero, empty, and `None` all mean missing.”** Truth testing groups them in Boolean contexts, but their domain meanings remain distinct.
9. **“Type annotations make Python statically typed at runtime.”** They describe intent; ordinary runtime execution does not enforce them automatically.
10. **“Everything seen in CPython is Python.”** Language guarantees, implementation strategies, and experiment results require separate labels.

11. **“Multiplication executes before the left operand of addition.”** Precedence determines grouping; operand evaluation still follows the expression’s evaluation rules.
12. **“Parentheses create tuples.”** A comma creates non-empty tuple structure; parentheses group and are required for the empty tuple.
13. **“A failed assignment leaves all state unchanged.”** Right-side effects, iterable consumption, in-place mutation, and earlier target assignments can survive a later failure.
14. **“Function arguments are copied into parameters.”** Parameters become bindings to supplied objects. Copying is a separate operation.
15. **“Mutable values are passed by reference but immutable values by value.”** Python uses one object-binding call model; mutability determines which changes can be observed through aliases.
16. **“Default arguments are calculated when omitted.”** Default expressions execute when the function definition executes and their objects are retained.
17. **“A successful type annotation validates the runtime value.”** Ordinary annotations publish metadata and static intent; domain validation remains executable logic.
18. **“Duck typing means types do not matter.”** It makes behavioural protocols central; an object must still satisfy exact operation and semantic obligations.
19. **“Converting input makes it valid.”** Conversion establishes one representational property and can lose distinctions. Domain constraints require separate checks.
20. **“Unicode equality means visually equal text.”** Ordinary string equality compares code-point sequences; normalisation, grapheme structure, casing, and collation are separate policies.
21. **“Raw strings are safe strings.”** Raw notation changes Python literal escape processing only; it supplies no safety for downstream languages.
22. **“Bytes displayed as letters are text.”** A bytes representation uses printable characters as notation. Text exists only under an encoding contract.
23. **“Deep copy recursively duplicates reality.”** It follows customisable object protocols, preserves selected sharing, and cannot duplicate external resources or identities universally.
24. **“A hash identifies a value permanently.”** Python hashes are collision-prone process tools, and selected hashes can be randomised.
25. **“An official-interpreter observation is a language law.”** CPython behaviour must be classified against the language reference and versioned implementation contract.
