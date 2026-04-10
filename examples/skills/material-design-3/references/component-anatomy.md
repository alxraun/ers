# MODULE: MORPHOLOGICAL_GEOMETRY
* domain: m3_physical_form
* nature: geometric_and_structural_specs
* context: manual_component_construction
* unit: `dp` [density_independent_pixel]

# SHAPE_SCALE_SYSTEM
* role: defining_containment_style
* logic: size_independent_roundedness
* types: {ROUNDED, CUT}
* status: rounded == default

## THE_TEN_LEVEL_SCALE
* `corner_none`: `0dp` => usage: {full_screen_views, tiled_grids}
* `corner_extra_small`: `4dp` => usage: {snackbars, menu_items, text_fields}
* `corner_small`: `8dp` => usage: {chips, tooltips, selection_controls}
* `corner_medium`: `12dp` => usage: {cards, small_dialogs}
* `corner_large`: `16dp` => usage: {modal_navigation_drawer, standard_fab}
* `corner_large_increased`: `20dp` => usage: {custom_hero_cards}
* `corner_extra_large`: `28dp` => usage: {dialogs, large_fab}
* `corner_extra_large_increased`: `32dp` => usage: {large_modal_sheets}
* `corner_extra_extra_large`: `48dp` => usage: {giant_display_containers}
* `corner_full`: `9999px` => usage: {buttons, search_bar, badges}

# ELEVATION_SYSTEM
* nature: z_axis_hierarchy
* mechanism: {shadows | surface_tonal_overlay}
* logic: level -> mapped_to -> `dp_height`

## ELEVATION_LEVELS
* `level_0`: `0dp` => state: resting [non_elevated]
* `level_1`: `1dp` => usage: {cards_elevated, elevated_buttons_resting, modal_drawer}
* `level_2`: `3dp` => usage: {scrolled_app_bar, menu, toolbar}
* `level_3`: `6dp` => usage: {dialogs, fab, search_bar, date_pickers}
* `level_4`: `8dp` => usage: {hovered_fab, dragged_components}
* `level_5`: `12dp` => usage: {highest_priority_modals}

# SURFACE_TINT_GEOMETRY
* definition: color_based_elevation_cue
* logic: `surface_color` + `primary_color`[@`opacity`]
* mapping:
  * level_1 => 5% `primary`
  * level_2 => 8% `primary`
  * level_3 => 11% `primary`
  * level_4 => 12% `primary`
  * level_5 => 14% `primary`
* result: perceptual_depth without drop_shadows

# COMPONENT_ANATOMY: BUTTONS
* universal_height: `40dp`
* universal_shape: `corner_full`
* label_text_font: `label-large`

## BUTTON_VARIANTS
* **Filled**: `container_color` == `primary`, `elevation` == `level_0`
* **Elevated**: `container_color` == `surface_container_low`, `elevation` == `level_1`
* **Tonal**: `container_color` == `secondary_container`, `elevation` == `level_0`
* **Outlined**: `outline_color` == `outline`, `elevation` == `level_0`
* **Text**: `container_color` == `transparent`, `elevation` == `level_0`

## BUTTON_SPACING_INTERNAL
* `leading_space`: `24dp` [no_icon] | `16dp` [with_icon]
* `trailing_space`: `24dp` [no_icon] | `16dp` [with_trailing_icon]
* `icon_size`: `18dp`
* `icon_label_padding`: `8dp`

# COMPONENT_ANATOMY: INPUT_FIELDS
* container_shape: `corner_extra_small_top` [filled] | `corner_extra_small` [outlined]
* min_height: `56dp`
* active_indicator_height: `1px` [resting] | `3px` [focused]

## FIELD_INTERNAL_METRICS
* `leading_space`: `16dp`
* `trailing_space`: `16dp`
* `top_space`: `8dp` [with_label] | `16dp` [no_label]
* `bottom_space`: `8dp` [with_label] | `16dp` [no_label]
* `supporting_text_top_space`: `4dp`
* `outline_width`: `1px` [resting] | `3px` [focused]
* `outline_label_padding`: `4dp` [horizontal]

# COMPONENT_ANATOMY: CHIPS
* container_height: `32dp`
* container_shape: `corner_small` [`8dp`]
* label_text_font: `label-large`

## CHIP_INTERNAL_METRICS
* `leading_space`: `16dp`
* `trailing_space`: `16dp`
* `with_icon_leading_space`: `8dp`
* `icon_size`: `18dp`
* `icon_label_space`: `8dp`
* `avatar_size`: `24dp`

# COMPONENT_ANATOMY: CARDS
* container_shape: `corner_medium` [`12dp`]
* state[resting]: `elevation` == `level_0` [outlined/filled] | `level_1` [elevated]
* state[hover]: `elevation` == `level_1` [outlined/filled] | `level_2` [elevated]

# COMPONENT_ANATOMY: FAB
* type[small]: `size` == `40dp`, `icon` == `24dp`, `shape` == `corner_small`
* type[standard]: `size` == `56dp`, `icon` == `24dp`, `shape` == `corner_large`
* type[large]: `size` == `96dp`, `icon` == `36dp`, `shape` == `corner_extra_large`
* type[extended]: `height` == `56dp`, `label_padding` == `20dp`, `shape` == `corner_large`

# COMPONENT_ANATOMY: NAVIGATION
* **Navigation Bar**: `height` == `80dp`, `active_indicator_shape` == `corner_full`, `active_indicator_width` == `64dp`
* **Navigation Rail**: `width` == `80dp`, `active_indicator_shape` == `corner_full`
* **Navigation Drawer**: `width_modal` == `360dp`, `width_standard` == `240dp` -> `320dp`, `item_height` == `56dp`

# COMPONENT_ANATOMY: DIALOGS
* container_shape: `corner_extra_large` [`28dp`]
* padding_all: `24dp`
* icon_size: `24dp`
* headline_spacing_bottom: `16dp`

# OPTICAL_GEOMETRY_LAWS
* principle[optical_roundness]:
  * condition: nested_containers
  * rule: `outer_radius` - `padding` == `inner_radius`
  * example: `16dp` [outer] - `4dp` [padding] => `12dp` [inner]
* principle[baseline_shift]:
  * condition: icon_beside_text
  * rule: `icon_baseline` == `text_baseline` - 11.5% of `font_size`
* principle[touch_target_expansion]:
  * condition: visual_element < `48dp`
  * rule: invisible_target_area == `48dp` x `48dp`
