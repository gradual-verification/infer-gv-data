- butterknife
  - Only missing in _eradicate_:
    - butterknife-lint/src/main/java/butterknife/lint/InvalidR2UsageDetector.java:104
      - **Negative:** The code checks the variable beforehand using
        `instanceof`, which [prevents a null dereference][instanceof].
- skaffold-tools-for-java
  - Only present in _gradual_:
    - skaffold-plugins-core/src/main/java/com/google/cloud/tools/skaffold/command/Skaffold.java:189
      - **Negative:** The path being dereferenced is a field which is checked
        for null beforehand, but gradual doesn't update field lattice values.

[instanceof]: https://stackoverflow.com/a/2950415/5044950
