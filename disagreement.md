- AutoDispose:
  - Only present in gradual:
    - sample/src/main/java/com/uber/autodispose/recipes/AutoDisposeView.java:90
      - **Negative:** The path being dereferenced is a field which is checked
        for null beforehand, but gradual doesn't update field lattice values.
    - sample/src/main/java/com/uber/autodispose/recipes/AutoDisposeView.java:97
      - **Negative:** The path being dereferenced is a field which is checked
        for null beforehand, but gradual doesn't update field lattice values.
- butterknife
  - Only missing in _eradicate_:
    - butterknife-lint/src/main/java/butterknife/lint/InvalidR2UsageDetector.java:104
      - **Negative:** The code checks the variable beforehand using
        `instanceof`, which [prevents a null dereference][instanceof].
- filesystem-generator:
  - Only present in eradicate:
    - src/test/java/de/zuellich/fsgenerator/FSGeneratorTest.java:13
      - **Negative:** The two fields aren't initialized in a constructor, but
        there is a specially marked `@Before` method that initializes them.
- skaffold-tools-for-java
  - Only present in _gradual_:
    - skaffold-plugins-core/src/main/java/com/google/cloud/tools/skaffold/command/Skaffold.java:189
      - **Negative:** The path being dereferenced is a field which is checked
        for null beforehand, but gradual doesn't update field lattice values.

[instanceof]: https://stackoverflow.com/a/2950415/5044950
