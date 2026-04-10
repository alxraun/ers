# MODULE: SPATIAL_LAYOUT
* domain: m3_physical_architecture
* nature: declarative_geometric_laws
* context: framework_agnostic_implementation

# CORE_AXIOMS
* unit: `dp` == density_independent_pixel
* conversion: `1dp` == `1px` @ 160dpi
* grid_base: `8dp`
* grid_micro: `4dp`
* invariant: all_dimensions % `4dp` == 0
* invariant: touch_target_min == `48dp` x `48dp`
* invariant: pointer_target_min == `44dp` x `44dp`

# WINDOW_SIZE_CLASSES
* role: adaptive_breakpoint_system
* logic: width_based_classification
* state_space: {COMPACT, MEDIUM, EXPANDED, LARGE, EXTRA_LARGE}

## CLASS: COMPACT
* range: width < `600dp`
* typical_device: {phone_portrait}
* layout_structure:
  * panes_visible: 1
  * navigation: {navigation_bar | modal_navigation_drawer}
  * body_margins: `16dp`
  * dialog_type: {simple | fullscreen}
  * action_placement: bottom_sheet

## CLASS: MEDIUM
* range: `600dp` <= width < `840dp`
* typical_device: {tablet_portrait | foldable_unfolded_portrait}
* layout_structure:
  * panes_visible: 1 [recommended] | 2 [possible_for_low_density]
  * navigation: {navigation_rail | navigation_bar}
  * body_margins: `24dp`
  * pane_spacer: `24dp`
  * action_placement: menu

## CLASS: EXPANDED
* range: `840dp` <= width < `1200dp`
* typical_device: {tablet_landscape | foldable_landscape | phone_landscape}
* layout_structure:
  * panes_visible: 2
  * navigation: {navigation_rail | navigation_drawer}
  * body_margins: `24dp`
  * pane_spacer: `24dp`
  * action_placement: menu

## CLASS: LARGE
* range: `1200dp` <= width < `1600dp`
* typical_device: {laptop | desktop}
* layout_structure:
  * panes_visible: 2
  * navigation: {navigation_drawer [standard] | navigation_rail}
  * body_margins: `24dp`
  * pane_spacer: `24dp`
  * fixed_pane_width_default: `360dp` | `412dp`

## CLASS: EXTRA_LARGE
* range: width >= `1600dp`
* typical_device: {desktop_monitor | ultra_wide}
* layout_structure:
  * panes_visible: 2 | 3 [with_side_sheet]
  * navigation: {navigation_drawer [standard]}
  * body_margins: `24dp`
  * pane_spacer: `24dp`
  * max_width_constraint: required [prevent_line_length_fatigue]

# STRUCTURAL_REGIONS
* topology: window -> {navigation_region + body_region}

## NAVIGATION_REGION
* placement:
  * LTR => left_edge
  * RTL => right_edge
  * COMPACT => bottom_edge [navigation_bar]
* z_index: high [above_body_scrolling]
* containment: explicit_surface_coloring

## BODY_REGION
* role: content_container
* composition: {pane | pane + spacer + pane}
* constraint: content_safe_area
  * avoid: display_cutouts
  * avoid: software_keyboard
  * avoid: system_gestures
  * avoid: hinge_seam [foldable]

# PANE_SYSTEM
* definition: atomic_layout_container
* types: {FIXED, FLEXIBLE}

## PANE: FIXED
* width: immutable [static_dp]
* usage: {list_view | supporting_content | navigation_structure}
* default_width[large+]: `360dp` -> `412dp`
* constraint: width <= `400dp` [if_side_sheet]

## PANE: FLEXIBLE
* width: fluid [fill_available_space]
* usage: {detail_view | document_editor | media_viewer}
* logic: `window_width` - `navigation_width` - `margins` - `spacers` - `fixed_pane_width`

## PANE_BEHAVIORS
* strategy[reflow]:
  * condition: window_size_decrease
  * action: horizontal_panes -> vertical_stack
* strategy[show_hide]:
  * condition: compact_width
  * action: focus_pane -> visible, support_pane -> hidden
* strategy[levitate]:
  * condition: temporary_context
  * action: pane -> overlay [floating | docked]
  * example: bottom_sheet -> floating_pane [on_resize]

## DRAG_HANDLE
* role: pane_resizer
* placement: inside `spacer`
* interaction:
  * tap: toggle {collapse | expand}
  * drag: resize_ratio
* visual_state:
  * hover: cursor -> resize_icon
  * focus: visible_ring
* accessibility: focusable + keyboard_actuatable

# SPACING_TOKENS
* logic: visual_breathing_room
* scale: `4dp` increments

## MARGINS
* definition: window_edge -> content_start
* value[compact]: `16dp`
* value[medium+]: `24dp`
* override: `0dp` [full_bleed_media]

## PADDING
* definition: container_edge -> internal_element
* min: `4dp`
* standard: `16dp`

## SPACERS
* definition: pane_a <-> pane_b
* standard: `24dp`
* visual_centering: required [in_split_pane_layouts]

# CANONICAL_LAYOUTS
* nature: architectural_patterns

## PATTERN: LIST_DETAIL
* relationship: parent -> child
* composition:
  * pane_1: list_collection [fixed | flexible]
  * pane_2: item_detail [flexible]
* behavior[compact]:
  * state_a: list_visible
  * interaction: tap_item -> nav_push -> detail_visible
* behavior[expanded+]:
  * state: list + detail [co-planar]
  * interaction: tap_item -> update_detail

## PATTERN: SUPPORTING_PANE
* relationship: focus -> helper
* composition:
  * pane_1: main_content [flexible]
  * pane_2: support_tools [fixed, `360dp`]
* behavior[compact]: support -> bottom_sheet
* behavior[expanded]: support -> side_panel

## PATTERN: FEED
* structure: grid_collection
* adaptation:
  * compact: 1 column
  * medium: 2 columns
  * expanded: 3 columns
  * large: 4 columns
* item_sizing: aspect_ratio_preservation

# HARDWARE_CONSIDERATIONS

## FOLDABLES
* state: {FOLDED, OPEN_FLAT, TABLETOP}
* hinge_awareness:
  * logic: no_content_across_hinge
  * action: split_view -> snap_to_hinge
* posture[tabletop]:
  * top_half: viewing_area
  * bottom_half: controls_area

## INPUT_MODALITIES
* touch:
  * target: `48dp`+
  * spacing: `8dp` between targets
* cursor:
  * target: `44dp`+ [denser_layouts_allowed]
  * hover: state_layer_visible
* keyboard:
  * focus_order: DOM_order [left->right, top->bottom]
  * shortcuts: required [navigation_efficiency]

# GROUPING_LOGIC
* type[explicit]:
  * mechanism: {card | border | divider | surface_color_change}
  * signal: separation_of_context
* type[implicit]:
  * mechanism: {whitespace | proximity}
  * signal: relationship_strength
  * rule: internal_gap < external_gap
