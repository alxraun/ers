# c_sharp_clean_code_guidelines
* nature: coding_standard
* language: c_sharp
* focus: maintainability + readability + reliability

## solid_and_dry
* **single_responsibility_principle** (SRP)
    * definition: change_reason_count == 1
    * constraint: multiple_responsibilities -> cohesion_loss
* **open_closed_principle** (OCP)
    * extension: open
    * modification: closed
    * benefit: new_features !affect existing_tests
* **liskov_substitution_principle** (LSP)
    * subtype_substitution -> safe
    * constraint: child_behavior ~ parent_contract
* **interface_segregation_principle** (ISP)
    * interface_size -> small
    * strategy: fat_interface -> split -> specific_interfaces
* **dependency_inversion_principle** (DIP)
    * dependency -> abstractions
    * coupling -> low
* **dont_repeat_yourself** (DRY)
    * duplication -> error_prone
    * solution: abstraction

## classes
* **fluent_interfaces**
    * technique: method_chaining
    * result: expressiveness + readability
* **relationship_preference**
    * **composition** (`has-a`) > **inheritance** (`is-a`)
    * reason: coupling_reduction

## functions
* **side_effects**
    * goal: avoid
    * flow: input -> output
    * mutation: global_state | parameters -> null
* **conditionals**
    * polarity: negative -> avoid
    * strategy: polymorphism > {`if/else`, `switch`}
    * encapsulation: complex_boolean -> method | property
* **type_safety**
    * type_checking -> avoid
    * alternatives: {polymorphism, pattern_matching}
    * correctness: system_enforced
* **parameters**
    * flags: boolean -> forbidden => split_method
    * quantity: `<= 2`
    * quantity > 2 => action: consolidate -> parameter_object
    * defaults: default_arguments > short_circuiting
* **structure**
    * scope: global_state_write -> forbidden
    * responsibility: one_thing
    * abstraction_level: single
    * locality: caller_callee_proximity -> vertical_close
* **naming**
    * style: specific + clear

## variables
* **control_flow**
    * nesting: deep -> avoid
    * strategy: guard_clauses (return_early)
* **naming_conventions**
    * **mental_mapping**: avoid -> explicit_names
    * **magic_values**: {strings, numbers} -> {constants, enums}
    * **context**: redundancy -> avoid
    * **vocabulary**: consistent_per_type
    * **searchability**: generic_names (`data`) -> avoid
* **clarity**
    * explanatory_variables: complex_expressions -> named_intermediates
    * attributes: meaningful + pronounceable

## objects_and_data_structures
* **properties**
    * access: getters + setters
    * role: logic_control + validation
* **encapsulation**
    * visibility: private | protected
    * exposure: minimal

## error_handling
* **exceptions**
    * caught_errors: swallow -> forbidden
    * action: log | notify
* **filtering**
    * strategy: specific_catch_blocks > generic_catch_with_if
* **rethrowing**
    * syntax: `throw;`
    * anti_pattern: `throw ex;`
    * reason: stack_trace_preservation
