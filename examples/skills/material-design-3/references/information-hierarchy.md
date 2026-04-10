# MODULE: INFORMATION_HIERARCHY
* domain: m3_semiotics_and_typography
* nature: architectural_communication_laws
* context: content_structure + symbolic_alignment
* goal: guarantee_readability + express_brand + establish_hierarchy

# CORE_AXIOMS
* unit: `sp` == scale_independent_pixel [Android_Standard]
* unit: `rem` == root_em [Web_Standard]
* conversion: `16sp` == `1rem`
* base_anchor: `Body_Medium` == `14sp`
* scale_ratio: `Major_Second` [1.125]
* logic: `size_n` == `base_anchor` * (1.125 ^ n)

# MATHEMATICAL_TYPE_SCALE
* role: defining_proportional_consistency
* state_space: {DISPLAY, HEADLINE, TITLE, BODY, LABEL}
* variants: {SMALL, MEDIUM, LARGE}
* status: baseline | emphasized [2025_update]

## ROLE: DISPLAY [Expressive]
* usage: {hero_numbers, splash_screens, large_expressive_headers}
* font_weight: `400` [Baseline] | `600` [Emphasized]
* line_height_ratio: 1.1 -> 1.2
* sizes:
  * Large: `57sp`
  * Medium: `45sp`
  * Small: `36sp`

## ROLE: HEADLINE [Sectional]
* usage: {page_headers, major_content_regions}
* font_weight: `400` [Baseline] | `600` [Emphasized]
* sizes:
  * Large: `32sp`
  * Medium: `28sp`
  * Small: `24sp`

## ROLE: TITLE [Component]
* usage: {card_headers, dialog_titles, list_subheaders}
* font_weight: `500` [Medium] | `700` [Bold]
* sizes:
  * Large: `22sp`
  * Medium: `16sp`
  * Small: `14sp`

## ROLE: BODY [Reading]
* usage: {long_form_text, descriptions, user_input}
* font_weight: `400` [Regular]
* line_height_ratio: 1.5 [Required_for_readability]
* sizes:
  * Large: `16sp`
  * Medium: `14sp`
  * Small: `12sp`

## ROLE: LABEL [Utilitarian]
* usage: {button_text, chip_text, navigation_labels}
* font_weight: `500` [Medium]
* sizes:
  * Large: `14sp`
  * Medium: `12sp`
  * Small: `11sp`

# VARIABLE_FONT_AXES [DYNAMIC_EXPRESSION]
* role: manual_tuning_of_weight_and_grade
* target: {Roboto_Flex, Google_Sans_Flex}

## AXIS: WEIGHT [wght]
* range: `100` -> `900`
* baseline: `400`
* emphasis: `600` | `700`
* logic: scale_weight_up as size decreases [Compensation]

## AXIS: GRADE [GRAD]
* nature: optical_weight_without_reflow
* logic: change_thickness !affecting_character_width
* use_case: dark_mode_bleed_compensation
  * Dark_mode => `grad`: `-25` [reduce_glow_blur]
  * Interaction_highlight => `grad`: `+150` [increase_presence]

## AXIS: WIDTH [wdth]
* range: `25` -> `151`
* logic: narrow_width => usage: {navigation_rail, condensed_labels}

## AXIS: OPTICAL_SIZE [opsz]
* logic: `opsz` == `font_size`
* effect:
  * low_opsz => increased_x_height + thicker_thins [Readability]
  * high_opsz => refined_details + high_contrast_strokes [Aesthetics]

# SYMBOLIC_SYSTEM: MATERIAL_SYMBOLS
* nature: variable_icon_font
* styles: {OUTLINED, ROUNDED, SHARP}
* grid_base: `24dp` x `24dp`

## ICON_AXES
* `fill`: {0 | 1} => state: {unselected | selected}
* `weight`: `100` -> `700` [default: 400]
* `grade`: `-25` -> `200`
* `optical_size`: `20dp`, `24dp`, `40dp`, `48dp`

## ICON_OPTICAL_LAWS
* alignment: centered_in_bounding_box
* baseline_shift: `icon_y` -> move_down -> `11.5%` of `text_font_size` [Optical_Centering_with_Text]
* matching: `icon_weight` ~ matches ~ `text_weight`
* sizing:
  * compact_ui => `20dp` [opsz]
  * standard_ui => `24dp` [opsz]
  * hero_moments => `40dp` | `48dp` [opsz]

# READABILITY_LAWS [MANUAL_TYPESETTING]
* law[line_length]: ideal == `40` -> `60` characters_per_line
* law[line_height]:
  * Display/Headline => `1.2 * font_size`
  * Body/Label => `1.5 * font_size`
* law[letter_spacing]:
  * large_titles => `-0.25sp` [Tighter]
  * small_labels => `+0.1sp` -> `+0.5sp` [Looser]
* law[tabular_nums]: usage: {clocks, timers, data_tables}
  * font_variant: `tabular-nums` [monospaced_digits]

# CONTENT_CHOREOGRAPHY
* rule[sentence_case]: "Only the first letter is capitalized"
  * applies_to: {titles, buttons, labels}
* rule[anti_all_caps]: "Do not use ALL CAPS for UI text" [Accessibility_Failure]
* rule[consequence_first]: "Summarize action result at the start of the sentence"
* rule[pronoun_consistency]:
  * usage: "You" / "Your" [Second_person]
  * avoid: "I" / "My" [except_legal_agreements]

# ACCESSIBILITY_MARKUP_LOGIC
* element[interactive_icon] => needs => `aria-label` [Action_Description]
* element[decorative_image] => needs => `alt=""` [Hide_from_AT]
* element[chart] => needs => `alt="Summary + Key Takeaway"`
* hierarchy[headings]:
  * H1 => one_per_page
  * structure => !skip_levels [H2 -> H4 == FORBIDDEN]
