# 10.17 Exercises

The exercises progress from namespace mechanics to release engineering. Perform import-lifecycle experiments in disposable directories and fresh interpreters; a long-running REPL can conceal cache and ordering effects.

### 10.17.1 Module boundaries and dependency architecture

1. Classify a repository, source file, runtime module, import package, namespace package, and distribution. Give a counterexample to every proposed one-to-one mapping between them.
2. Take a 200-line “utilities” module and classify each function by invariant, reason to change, and dependency. Propose cohesive modules without applying a one-function-per-file rule.
3. For five modules in a small application, draw both import and possible runtime call graphs. Identify at least one edge whose direction differs between them because of injected polymorphism.
4. Define cohesion and six forms of coupling using concrete code from one project. Explain which coupling is essential and which leaks representation or lifecycle.
5. Measure change amplification for a public class imported through ten physical submodule paths. Add a façade and show which future move edits become unnecessary.
6. Split domain model, parser, formatter, persistence, and command interface into layers. For every import edge, state why the source needs knowledge of the target.
7. Deliberately make a domain module import a CLI parser. Explain the inversion and refactor coordination outward.
8. Compare a one-class-per-file layout with a cohesive domain-module layout for six related value types. Measure navigation, cycles, test boundaries, and public paths.
9. Identify the most stable and most volatile modules from version history. Test whether dependency direction points toward stability; propose one inversion.
10. Create an architecture rule forbidding domain-to-adapter imports. Implement a static or test-time check and document dynamic-import limitations.
11. Design a package façade that exposes five stable concepts while keeping twelve helpers internal. Ensure internal modules do not re-enter the façade and cause cycles.
12. Analyse a module-global cache as a component: owner, lifetime, capacity, invalidation, failures, concurrency, secret exposure, and test reset.
13. Move that cache into an injected object. Compare construction, call signatures, process scope, and test isolation.
14. Decide whether two mutually dependent files should merge or extract a lower abstraction. Defend the decision using cohesion and independent reasons to change.
15. Integration with Chapter 9: model a package as an object graph of modules, classes, descriptors, and shared globals. Mark ownership and reference-lifetime edges.

### 10.17.2 Import machinery and module identity

16. Create a module printing an execution marker. Import it twice under one canonical name in one process and once in each of two subprocesses; explain counts.
17. Inspect its entry in <code>sys.modules</code>, package attribute binding, <code>__spec__</code>, loader, origin, package, and file where present.
18. Import one source under two names using an intentionally constructed loader experiment. Show duplicate class identity and registry state; explain why production code should avoid it.
19. Delete only the local module variable after import. Prove the module remains cached. Then remove only the cache entry while another reference remains and explain why this is not unloading.
20. Re-import after cache removal and compare old/new module and class objects. Do not use this as an application reload mechanism.
21. Build a module that mutates a registry and then raises. Import twice under exception handling and account for every retained effect and cache entry.
22. Make the failing module import a successful helper first. Show why the helper remains cached across retries.
23. Use <code>importlib.util.find_spec</code> for built-in, source, package, namespace, and missing names. Record which fields cannot be assumed universal.
24. Write a minimal educational meta-path finder/loader for one fixed in-memory module. Implement cache-compatible loading, then list why arbitrary custom loading broadens security and debugging risk.
25. Insert and restore the finder with a context manager so failure cannot pollute <code>sys.meta_path</code>. Consider concurrent imports.
26. Inspect <code>sys.path</code> under a shell, <code>-m</code>, a direct script, a test runner, and a virtual environment. Explain each relevant difference without assuming order is portable.
27. Create a local file shadowing a standard-library module in a disposable directory. Diagnose using specification and origin; repair by renaming.
28. Demonstrate parent-package initialisation before child-module execution with an event log.
29. Show that a package child becomes an attribute of the parent after import. Rebind that attribute and compare it with <code>sys.modules</code>.
30. Inspect a <code>__pycache__</code> directory after importing source. Start a fresh process and prove that bytecode caching does not suppress body execution.
31. Change source under conditions that invalidate its cache and observe recompilation without treating timestamp details as universal.
32. Reload a module that defines a class. Compare old imported class, new module class, existing instances, and a registry holding the old class.
33. Remove a name from source before reload. Determine whether the old module binding remains and derive the namespace-retention hazard.
34. Put a heavy optional import behind first use. Measure startup and first-use latency, then document changed failure timing and concurrency policy.
35. Integration with Chapter 6: model import loading as a state machine with absent, creating, executing, complete, and failed states. Place cache insertion/removal and recursive observation transitions.

### 10.17.3 Import forms, scope, and entry environments

36. Compare <code>import package.child</code>, <code>import package.child as alias</code>, <code>from package import child</code>, and <code>from package.child import Name</code>. Draw every local and package binding.
37. Import a mutable object with both module and from-import forms. Mutate it, then rebind the source attribute; predict all observations.
38. Construct the monkeypatch-location example. Patch the defining namespace and consuming namespace separately and explain results from lookup timing.
39. Place an import inside a function and inspect local/global namespaces. Call repeatedly and distinguish name binding from module execution.
40. Write a conditional import that leaves a local name unbound. Repair it with explicit capability branching and a meaningful absence error.
41. Simulate an optional package absent versus a present package with a missing transitive dependency. Catch only the intended <code>ModuleNotFoundError</code> by inspecting its name.
42. Define <code>__all__</code> containing a missing name and perform wildcard import in a disposable module. Explain failure timing.
43. Compare module qualification and direct symbol imports for two colliding <code>parse</code> functions. Choose readable aliases.
44. In a three-level package, resolve one-, two-, and three-dot imports by hand. Attempt to traverse beyond the package root and explain the failure.
45. Execute one internal file directly and with <code>-m</code>. Compare <code>__name__</code>, <code>__package__</code>, <code>__spec__</code>, <code>sys.path[0]</code>, and relative imports.
46. Make entry code import its canonical module name and demonstrate duplicate definition identity. Refactor substantial definitions into a canonical implementation module.
47. Write <code>main(arguments)</code>, a thin <code>__main__.py</code>, and a console-script target sharing one implementation. Test both launch routes.
48. Return statuses 0, 1, and 2 for success, operational failure, and usage failure. Assert stdout/stderr separation in subprocess tests.
49. Make a deep library function call <code>sys.exit</code>. Show the composition defect, replace it with a domain exception, and translate at entry.
50. Integration with Chapter 6: use a context manager to capture/restore process-global state modified by an entry test. Explain why subprocess isolation proves more.

### 10.17.4 Circular imports and initialisation order

51. Construct the two-module from-import cycle and annotate which statement has completed when failure occurs.
52. Replace one edge with module import plus delayed attribute access. Show why the current run succeeds and the structural cycle remains.
53. Reorder top-level assignments so the latent cycle changes behaviour. Use this as evidence of temporal coupling.
54. Create a façade cycle through <code>package.__init__</code> re-exports. Repair internal imports to target defining modules.
55. Extract a shared immutable value type from two mutually importing domain modules. Draw the acyclic result.
56. Invert a concrete database/report dependency through a protocol owned by reporting policy. Show import edge and runtime call edge directions.
57. Move orchestration from one low-level module into a higher application module. Verify that both lower modules are independently importable.
58. Merge two falsely separated modules and argue why cohesion improves despite increased file length.
59. Use <code>TYPE_CHECKING</code> for a genuinely annotation-only edge. Resolve annotations at runtime and document when the hidden name is needed.
60. Create a framework that reflects annotations during class construction. Show why a type-check-only import may be insufficient and design a shared contract module.
61. Refactor a plugin base that imports implementations into external entry-point discovery. Ensure the contract does not know concrete plugins.
62. Extract a static import graph and compute strongly connected components. Compare with a runtime trace under one test workload.
63. Import public modules in varied orders in fresh subprocesses. Treat any order-dependent success as a defect and locate shared state.
64. Create a module-level service instance that deepens a cycle. Move assembly into a composition-root function and specify resource closure.
65. Write a cycle review report classifying each edge as type-only, late optional, misplaced coordination, concrete inversion, façade re-entry, or falsely split cohesion.

### 10.17.5 Public APIs, state, and evolution

66. Define a package API with re-exports and <code>__all__</code>. Write tests that every listed name exists and no chosen internal dependency leaks through wildcard import.
67. Move a class to a new module while re-exporting the same object from the old path. Prove identity, instance checks, and pickling expectations under both paths.
68. Repeat Exercise 67 by copying/redefining the class and catalogue every identity break.
69. Produce ten API changes retaining all public names: one each for signature, accepted values, return ownership, order, exception, side effect, resource lifetime, typing, complexity, and security authority.
70. Add an optional keyword-only parameter without breaking existing calls. Then rename an existing keyword and show the break missed by positional tests.
71. Evolve an overridable base method by adding a passed keyword. Test existing subclass overrides and design a compatible extension mechanism.
72. Change a list result to a generator. Build callers broken by indexing, repeated iteration, truth testing, eager validation, and resource lifetime.
73. Build a module-level deprecation alias using <code>__getattr__</code>. Test warning category, stack location, repeated access, static typing, and eventual removal.
74. Customise module <code>__dir__</code> for the alias. Explain why discoverability and actual retrieval are separate.
75. Implement a lazy public export. Test first access, failed import, retry, concurrent access, <code>dir</code>, pickling name, and startup measurement.
76. Define a small stable exception hierarchy and translate a vendor exception with causal chaining. Test callers at broad and narrow recovery levels.
77. Return a live mutable view in version 1 and snapshot in version 2. Analyse both behavioural directions and write migration documentation.
78. Specify an ordering guarantee for query results. Build tests that assert only that guarantee, not incidental internal order.
79. Establish a documented complexity bound and benchmark representative scale. Show why timing alone does not prove asymptotic class.
80. Publish runtime annotations and a <code>py.typed</code> marker. Build a clean consumer fixture that type-checks from the wheel.
81. Compare source <code>__version__</code> with installed distribution metadata and eliminate duplicate version sources.
82. Create an API-change review table for a real refactor and fill every dimension, including “unchanged with evidence.”
83. Move global configuration parsing into one immutable object at startup. Prohibit scattered environment reads and test invalid configurations before resource acquisition.
84. Replace global clients with constructor and factory injection. State why session lifetime requires a factory rather than one shared object.
85. Integration with Chapter 9: define public subclassing hooks, final internals, and supported composition protocols for a library. Explain which internals external subclasses may rely on.

### 10.17.6 Project metadata and build systems

86. Write a current <code>pyproject.toml</code> for a <code>src</code>-layout pure Python library: build system, static metadata, Python range, SPDX licence expression, licence files, readme, dependencies, test extra, URLs, and entry point.
87. Parse the TOML and classify every field’s TOML type and consuming standard/tool.
88. Deliberately place runtime dependencies in <code>build-system.requires</code>. Build/install and explain why the installed project can still lack them.
89. Make the build succeed only because of an undeclared ambient build package. Enable isolation and repair the build requirements.
90. Derive version dynamically without importing the runtime package. Explain the build cycle avoided.
91. Configure a dynamic version by importing a package that imports an uninstalled runtime dependency. Reproduce the failure and redesign.
92. Add environment markers for a genuinely platform- or Python-specific requirement. Resolve on at least two target simulations and verify marker logic.
93. Define two public extras and show that requesting both unions additional requirements while installing one base distribution.
94. Declare a console script and verify the generated command only after installation. Change the target without reinstalling and diagnose the stale wrapper.
95. Define a plugin entry-point group in a separate distribution. Discover metadata without importing plugins, then load one under explicit failure handling.
96. Configure backend-specific package discovery for <code>src</code>. Prove that standard <code>[project]</code> metadata alone did not choose file inclusion.
97. Deliberately omit <code>py.typed</code>, a stub, a licence, and a resource in separate builds. Detect each through archive and clean-install tests.
98. Put a fake credential in a tool table in a disposable project, build archives, and inspect how easily configuration enters source artefacts. Remove it and define an external secret path.
99. Validate long-description rendering and links as they appear outside the repository.
100. Compare broad library requirements with an application lock. Explain why publishing the exact lock as library metadata can make composition impossible.

### 10.17.7 Sdists, wheels, installation, and resolution

101. Build sdist and wheel directly from checkout. Then build the wheel from the sdist and compare contents/metadata.
102. List wheel internals and identify code, package data, distribution metadata, entry points, and file records.
103. Parse a wheel filename into distribution, version, build component if present, Python tag, ABI tag, and platform tag.
104. Compare a pure <code>py3-none-any</code> wheel with a native wheel from an available project. Explain which compatibility claims each filename makes and does not make.
105. Install the wheel in a clean environment outside the repository. Import public names, query distribution metadata, run entry commands, and load resources.
106. Install in editable mode and show source edits affecting imports. Contrast file locations and behaviour with regular wheel installation.
107. Use <code>packages_distributions</code> to map several import names. Find a non-one-to-one example and explain metadata limitations.
108. Create two disposable distributions that collide on one module path. Observe installation/uninstallation risk; do not perform this in a valued environment.
109. Measure reproducibility of two builds. Identify timestamp, ordering, generated metadata, toolchain, or path sources of differing hashes.
110. Create a release manifest recording source revision, builder, build requirements, Python/platform, artefact names/hashes, and verification results.
111. Parse and order versions containing release, pre-release, post-release, development, epoch, and local components using a packaging-aware library; compare lexical order.
112. Evaluate specifier membership for bounds, exclusions, wildcard equality, and compatible release. Derive each accepted set before running.
113. Construct a four-project dependency graph with one unsatisfiable candidate combination. Manually backtrack to a valid solution or prove none.
114. Demonstrate that broad resolution can select a different valid graph after adding a candidate, while a lock retains the recorded one.
115. Distinguish a requirement from a constraint by constraining a project no dependency requests. Observe whether it is installed under the chosen tool.
116. Generate or reason about locks for two operating systems with marker-dependent dependencies. State whether the lock is universal or target-specific.
117. Pin a version with several platform wheels and show why the version alone does not identify bytes. Add accepted hashes.
118. Analyse extras from two dependants and compute the union of activated requirements.
119. Declare a direct VCS or archive reference in a private experiment. Replace a moving branch with immutable identity and remove credentials from the URL.
120. Run an installed-consistency checker, then create a behavioural incompatibility that metadata ranges permit. Explain why tests remain necessary.

### 10.17.8 Namespace packages and resources

121. Build two disposable distributions contributing distinct children to one implicit namespace. Inspect the namespace path and import both children.
122. Add <code>__init__.py</code> to one root portion and observe changed resolution. Explain why namespace conventions must be coordinated.
123. Make two portions supply the same child module and diagnose which is selected. Treat this as a collision, not merging.
124. Query distribution providers for the namespace top-level name and explain the list result.
125. Package a UTF-8 text template and binary fixture. Read both with <code>importlib.resources.files</code> from a clean wheel installation.
126. Use <code>as_file</code> for an API requiring a path. Attempt to retain the path after context exit and explain the invalid lifetime assumption.
127. Run a package from an archive-compatible importer where feasible and show why <code>Path(__file__).parent</code> assumptions fail or narrow portability.
128. Deliberately omit a resource from the wheel while it remains in source. Make the clean-install test expose the omission.
129. Attempt to write mutable state beside an installed package under a read-only simulation. Redesign using an external platform-appropriate data directory.
130. Place a large optional dataset in a wheel and calculate distribution/storage/update cost. Design an integrity-verified external data protocol instead.

### 10.17.9 Import and supply-chain security

131. Create a disposable path-shadowing demonstration for a harmless module. List the preconditions an attacker would need and the environment controls that remove them.
132. Inspect site startup configuration in a disposable virtual environment. Identify which installed configuration can run imports before application code.
133. Build a dynamic plugin loader with an allowlisted identifier-to-entry-point mapping. Reject arbitrary dotted names and validate the loaded interface.
134. Threat-model the plugin under malicious behaviour. Specify a separate-process protocol and restrictions for files, network, environment, CPU, memory, and child processes.
135. Model dependency confusion for an internal name across public/private indexes. Define source binding, authentication, hashes, and a resolution test.
136. Review a lock entry as an integrity claim. Identify who authorised its hash and what malicious-but-approved artefact risk remains.
137. Separate a build job from a publication job so untrusted build code cannot access publishing credentials. Specify the artefact handoff and verification.
138. Audit import-error logs for path, URL, environment, and credential leakage. Add redaction without destroying causal diagnostics.
139. Remove an apparently unused dependency only after checking static imports, dynamic entry points, build configuration, startup hooks, and optional feature tests.
140. Produce a ten-question threat model for the complete import/build/deploy chain of a selected Python application.

### 10.17.10 Capstone projects

141. Implement the ledger architecture from §10.15. It must be usable as library and command, contain exact domain values, remain import-safe, have an acyclic dependency graph, and translate boundary failures coherently.
142. Package it with current metadata, an SPDX licence expression, type information, one optional adapter extra, and convergent <code>-m</code>/console entry points.
143. Build sdist and wheel from a clean revision, build the wheel from the sdist, inspect both, and install/test outside source on every supported Python version.
144. Add a package resource only where it serves a real requirement. Verify through Traversable access and path materialisation in installed and archive-like layouts.
145. Publish a version 2 design that moves internal modules while preserving root public identities. Supply deprecation, exception, typing, serialisation, and performance compatibility analysis.
146. Add a third-party exporter through entry-point discovery. Keep its contract in the host, isolate import failure, detect duplicate names/versions, and explain why in-process loading is trusted execution.
147. Create a reproducibility and provenance report including source identity, build inputs, dependency graph, artefact hashes, target tags, tests, and unresolved environmental inputs.
148. Build an import-forensics command that reports interpreter, environment prefixes, search path, spec, origin, loader, cache identity, candidate distributions, and installed metadata without claiming these facts prove trust.
149. Research a mature Python distribution’s package layout and evolution. Map repository, distributions, import packages, namespace portions, public façades, build backend, wheels, extras, and entry points using primary sources and artefact inspection.
150. Defend the complete project in an oral-style report: for every module and dependency, state responsibility, public contract, import-time effect, state lifetime, failure vocabulary, authority, installation source, test evidence, and planned compatible evolution.
