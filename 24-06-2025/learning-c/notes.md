# C programming notes

Let’s build up your understanding of the **C programming language** from the ground up. C is a powerful and foundational language, often considered the "mother of all modern languages" because many other languages (like C++, Java, and even Python) are influenced by it.

---

## 🔰 1. What Is C?

C is a **general-purpose**, **procedural**, and **low-level** programming language developed in the **early 1970s** by **Dennis Ritchie** at **Bell Labs**. It was originally created to implement the UNIX operating system.

### Why Learn C?

- It's **fast** and gives you **low-level memory access**.
- It teaches you how computers actually work.
- It's used in **operating systems**, **embedded systems**, **compilers**, **drivers**, and more.

---

## 🧱 2. Basics of a C Program

Here’s a simple C program:

```c
#include <stdio.h>

int main() {
    printf("Hello, world!\n");
    return 0;
}
```

### Breakdown:

- `#include <stdio.h>` – Includes the Standard Input Output library.
- `int main()` – Entry point of the program.
- `printf()` – Function to print text.
- `return 0;` – Indicates successful program termination.

---

## 🧠 3. Key Concepts

### 📌 Variables & Data Types

Variables store data. C is **statically typed**, so you must declare types.

```c
int age = 25;
float weight = 70.5;
char grade = 'A';
```

### 📌 Operators

- Arithmetic: `+`, `-`, `*`, `/`, `%`
- Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Logical: `&&`, `||`, `!`

---

### 📌 Control Flow

#### `if`, `else`, `else if`

```c
if (age > 18) {
    printf("Adult\n");
} else {
    printf("Minor\n");
}
```

#### `for`, `while`, `do-while`

```c
for (int i = 0; i < 5; i++) {
    printf("%d\n", i);
}
```

---

## 🔄 4. Functions

Functions allow code reuse.

```c
int add(int a, int b) {
    return a + b;
}

int main() {
    int result = add(3, 4);
    printf("Sum is %d\n", result);
}
```

---

## 🧱 5. Arrays and Strings

### Arrays

```c
int numbers[5] = {1, 2, 3, 4, 5};
```

### Strings (character arrays)

```c
char name[] = "Alice";
printf("%s", name);
```

---

## 📦 6. Pointers

Pointers store memory addresses.

```c
int x = 10;
int *p = &x;
printf("%d", *p);  // Outputs 10
```

Understanding pointers is key in C, especially for arrays, functions, and memory management.

---

## 🗃️ 7. Structures

Used to group variables of different types.

```c
struct Person {
    char name[50];
    int age;
};

struct Person p1 = {"Alice", 30};
```

---

## 🔧 8. Memory Management

Manual memory handling using:

- `malloc()` – allocate memory
- `free()` – deallocate memory

```c
int *ptr = malloc(sizeof(int) * 5);
free(ptr);
```

---

## 🧰 9. File Handling

C supports file operations:

```c
FILE *f = fopen("data.txt", "r");
fscanf(f, "%s", buffer);
fclose(f);
```

---

## 🧪 10. Compilation & Execution

C is compiled using tools like **GCC**.

```bash
gcc program.c -o program
./program
```

---

## 🔚 In Summary

| Concept           | Description                              |
| ----------------- | ---------------------------------------- |
| **Low-level**     | Close to hardware                        |
| **Compiled**      | Translated before execution              |
| **Fast**          | Excellent for performance-critical tasks |
| **Manual memory** | No garbage collection                    |
| **Portable**      | Works on various systems                 |

---
