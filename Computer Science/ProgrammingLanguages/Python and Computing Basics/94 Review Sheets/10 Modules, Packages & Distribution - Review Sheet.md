# 10.16 Common misconceptions consolidated

### 10.16.1 Modules and import execution

1. **“A module is a file.”** A module is a runtime namespace object. Source files are one common origin; built-in, frozen, generated, archive-loaded, and custom-loaded modules need not have an ordinary file.
2. **“One file always corresponds to one module object.”** Loading the same source under distinct names or interpreters can create multiple objects and class identities.
3. **“Import pastes definitions into the caller.”** It loads or reuses module objects and performs specified name bindings.
4. **“Import only declares dependencies.”** A new module’s top-level code executes with process authority.
5. **“Importing twice always executes twice.”** Ordinary import reuses <code>sys.modules</code> under the same name.
6. **“Importing twice can never execute twice.”** Reload, failed import retry, separate processes, aliases, custom hooks, and distinct names can re-execute source.
7. **“<code>sys.modules</code> lists installed packages.”** It maps currently loaded module names to objects; distribution metadata is separate.
8. **“Removing a module from <code>sys.modules</code> unloads it.”** Existing references remain, resources may remain open, and re-import can create a second generation.
9. **“A failed import rolls back its effects.”** The failing cache entry is normally removed, but earlier mutations and successfully imported dependencies can remain.
10. **“The import lock makes module globals thread-safe.”** It coordinates aspects of loading; arbitrary later state access and effects require their own concurrency policy.
11. **“A bytecode cache means the module body need not run.”** It can avoid parsing/compilation; execution still creates runtime bindings.
12. **“Reload updates every imported reference.”** It re-executes a module context; external bindings and old instances/classes remain.

### 10.16.2 Names, paths, and entry execution

13. **“<code>import a.b</code> binds local <code>b</code>.”** Without alias it ordinarily binds top-level <code>a</code>; <code>a.b</code> becomes accessible through the package.
14. **“From-import copies the object.”** It binds another reference to the current object; later source rebinding does not propagate, while mutation of a shared object can.
15. **“Patching the defining module always changes consumers.”** Code uses the binding in the namespace it looks up at call time; from-import consumers may hold separate bindings.
16. **“An import inside a function reloads on every call.”** The module is normally cached, though a local binding is performed and failure is deferred.
17. **“Catching every import exception is a valid optional-dependency check.”** It conceals defects and missing transitive requirements; catch and classify the intended absence narrowly.
18. **“Wildcard import makes all names public.”** It selects bindings via <code>__all__</code> or fallback rules; public support is a broader documented contract.
19. **“Absolute import means an absolute filesystem path.”** It starts from an import-system root and can resolve through varied loaders and locations.
20. **“Absolute imports always select this project’s package.”** Active search order can select a shadowing module.
21. **“Relative imports are unreliable.”** They are deterministic given valid package identity and context; direct internal-file launch commonly destroys that context.
22. **“A directory containing <code>__init__.py</code> makes direct execution package-aware.”** Runtime loading identity, not containment alone, establishes package context.
23. **“Changing dots can fix a circular import.”** Spelling changes resolution, not the dependency graph.
24. **“<code>-m</code> and direct-file execution differ only in convenience.”** They establish different specification/package context and can alter identity and imports.
25. **“<code>__name__ == '__main__'</code> identifies a file named <code>__main__.py</code>.”** It identifies the current top-level execution environment.
26. **“A name guard prevents every import side effect.”** Only its suite is conditional; all other top-level statements execute.
27. **“Returning an integer from <code>main</code> sets process status automatically.”** An entry adapter must pass it to <code>SystemExit</code> or generated equivalent.

### 10.16.3 Architecture, state, and APIs

28. **“Modularity means more files.”** It means cohesive ownership, explicit interfaces, and controlled dependency direction; fragmentation can worsen all three.
29. **“Few imports mean low coupling.”** Representation, temporal, failure, deployment, and authority coupling can exist without many import statements.
30. **“The import graph is the call graph.”** Dependency direction and runtime dynamic calls can point differently.
31. **“Every circular import is rejected.”** Some complete because retrieval is deferred; they remain temporally coupled and fragile.
32. **“A local import structurally repairs a cycle.”** It only changes when the edge is exercised unless architecture also changes.
33. **“A common module always reduces duplication cleanly.”** An incoherent dumping ground creates a dependency magnet and new cycles.
34. **“Module globals are universally bad.”** Immutable definitions and deliberately scoped state can have clear module ownership; hidden mutable lifecycle is the defect.
35. **“<code>global</code> means one value across the application.”** It targets one defining module namespace, ordinarily per module identity and interpreter/process.
36. **“A module cache is a safe cache policy.”** Retention, size, invalidation, concurrency, secrets, and process scope remain unanswered.
37. **“Dependency injection requires a container framework.”** Passing a collaborator or factory explicitly is injection.
38. **“A service locator and injection are equivalent.”** A locator hides acquisition inside consumers and grants ambient registry access; injection makes requirements visible at assembly.
39. **“Uppercase constants are enforced immutable.”** Uppercase is a convention, and referenced objects may also be mutable.
40. **“Keeping a public name preserves compatibility.”** Signatures, semantics, effects, exceptions, ownership, ordering, typing, and cost can change incompatibly.
41. **“<code>__all__</code> hides internal names.”** It controls wildcard selection and signals intent; explicit access remains possible.
42. **“A redefined compatibility class is the same as a re-export.”** Redefinition creates new type identity; re-export binds the same object.
43. **“A deprecation warning permits immediate removal.”** Deprecation is a staged migration contract under the project’s compatibility policy.

### 10.16.4 Packaging, builds, and dependency resolution

44. **“Package, project, repository, and distribution are one thing.”** They are related units with potentially different names and cardinalities.
45. **“The pip project name can always be inferred from the import.”** Mappings are not one-to-one; authoritative metadata is required.
46. **“If metadata says a version is installed, that code handled the import.”** Shadowing, editable sources, overlaps, and mutation can separate resolved code from metadata.
47. **“<code>pyproject.toml</code> is pip configuration.”** It carries standard build/project metadata and namespaced configuration for many tools; pip is one possible consumer/frontend.
48. **“Build requirements are runtime dependencies.”** They bootstrap the build backend; installed runtime requirements are declared separately.
49. **“Build isolation makes a build safe.”** It reduces ambient dependency leakage but still executes build code and depends on external toolchain/authority controls.
50. **“An sdist is an arbitrary source ZIP.”** It is a standard source-distribution artefact with metadata and build sufficiency obligations.
51. **“A wheel is source code renamed.”** It is a standard installation-oriented archive with internal metadata and compatibility tags.
52. **“Pure Python means platform behaviour is identical.”** OS APIs, encodings, path rules, dependency markers, and interpreter differences remain.
53. **“A wheel cannot execute code.”** Importing it executes modules; installation and generated entry points also involve executable tooling.
54. **“Source tests prove the wheel.”** File selection, resources, metadata, entry points, and import roots can differ; test the installed artefact outside the checkout.
55. **“An exact version pin identifies exact bytes.”** A version may have several wheels and an sdist; hashes bind accepted artefacts.
56. **“Exact pins alone make an environment reproducible.”** Interpreter, platform, indexes, artefacts, build tools, external libraries, and markers also matter.
57. **“A lock proves security.”** It records a selection; trustworthy provenance, vulnerability review, updates, and containment are separate.
58. **“Resolve each dependency independently at its newest version.”** The entire transitive constraint graph must have one compatible selection.
59. **“Extras are runtime feature switches.”** They add installation requirements; runtime configuration and capability detection remain.
60. **“A transitive dependency need not be declared when directly imported.”** Relying on another project to retain it creates an undeclared unstable edge.

### 10.16.5 Resources, namespaces, and security

61. **“A package is always one directory.”** Namespace packages can combine portions, and loaders can represent packages outside ordinary directories.
62. **“Every package has <code>__init__.py</code>.”** Implicit namespace packages need not.
63. **“Namespace packages merge same-named modules.”** They combine search portions; one fully qualified module name still resolves to one selected module.
64. **“Package resources are ordinary neighbouring files.”** They are logical loader-managed contents and may require a Traversable or temporary materialisation.
65. **“Installed package directories are suitable for mutable user data.”** They may be read-only, shared, archived, or replaced; use designated external data locations.
66. **“If a resource exists in Git, it enters the wheel.”** Backend inclusion rules decide artefact contents; verify both archives and clean installation.
67. **“Importing a plugin is safer than running an executable.”** Import executes arbitrary code with current process authority.
68. **“Protocol validation sandboxes a plugin.”** It checks interface compatibility, not filesystem, network, memory, or credential authority.
69. **“Checking <code>__file__</code> before use prevents malicious import.”** Import has already executed, attributes can lie, and pre-checks can race. Control provenance and environment before execution.
70. **“A private index first in a list always prevents dependency confusion.”** Candidate/source selection semantics require explicit tested source binding and hashes.
71. **“Our code never imports it, so it cannot execute.”** Startup customisation, path configuration, build hooks, entry points, instrumentation, and plugins can execute dependencies indirectly.
72. **“No third-party runtime dependencies means no supply-chain risk.”** Build requirements, interpreter/runtime distribution, release infrastructure, and packaged source still form a supply chain.
