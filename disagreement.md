Negative
--------

- _checked field_: The path being dereferenced is a field which is checked for
  null beforehand, but gradual doesn't update field lattice values.
- _checked instanceof_: The code checks the variable beforehand using
  `instanceof`, which [prevents a null dereference][instanceof].
- _initialized elsewhere_: The two fields aren't initialized in a constructor,
  but there is a specially marked `@Before` method that initializes them.

[instanceof]: https://stackoverflow.com/a/2950415/5044950
