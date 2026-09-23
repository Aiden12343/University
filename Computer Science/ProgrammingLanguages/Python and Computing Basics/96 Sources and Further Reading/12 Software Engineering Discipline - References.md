# 12.27 References and further study

The references below mix normative specifications, primary tool documentation, foundational papers, and advanced texts. Versioned online documentation should be read for the exact tool release used by a project.

1. ISO/IEC/IEEE, *Systems and Software Engineering—Software Life Cycle Processes*, ISO/IEC/IEEE 12207:2017. Defines a comprehensive vocabulary and process framework for software lifecycles.
2. ISO/IEC/IEEE, *Systems and Software Engineering—Life Cycle Processes—Requirements Engineering*, ISO/IEC/IEEE 29148:2018. Normative treatment of requirements processes, information items, and characteristics.
3. ISO/IEC, [*Systems and Software Quality Requirements and Evaluation—Product Quality Model*](https://www.iso.org/standard/78176.html), ISO/IEC 25010:2023. Current product-quality characteristic model.
4. ISO/IEC/IEEE, *Systems and Software Engineering—Architecture Description*, ISO/IEC/IEEE 42010:2022. Defines architecture-description concepts, viewpoints, views, and decisions.
5. IEEE Computer Society, *Guide to the Software Engineering Body of Knowledge (SWEBOK Guide)*, Version 4.0. Broad map of recognised software-engineering knowledge areas.
6. ACM and IEEE Computer Society, *Software Engineering Code of Ethics and Professional Practice*, 1999. Professional obligations concerning public interest, clients, product quality, judgement, management, profession, colleagues, and self.
7. F. P. Brooks, Jr., “No Silver Bullet—Essence and Accidents of Software Engineering,” *Computer* 20(4), 1987, pp. 10–19. Classic argument concerning essential complexity and limits of universal productivity claims.
8. D. L. Parnas, “On the Criteria To Be Used in Decomposing Systems into Modules,” *Communications of the ACM* 15(12), 1972, pp. 1053–1058. Foundational information-hiding and change-oriented modularity argument.
9. M. Shaw and D. Garlan, *Software Architecture: Perspectives on an Emerging Discipline*, Prentice Hall, 1996. Establishes architectural styles, components, connectors, and reasoning perspectives.
10. L. Bass, P. Clements, and R. Kazman, *Software Architecture in Practice*, 4th ed., Addison-Wesley, 2021. Quality-attribute scenarios, architecture design, evaluation, and documentation.
11. M. Fowler, *Refactoring: Improving the Design of Existing Code*, 2nd ed., Addison-Wesley, 2018. Catalogue and process for behaviour-preserving structural change.
12. G. J. Myers, C. Sandler, and T. Badgett, *The Art of Software Testing*, 3rd ed., Wiley, 2011. Systematic testing principles and test design.
13. P. Ammann and J. Offutt, *Introduction to Software Testing*, 2nd ed., Cambridge University Press, 2016. Formal coverage criteria, graph, logic, syntax, and input-space testing.
14. G. Meszaros, *xUnit Test Patterns: Refactoring Test Code*, Addison-Wesley, 2007. Detailed vocabulary for fixtures, doubles, smells, and test organisation.
15. B. Beizer, *Software Testing Techniques*, 2nd ed., Van Nostrand Reinhold, 1990. Foundational structural and functional testing analysis.
16. V. R. Basili, R. W. Selby, and D. H. Hutchens, “Experimentation in Software Engineering,” *IEEE Transactions on Software Engineering* SE-12(7), 1986, pp. 733–743. Methodological treatment of controlled software-engineering experiments.
17. T. J. McCabe, “A Complexity Measure,” *IEEE Transactions on Software Engineering* SE-2(4), 1976, pp. 308–320. Introduces cyclomatic complexity.
18. J. J. Chilenski and S. P. Miller, “Applicability of Modified Condition/Decision Coverage to Software Testing,” *Software Engineering Journal* 9(5), 1994, pp. 193–200. Explains and evaluates MC/DC.
19. Y. Jia and M. Harman, “An Analysis and Survey of the Development of Mutation Testing,” *IEEE Transactions on Software Engineering* 37(5), 2011, pp. 649–678. Comprehensive mutation-testing survey.
20. K. Claessen and J. Hughes, “QuickCheck: A Lightweight Tool for Random Testing of Haskell Programs,” *Proceedings of ICFP*, 2000, pp. 268–279. Foundational property-based testing paper.
21. Hypothesis Project, [*Hypothesis Documentation*](https://hypothesis.readthedocs.io/en/latest/). Official documentation for Python property-based generation, shrinking, stateful tests, and settings.
22. pytest Development Team, [*Good Integration Practices*](https://docs.pytest.org/en/stable/explanation/goodpractices.html). Official collection, layout, import-mode, and installed-package testing guidance.
23. pytest Development Team, [*How to Use Fixtures*](https://docs.pytest.org/en/stable/how-to/fixtures.html). Official fixture dependency, scope, parameterisation, and teardown semantics.
24. pytest Development Team, [*How to Parametrize Fixtures and Test Functions*](https://docs.pytest.org/en/stable/how-to/parametrize.html). Official parameterisation rules and examples.
25. pytest Development Team, [*How to Monkeypatch/Mock Modules and Environments*](https://docs.pytest.org/en/stable/how-to/monkeypatch.html). Official temporary mutation helpers and restoration behaviour.
26. pytest Development Team, [*How to Manage Logging*](https://docs.pytest.org/en/stable/how-to/logging.html). Official log capture and configuration behaviour.
27. Python Software Foundation, [<code>unittest</code>—Unit Testing Framework](https://docs.python.org/3.12/library/unittest.html), Python 3.12 Standard Library. Specifies the standard xUnit-style framework and mock facilities.
28. Python Software Foundation, [<code>doctest</code>—Test Interactive Python Examples](https://docs.python.org/3.12/library/doctest.html), Python 3.12 Standard Library. Specifies discovery, execution, flags, and output comparison for executable examples.
29. A. Zeller, *Why Programs Fail: A Guide to Systematic Debugging*, 2nd ed., Morgan Kaufmann, 2009. Scientific debugging, cause–effect reasoning, and automated isolation.
30. H. Cleve and A. Zeller, “Locating Causes of Program Failures,” *Proceedings of ICSE*, 2005, pp. 342–351. Cause-transition and automated debugging research.
31. A. Zeller and R. Hildebrandt, “Simplifying and Isolating Failure-Inducing Input,” *IEEE Transactions on Software Engineering* 28(2), 2002, pp. 183–200. Delta debugging for systematic input reduction.
32. Python Software Foundation, [<code>pdb</code>—The Python Debugger](https://docs.python.org/3.12/library/pdb.html), Python 3.12 Standard Library. Official breakpoint, stack, stepping, and post-mortem debugger semantics.
33. Python Software Foundation, [<code>logging</code>—Logging Facility for Python](https://docs.python.org/3.12/library/logging.html), Python 3.12 Standard Library. Official logger hierarchy, records, handlers, filters, formatters, and configuration.
34. Python Software Foundation, [<code>faulthandler</code>—Dump the Python Traceback](https://docs.python.org/3.12/library/faulthandler.html), Python 3.12 Standard Library. Runtime traceback diagnostics for faults and hangs.
35. Python Software Foundation, [<code>tracemalloc</code>—Trace Memory Allocations](https://docs.python.org/3.12/library/tracemalloc.html), Python 3.12 Standard Library. Allocation snapshots, traceback statistics, and comparison.
36. B. Beyer, C. Jones, J. Petoff, and N. R. Murphy, eds., *Site Reliability Engineering: How Google Runs Production Systems*, O’Reilly, 2016. Service indicators, objectives, monitoring, incident response, and operational engineering.
37. OpenTelemetry Authors, *OpenTelemetry Specification*. Normative telemetry data and API concepts for traces, metrics, logs, contexts, and propagation.
38. S. Chacon and B. Straub, *Pro Git*, 2nd ed., Apress, 2014. Distributed workflows and Git’s object, reference, and branch model.
39. Git Project, [*gitglossary*](https://git-scm.com/docs/gitglossary). Normative terminology for objects, references, index, working tree, and revision graph.
40. Git Project, [*gitrepository-layout*](https://git-scm.com/docs/gitrepository-layout). Repository and per-worktree administrative layout.
41. Git Project, [*gitrevisions*](https://git-scm.com/docs/gitrevisions). Revision naming, ancestry, ranges, and set notation.
42. Git Project, [*git-merge*](https://git-scm.com/docs/git-merge). Fast-forward, merge commits, strategies, conflicts, and state.
43. Git Project, [*git-rebase*](https://git-scm.com/docs/git-rebase). Replay semantics, interactive transformations, conflicts, and recovery.
44. Git Project, [*git-bisect*](https://git-scm.com/docs/git-bisect). Binary history search, automated predicates, skips, and exit-status protocol.
45. Git Project, [*git-reflog*](https://git-scm.com/docs/git-reflog). Local reference-log management and expiry.
46. Git Project, [*gitignore*](https://git-scm.com/docs/gitignore). Pattern sources, precedence, matching, and tracked-file limitation.
47. Git Project, [*git-reset*](https://git-scm.com/docs/git-reset) and [*git-revert*](https://git-scm.com/docs/git-revert). Authoritative distinction among reference/index/tree reset and history-preserving inverse commits.
48. G. van Rossum, B. Warsaw, and N. Coghlan, [PEP 8—Style Guide for Python Code](https://peps.python.org/pep-0008/). Primary Python style guidance and its scope.
49. D. Goodger and G. van Rossum, [PEP 257—Docstring Conventions](https://peps.python.org/pep-0257/). Primary conventions for docstring placement and form.
50. G. van Rossum, J. Lehtosalo, and Ł. Langa, [PEP 484—Type Hints](https://peps.python.org/pep-0484/). Foundational gradual-typing proposal for Python.
51. I. Levkivskyi, J. Lehtosalo, and Ł. Langa, [PEP 544—Protocols](https://peps.python.org/pep-0544/). Structural subtyping and protocol specification.
52. E. Smith, [PEP 561—Distributing and Packaging Type Information](https://peps.python.org/pep-0561/). Discovery and distribution of inline and stub typing information.
53. J. Gonzalez, E. Traut, and M. Salgado, [PEP 695—Type Parameter Syntax](https://peps.python.org/pep-0695/). Python 3.12 syntax and variance inference for type parameters and aliases.
54. Python Typing Council, [*Specification for the Python Type System*](https://typing.python.org/en/latest/spec/). Living normative typing specification separated from historical PEP documents.
55. Python Software Foundation, [<code>typing</code>—Support for Type Hints](https://docs.python.org/3.12/library/typing.html), Python 3.12 Standard Library. Runtime typing objects and versioned API documentation.
56. Mypy Project, [*Mypy Documentation*](https://mypy.readthedocs.io/en/stable/) and [*Configuration File Reference*](https://mypy.readthedocs.io/en/stable/config_file.html). Checker semantics, adoption, generics, protocols, stubs, and configuration.
57. M. Fowler and M. Foemmel, “Continuous Integration,” 2006. Influential account of frequent integration and automated self-testing builds.
58. J. Humble and D. Farley, *Continuous Delivery*, Addison-Wesley, 2010. Build pipelines, deployment automation, configuration, testing, and release patterns.
59. NIST, [*Secure Software Development Framework (SSDF) Version 1.1*](https://csrc.nist.gov/pubs/sp/800/218/final), SP 800-218, 2022. Risk-based practices for preparing, protecting, producing, and responding to software.
60. A. Coghlan and D. Stufft, [PEP 440—Version Identification and Dependency Specification](https://peps.python.org/pep-0440/). Normative Python distribution version and specifier rules.
61. T. Kluyver et al., [PEP 517—A Build-System Independent Format for Source Trees](https://peps.python.org/pep-0517/) and [PEP 518—Specifying Minimum Build System Requirements](https://peps.python.org/pep-0518/). Build front-end/back-end protocol and declarative build requirements.
62. Python Packaging Authority, [*Binary Distribution Format*](https://packaging.python.org/en/latest/specifications/binary-distribution-format/) and [*Source Distribution Format*](https://packaging.python.org/en/latest/specifications/source-distribution-format/). Current wheel and source-archive specifications.
63. Python Packaging Authority, [*PyPA Specifications*](https://packaging.python.org/en/latest/specifications/) and [*Writing Your pyproject.toml*](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/). Maintained packaging standards index and project metadata guidance.
64. T. Preston-Werner, [*Semantic Versioning 2.0.0*](https://semver.org/). Versioning rules contingent on a declared public API.
65. SLSA Community, [*SLSA Provenance Specification 1.2*](https://slsa.dev/spec/v1.2/provenance). Build provenance model and predicate.
66. SPDX Project, [*SPDX Specifications*](https://spdx.dev/use/specifications/). Standardised software-package, licence, security, and build information formats.

---
