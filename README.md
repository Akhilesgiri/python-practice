# Python Practice

Welcome to my Python practice repository.

This repository contains a full Python learning path, covering beginner fundamentals, core programming concepts, object-oriented programming, advanced Python, backend development, FastAPI, databases, and practical mini projects.

---

# Topics Covered

## Python Basics
- Hello World
- Variables
- Data Types
- Type Conversion
- Input & Output
- Comments
- Naming Conventions
- Indentation
- Multiple Assignment
- Constants
- Docstrings
- Type Annotations
- Mutable vs Immutable
- Truthy/Falsy
- None

## Operators
- Arithmetic
- Assignment
- Comparison
- Logical
- Bitwise
- Membership
- Identity
- Operator Precedence
- Ternary Operator

## Strings
- Creation
- Indexing
- Slicing
- String Methods
- Formatting
- f-Strings
- Escape Characters
- String Encoding
- Regular Expressions

## Data Structures
- Lists
- Tuples
- Sets
- Dictionaries
- Dictionary Comprehension
- List Comprehension
- Nested Data Structures
- Unpacking
- Shallow vs Deep Copy
- Set Comprehension

## Conditions & Loops
- If / Else / Elif
- Nested Conditions
- Match Case
- For Loops
- While Loops
- Range
- Break / Continue / Pass
- Enumerate / Zip
- Nested Loops
- For-Else / While-Else

## Functions
- Function Basics
- Parameters
- Return Values
- Default Arguments
- *args / **kwargs
- Lambda Functions
- Scope
- Closures
- Recursion
- First-Class Functions
- Higher-Order Functions
- Function Annotations
- Partial Functions
- Callable Objects

## Object-Oriented Programming
- Classes & Objects
- Constructors
- Instance & Class Variables
- Inheritance
- Polymorphism
- Encapsulation
- Abstraction
- Magic Methods
- Data Classes
- Properties
- Static & Class Methods
- Multiple Inheritance
- MRO
- Composition
- Abstract Base Classes
- Protocols

## File Handling
- Read / Write / Append
- JSON
- CSV
- Binary Files
- Pickle
- Pathlib
- OS Module

## Exceptions
- Try / Except
- Multiple Exceptions
- Else / Finally
- Raise
- Custom Exceptions
- Assert
- Exception Chaining
- Custom Error Messages

## Modules & Packages
- Imports
- Custom Modules
- Packages
- Virtual Environments
- Pip
- `__name__`
- Sys Module
- OS Module
- Datetime Module
- Virtualenv vs venv

## Advanced Python
- Iterators
- Generators
- Decorators
- Context Managers
- Typing
- Collections
- itertools
- functools
- Async / Await
- Threading
- Multiprocessing
- asyncio
- concurrent.futures
- Descriptors
- Metaclasses
- Memory Management
- Slots
- Garbage Collection
- Weak References
- LRU Cache
- ContextVars

## Problem Solving
- Patterns
- Arrays
- Strings
- Hashing
- Two Pointers
- Sliding Window
- Stack
- Queue
- Binary Search
- Linked List
- Trees
- Graphs
- Heap
- Backtracking
- Dynamic Programming
- Greedy Algorithms
- Interview Questions

## Backend & FastAPI
- HTTP / HTTPS
- REST APIs
- CRUD
- Authentication
- Authorization
- API Design
- FastAPI Installation
- Path & Query Parameters
- Request Body
- Response Models
- Pydantic
- Dependency Injection
- Middleware
- Authentication
- Database Integration

## Database
- SQL Basics
- Constraints
- Joins
- Group By
- Subqueries
- Indexes
- Views
- Transactions
- PostgreSQL
- SQLAlchemy
- Alembic

---

# Repository Structure

```text
python-practice/
├── .gitignore
├── LICENSE
├── README.md
├── REPO_STRUCTURE.md
├── requirements.txt
├── 01_python_basics/
│   ├── 01_hello_world.py
│   ├── 02_variables.py
│   ├── 03_datatypes.py
│   ├── 04_type_conversion.py
│   ├── 05_input_output.py
│   ├── 06_comments.py
│   ├── 07_keywords.py
│   ├── 08_indentation.py
│   ├── 09_naming_conventions.py
│   ├── 10_multiple_assignment.py
│   ├── 11_constants.py
│   ├── 12_docstrings.py
│   ├── 13_type_annotations.py
│   ├── 14_mutable_vs_immutable.py
│   ├── 15_truthy_falsy.py
│   ├── 16_none.py
│   ├── exercises.py
│   └── README.md
├── 02_operators/
│   ├── 01_arithmetic.py
│   ├── 02_assignment.py
│   ├── 03_comparison.py
│   ├── 04_logical.py
│   ├── 05_bitwise.py
│   ├── 06_membership.py
│   ├── 07_identity.py
│   ├── 08_operator_precedence.py
│   ├── 09_ternary_operator.py
│   ├── exercises.py
│   └── README.md
├── 03_strings/
│   ├── 01_string_creation.py
│   ├── 02_indexing.py
│   ├── 03_slicing.py
│   ├── 04_string_methods.py
│   ├── 05_formatting.py
│   ├── 06_f_strings.py
│   ├── 07_escape_characters.py
│   ├── 08_string_encoding.py
│   ├── 09_regular_expressions.py
│   ├── exercises.py
│   └── README.md
├── 04_data_structures/
│   ├── 01_lists.py
│   ├── 02_tuples.py
│   ├── 03_sets.py
│   ├── 04_dictionaries.py
│   ├── 05_list_comprehension.py
│   ├── 06_dictionary_comprehension.py
│   ├── 07_nested_data_structures.py
│   ├── 08_unpacking.py
│   ├── 09_shallow_vs_deep_copy.py
│   ├── 10_set_comprehension.py
│   ├── exercises.py
│   └── README.md
├── 05_conditions/
│   ├── 01_if.py
│   ├── 02_if_else.py
│   ├── 03_elif.py
│   ├── 04_nested_if.py
│   ├── 05_match_case.py
│   ├── exercises.py
│   └── README.md
├── 06_loops/
│   ├── 01_for_loop.py
│   ├── 02_while_loop.py
│   ├── 03_range.py
│   ├── 04_break_continue_pass.py
│   ├── 05_enumerate.py
│   ├── 06_zip.py
│   ├── 07_nested_loops.py
│   ├── 08_for_else.py
│   ├── 09_while_else.py
│   ├── exercises.py
│   └── README.md
├── 07_functions/
│   ├── 01_function_basics.py
│   ├── 02_parameters.py
│   ├── 03_return_values.py
│   ├── 04_default_arguments.py
│   ├── 05_args.py
│   ├── 06_kwargs.py
│   ├── 07_lambda.py
│   ├── 08_scope.py
│   ├── 09_closures.py
│   ├── 10_recursion.py
│   ├── 11_first_class_functions.py
│   ├── 12_higher_order_functions.py
│   ├── 13_function_annotations.py
│   ├── 14_partial_functions.py
│   ├── 15_callable.py
│   ├── exercises.py
│   └── README.md
├── 08_oops/
│   ├── 01_classes_objects.py
│   ├── 02_constructor.py
│   ├── 03_instance_class_variables.py
│   ├── 04_inheritance.py
│   ├── 05_polymorphism.py
│   ├── 06_encapsulation.py
│   ├── 07_abstraction.py
│   ├── 08_magic_methods.py
│   ├── 09_dataclasses.py
│   ├── 10_property.py
│   ├── 11_static_method.py
│   ├── 12_class_method.py
│   ├── 13_multiple_inheritance.py
│   ├── 14_method_resolution_order.py
│   ├── 15_composition.py
│   ├── 16_abstract_base_classes.py
│   ├── 17_protocols.py
│   ├── exercises.py
│   └── README.md
├── 09_file_handling/
│   ├── 01_read_file.py
│   ├── 02_write_file.py
│   ├── 03_append_file.py
│   ├── 04_json.py
│   ├── 05_csv.py
│   ├── 06_binary_files.py
│   ├── 07_pickle.py
│   ├── 08_pathlib.py
│   ├── 09_os_module.py
│   ├── exercises.py
│   └── README.md
├── 10_exception_handling/
│   ├── 01_try_except.py
│   ├── 02_multiple_exceptions.py
│   ├── 03_else_finally.py
│   ├── 04_raise.py
│   ├── 05_custom_exceptions.py
│   ├── 06_assert.py
│   ├── 07_exception_chaining.py
│   ├── 08_custom_error_messages.py
│   ├── exercises.py
│   └── README.md
├── 11_modules_packages/
│   ├── 01_imports.py
│   ├── 02_custom_modules.py
│   ├── 03_packages.py
│   ├── 04_virtual_environment.py
│   ├── 05_pip.py
│   ├── 06___name__.py
│   ├── 07_sys_module.py
│   ├── 08_os_module.py
│   ├── 09_datetime_module.py
│   ├── 10_virtualenv_vs_venv.py
│   ├── exercises.py
│   └── README.md
├── 12_advanced_python/
│   ├── 01_iterators.py
│   ├── 02_generators.py
│   ├── 03_decorators.py
│   ├── 04_context_managers.py
│   ├── 05_typing.py
│   ├── 06_collections_module.py
│   ├── 07_itertools.py
│   ├── 08_functools.py
│   ├── 09_pathlib.py
│   ├── 10_async_await.py
│   ├── 11_threading.py
│   ├── 12_multiprocessing.py
│   ├── 13_asyncio.py
│   ├── 14_concurrent_futures.py
│   ├── 15_descriptors.py
│   ├── 16_metaclasses.py
│   ├── 17_memory_management.py
│   ├── 17_slots.py
│   ├── 18_gc.py
│   ├── 19_weakref.py
│   ├── 20_lru_cache.py
│   ├── 21_contextvars.py
│   ├── exercises.py
│   └── README.md
├── 13_problem_solving/
│   ├── 01_easy.py
│   ├── 01_patterns.py
│   ├── 02_arrays.py
│   ├── 02_medium.py
│   ├── 03_hard.py
│   ├── 03_strings.py
│   ├── 04_hashing.py
│   ├── 04_patterns.py
│   ├── 05_two_pointers.py
│   ├── 06_sliding_window.py
│   ├── 07_stack.py
│   ├── 08_queue.py
│   ├── 09_binary_search.py
│   ├── 10_linked_list.py
│   ├── 11_trees.py
│   ├── 12_graphs.py
│   ├── 13_heap.py
│   ├── 14_backtracking.py
│   ├── 15_dynamic_programming.py
│   ├── 16_greedy.py
│   ├── 17_interview_questions.py
│   ├── exercises.py
│   └── README.md
├── 14_backend_basics/
│   ├── 01_http.py
│   ├── 02_https.py
│   ├── 03_rest_api.py
│   ├── 05_crud.py
│   ├── 06_authentication.py
│   ├── 07_authorization.py
│   ├── 08_api_design.py
│   ├── exercises.py
│   └── README.md
├── 15_fastapi/
│   ├── 01_installation.py
│   ├── 02_first_api.py
│   ├── 03_path_parameters.py
│   ├── 04_query_parameters.py
│   ├── 05_request_body.py
│   ├── 06_response_models.py
│   ├── 07_pydantic.py
│   ├── 08_dependency_injection.py
│   ├── 09_middleware.py
│   ├── 10_authentication.py
│   ├── 11_database.py
│   ├── exercises.py
│   ├── README.md
│   └── project/
│       └── README.md
├── 16_database/
│   ├── 01_sql_basics.sql
│   ├── 02_constraints.sql
│   ├── 03_joins.sql
│   ├── 04_group_by.sql
│   ├── 05_subqueries.sql
│   ├── 06_indexes.sql
│   ├── 07_views.sql
│   ├── 08_transactions.sql
│   ├── 09_postgresql.py
│   ├── 10_sqlalchemy.py
│   ├── 11_alembic.py
│   ├── exercises.py
│   └── README.md
├── interview_questions/
│   ├── advanced_python.md
│   ├── backend.md
│   ├── data_structures.md
│   ├── database.md
│   ├── fastapi.md
│   ├── functions.md
│   ├── oops.md
│   ├── operators.md
│   ├── python_basics.md
│   └── strings.md
├── mini_projects/
│   ├── banking_system/
│   │   └── README.md
│   ├── calculator/
│   │   └── README.md
│   ├── contact_book/
│   │   └── README.md
│   ├── expense_tracker/
│   │   └── README.md
│   ├── inventory_management/
│   │   └── README.md
│   ├── library_management/
│   │   └── README.md
│   ├── student_management/
│   │   └── README.md
│   ├── todo_cli/
│   │   └── README.md
│   ├── url_shortener/
│   │   └── README.md
│   └── weather_cli/
│       └── README.md
└── notes/
    ├── advanced_python.md
    ├── backend_basics.md
    ├── conditions.md
    ├── data_structures.md
    ├── database.md
    ├── exception_handling.md
    ├── fastapi.md
    ├── file_handling.md
    ├── functions.md
    ├── loops.md
    ├── modules_packages.md
    ├── oops.md
    ├── operators.md
    ├── python_basics.md
    └── strings.md
```
- Build a complete Python learning path from beginner to advanced
- Practice backend and API development with FastAPI
- Solve real-world problems with algorithms and data structures
- Create reusable Python portfolio projects
- Prepare for technical interviews and software engineering careers
