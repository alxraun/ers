# bash_clean_code_guidelines
* nature: coding_standard
* language: bash
* focus: robustness + maintainability + safety
* axiom: bash_is_systems_glue
* toolchain: shellcheck -> required

## structure_and_lifecycle
* **entry_point**
    * pattern: `main` function -> required
    * execution: `if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then main "$@"; fi`
    * benefit: testability + sourceability
* **safety_harness** (strict_mode)
    * configuration: `set -euo pipefail`
    * `set -e`: exit_on_error
    * `set -u`: nounset (undefined_vars -> error)
    * `set -o pipefail`: pipeline_error -> propagation
    * exception: intentional_failure => `cmd || true`
* **file_convention**
    * libraries: extension == `.sh` | `.bash`
    * executables: extension == null
    * shebang: `#!/bin/bash` (or `#!/usr/bin/env bash`)
    * permission: `SUID` | `SGID` -> forbidden

## functions
* **definition_style**
    * syntax: `my_func() { ... }`
    * keyword: `function` -> forbidden (portability_noise)
* **scope**
    * rule: global_pollution -> forbidden
    * declaration: `local` | `declare` -> required_inside_functions
    * exception: `readonly` constants
* **arguments**
    * naming: explicit_assignment_at_top
    * pattern: `local arg_name="$1"`
    * quantity: `> 3` => refactor | use_flags
* **return_values**
    * output: `stdout` (data)
    * status: `return code` (0-255)
    * error_msg: `stderr`

## variables_and_types
* **naming_convention**
    * local_variables: `snake_case`
    * functions: `snake_case`
    * constants: `UPPER_CASE`
    * environment_exports: `UPPER_CASE`
    * private/internal: `_snake_case`
* **quoting**
    * default: **double_quotes** `"$var"` -> always
    * reason: whitespace_safety + security
    * exceptions: `[[ ... ]]` (regex), arithmetic `(( ... ))`
* **interpolation**
    * preference: `${var}` > `$var`
    * benefit: boundary_clarity
* **arrays**
    * use_case: lists_of_items | command_arguments
    * expansion: `"${array[@]}"` -> preserves_quoting
    * anti_pattern: string_concatenation_for_lists
* **magic_values**
    * action: extract -> `readonly CONSTANT_NAME`

## syntax_and_operators
* **conditionals**
    * operator: `[[ ... ]]` > `[ ... ]`
    * benefit: safety + regex_support + logic_operators
    * numeric_comparison: `(( a > b ))` > `[[ $a -gt $b ]]`
    * emptiness: `[[ -z "$var" ]]` (empty) | `[[ -n "$var" ]]` (not_empty)
* **command_substitution**
    * syntax: `$( ... )` > `` `...` ``
    * benefit: nesting_readability
* **arithmetic**
    * syntax: `(( ... ))` | `$(( ... ))`
    * tools: `expr` | `let` -> obsolete
* **loops**
    * input_processing: `while read -r` > `for x in $(cat file)`
    * reason: whitespace_handling_correctness

## io_and_error_handling
* **streams**
    * info/data -> `stdout` (`&1`)
    * warnings/errors -> `stderr` (`&2`)
    * logging_function: `echo "..." >&2`
* **resource_management**
    * pattern: `mktemp` + `trap`
    * action: `trap 'rm -f "$tmpfile"' EXIT`
    * goal: auto_cleanup
* **path_resolution**
    * relative_paths: prefix with `./`
    * reliable_location: `$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)`
* **wildcards**
    * expansion: explicit_path `rm ./*` > `rm *`
    * safety: prevent_flag_injection

## performance_and_logic
* **process_spawning**
    * preference: builtins > external_binaries (sed/awk)
    * string_manipulation: `${var//pattern/replace}` > `sed`
* **pipelines**
    * formatting: split_multiline
    * operator: `|` (pipe) at_end_of_line
