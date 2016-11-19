# secret-santa-generator
Every year my mom and I are responsible of the raffle to the family's Secret Santa, because we are coders. Usually we just do it manually and pretend we programmed it. This year we may actually do things right.

# Version 1.0

It should only receive the names of the family members in a file and return a list, which is circular:
```
[ Person1, Person2, Person3]
```
It means _Person2_ is the Secret Santa gift recipient of _Person1_, _Person3_ is the Secret Santa gift recipient of _Person2_, and _Person1_ is the Secret Santa gift recipient of _Person3_.

As my family has some constraints, such _as husband and wife can't give presents to each other_, you can give a file of constraints, where you separate in groups (separated by a blank line) the people who cannot be secret santa of each other. 

To use:

```
python generator2.py <members_list_filename> <constraints_list_filename>
```

