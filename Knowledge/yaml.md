# Learning YAML

## Lesson 1: The Basics of YAML Syntax

Let’s start with the core concepts

### Key-Value Pairs

The simplest building block in YAML is a key-value pair. It’s written as `key: value`, with a colon and a space separating the key and value.

```yaml

name: Alice
age: 25
city: New York
```

`name`, `age`, and `city` are keys.
`Alice`, `25`, and `New York` are their values.

### Nesting (Hierarchy)

To show relationships, YAML uses indentation (spaces, not tabs—usually 2 spaces). This creates a hierarchy.

```yaml

person:
  name: Alice
  age: 25
  city: New York
```

`person` is a parent key.
`name`, `age`, and `city` are nested under it.

### Lists (Sequences)

Lists are represented with a hyphen (-) followed by a space. Each item in the list gets its own line.

```yaml
fruits:
  - Apple
  - Banana
  - Orange
```

`fruits` is the key.
`Apple`, `Banana`, and `Orange` are items in the list.

### Combining Lists and Key-Value Pairs

You can mix these together for more complex structures.
```yml
person:
  name: Alice
  hobbies:
    - Reading
    - Hiking
    - Cooking
```
`hobbies` is a list nested under `person`.

## Lesson 2 More YAML features

### Comments

You can add notes in YAML using the # symbol. Anything after # on a line is ignored by the parser.

```yml
student:
  name: Emma  # This is the student’s name
  age: 20     # Age in years
  favorite_subjects:
    - Math    # Great for problem-solving
    - Science
    - History
```

### Multi-line Strings

Sometimes you need to store longer text, like a description. YAML offers two ways:

- Block Style with `|`: Keeps newlines.
- Folded Style with `>`: Folds newlines into spaces.

```yml
student:
  name: Emma
  bio: |
    Emma is a curious student.
    She loves learning new things.
  motto: >
    Keep exploring and never
    stop asking questions.
```
- `bio` keeps the line breaks.
- `motto` becomes "Keep exploring and never stop asking questions." (one line).

### Multiple Documents in One File

You can separate YAML documents with `---` (three dashes).

```yml
---
student:
  name: Emma
  age: 20
---
student:
  name: Liam
  age: 22
```

This file has two separate YAML documents.

