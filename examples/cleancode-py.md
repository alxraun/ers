# python_clean_code_guidelines
* nature: coding_standard
* language: python
* focus: maintainability + readability

## classes
* **single_responsibility_principle** (SRP)
    * definition: change_reason_count == 1
* **open_closed_principle** (OCP)
    * extension: open
    * modification: closed
* **liskov_substitution_principle** (LSP)
    * base_class + subclass -> interchangeable
    * constraint: parent_contract !broken
* **interface_segregation_principle** (ISP)
    * interface_size -> small
    * result: client_dependency !excessive
* **dependency_inversion_principle** (DIP)
    * dependency -> abstractions
    * dependency !concrete_implementations

## functions
* **arguments**
    * quantity: `<= 2`
    * quantity > 2 => action: group -> {class | data_structure}
    * implication: many_args ~ function_doing_too_much
* **responsibility**
    * rule: do_one_thing
    * benefits: {easier_testing, composition, reasoning}
* **naming**
    * requirement: specific
    * anti_pattern: {`handle`, `process`}
* **flags**
    * boolean_parameter -> forbidden
    * implication: flag_presence => function_tasks > 1
    * solution: split_function
* **side_effects**
    * goal: avoid
    * ideal_flow: input -> output
    * constraint: external_state_modification -> null
* **abstraction_levels**
    * per_function: 1
    * high_logic + low_details => complexity
    * solution: decompose -> {reusability, easier_testing}

## variables
* **names**
    * properties: {meaningful, pronounceable}
    * anti_pattern: abbreviations
* **searchability**
    * magic_numbers | strings -> avoid
    * storage -> well_named_constants
* **explanatory_variables**
    * use_case: complex_expressions (e.g. regex)
    * action: break_down -> named_variables
* **mental_mapping**
    * generic_names: {`item`, `seq`} -> forbidden
    * requirement: explicit_names
* **context**
    * class_context_exists => variable_name_repetition -> redundant

## common
* **dry** (don't_repeat_yourself)
    * duplicate_code -> avoid
    * solution: abstractions
