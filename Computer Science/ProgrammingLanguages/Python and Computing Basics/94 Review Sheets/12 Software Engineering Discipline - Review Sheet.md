# 12.24 Common misconceptions consolidated

1. **“Testing proves there are no bugs.”** Tests supply finite evidence for named claims and cases.
2. **“Unit tests use mocks; integration tests use real objects.”** Scope and boundary purpose define the level; double choice is secondary.
3. **“More coverage means better tests.”** Coverage reports execution, not oracle quality.
4. **“Mocks isolate code and therefore improve design.”** They can also couple tests to internal calls and hide real integration semantics.
5. **“Debugging means changing code until output changes.”** It is hypothesis testing around the earliest divergence.
6. **“Git stores diffs.”** Its core object model stores content-addressed snapshots/trees with parent relationships, while diff is a derived comparison.
7. **“`.gitignore` removes secrets from Git.”** It affects untracked selection, not existing objects or copies.
8. **“PEP 8 compliance means good code.”** Style aids reading; contracts, names, algorithms, and architecture determine deeper quality.
9. **“Type hints validate runtime input.”** They guide tools and readers; external data still requires runtime parsing and validation.
10. **“CI is a remote test button.”** It reconstructs and evaluates change under a controlled integration policy.
