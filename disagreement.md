- butterknife
  - Only missing in eradicate:
    - butterknife-lint/src/main/java/butterknife/lint/InvalidR2UsageDetector.java:104
      - The code checks the variable beforehand using `instanceof`, which
        [prevents a null dereference][instanceof].

[instanceof]: https://stackoverflow.com/a/2950415/5044950
