# lua_clean_code_guidelines
* nature: coding_standard
* language: lua
* focus: maintainability + readability + performance

## naming_conventions
* **variables_and_functions**
    * style: `snake_case`
    * requirement: {meaningful, pronounceable}
* **factories**
    * style: `PascalCase`
    * use_case: table_instance_creation
* **booleans**
    * pattern: prefix {`is_`, `has_`}
* **searchability**
    * magic_values -> forbidden
    * solution: `named_constants`
* **context**
    * rule: redundant_repetition -> avoid
    * logic: `module_name` + `field_name` != `duplicate`
* **ignored_values**
    * syntax: `_`
    * use_case: unused_loop_variables

## formatting_and_syntax
* **indentation**
    * style: `2_spaces` (soft_tabs)
* **operators**
    * padding: `surround_with_spaces` (e.g., `+`, `-`, `=`, `..`)
* **statements**
    * semicolons: forbidden
    * separation: `newline`
* **strings**
    * quotes: `single_quotes` ('')
    * length > 80: break -> concatenation (`..`)
* **lists**
    * trailing_comma: discouraged
    * leading_comma: forbidden
* **file_structure**
    * termination: `final_newline` -> required

## variables
* **scope**
    * declaration: `local` -> mandatory
    * logic: global_namespace_pollution -> forbidden
    * visibility: `minimal_scope` (define near usage)
* **clarity**
    * complex_expressions -> `explanatory_variables`
    * mental_mapping -> forbidden => `explicit_names`

## functions
* **responsibility**
    * rule: do_one_thing
    * benefit: {testing, reuse, reasoning}
* **naming**
    * requirement: descriptive_intent
* **arguments**
    * quantity: `<= 2`
    * quantity > 2 => action: consolidate -> `table_parameter`
    * flag_arguments: forbidden => action: `split_function`
* **purity**
    * side_effects -> avoid
    * input_mutation -> forbidden
    * modification: return_copies > mutate_original
* **control_flow**
    * strategy: `early_return`
    * goal: nesting_reduction + validation_first
* **syntax**
    * preference: `local function name()` > `local name = function()`
    * table_methods: `self` -> required
    * organization: define_outside_literals -> assign_to_keys

## objects_and_tables
* **creation**
    * pattern: `constructor_syntax` (literal_initialization)
* **encapsulation**
    * access: {`getters`, `setters`}
    * visibility: `local` (private_members) @ module_level
* **architecture**
    * preference: **composition** > **inheritance**
* **member_access**
    * static_properties: `dot_notation` (`table.key`)
    * dynamic_properties: `bracket_notation` (`table[key]`)
* **length_operator** (`#`)
    * constraint: unreliable_on_sparse_tables
    * warning: `nil`_holes -> inaccurate_count

## conditionals
* **logic_polarity**
    * preference: `positive_conditions`
* **abstraction**
    * complex_logic -> `encapsulated_functions`
* **evaluation**
    * short_circuiting: `and` / `or` (e.g., `default_values`)
* **existence**
    * check: `if var then` (validates !`nil` && !`false`)

## modules
* **single_responsibility_principle** (SRP)
    * definition: 1_reason_to_change
* **loading**
    * `require` -> side_effect_free
    * constraint: global_state_modification -> forbidden
* **state_management**
    * classification: {`stateless_library` | `object_factory`}

## error_handling
* **strategy**
    * swallow_errors -> forbidden
    * expected_failures (I/O): return {`nil`, `error_message`}
    * programmer_errors: {`error()`, `assert()`} -> stop_execution

## type_conversion
* **casting**
    * style: explicit -> {`tostring()`, `tonumber()`}
    * implicit_coercion: forbidden
