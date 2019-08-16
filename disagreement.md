Negative
--------

- _assigned field_: The path being dereferenced is a field which is assigned a
  non-null value beforehand, but gradual doesn't update field lattice values.
- _checked call_: The return value of a probably-referentially-transparent call
  is checked before usage.
- _checked field_: The path being dereferenced is a field which is checked for
  null beforehand, but gradual doesn't update field lattice values.
- _checked instanceof_: The code checks the variable beforehand using
  `instanceof`, which [prevents a null dereference][instanceof].
- _complicated check_: The variable is safe, but for complicated control-flow
  reasons.
- _eradicate parameter_: Eradicate seems to give tons of false positives about
  passing parameters so I'm just gonna start ignoring these.
- _eradicate test_: Eradicate seems to give tons of false positives in tests so
  I'm just gonna start ignoring these.
- _fine inconsistent annotation_: An overridden annotation is marked as
  inconsistent, but it isn't used in an unsafe way.
- _generated code_: A warning in non-source code.
- _initialized elsewhere_: The two fields aren't initialized in a constructor,
  but there is a specially marked `@Before` method that initializes them.
- _missing annotation_: A field is checked for null, or a method returns null,
  so nullsafe insists that it be annotated as `@Nullable`.
- _phantom code_: Warning about some code that's not there.
- _safe return_: Warning about a non-null return value.
- _unstrict field_: A field that allows null is appraised as non-null.
- _unstrict parameter_: A parameter that allows null is appraised as non-null.
- _unstrict return_: A return value that allows null is appraised as non-null
  (e.g. for overriding).

Positive
--------

- _unchecked field_: The field is marked as `@Nullable` and not checked.
- _unchecked call_: The return value of a call is marked as `@Nullable` and not
  checked.

[instanceof]: https://stackoverflow.com/a/2950415/5044950
