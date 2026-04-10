# MODULE: INTERACTION_PHYSICS
* domain: m3_interactive_feedback
* nature: state_response_algorithms
* context: real_time_ui_behavior
* goal: communicate_interactivity + provide_feedback

# STATE_LAYER_LOGIC
* nature: additive_overlay_system
* mechanism: `container_color` + (`state_layer_color` @ `opacity`)
* rule[state_layer_color]:
  * condition: default
  * value: `on-color` of the component [e.g., `on-surface` for a surface component]
* topology: layer_stack -> {1: container, 2: state_layer, 3: content}
* invariant: single_state_layer_per_component == true [only one state active at a time]

# STATE_OPACITY_VALUES [THE_PHYSICS_CONSTANTS]
* unit: float [0.0 to 1.0]

## LAYER: HOVER
* state: pointer_hover
* value: `0.08` [8% opacity]
* behavior: animated_fade_in [short_duration]
* application: actions, selection_controls, inputs, cards, chips

## LAYER: FOCUS
* state: keyboard_or_voice_highlight
* value: `0.10` [10% opacity]
* application: all_interactive_components
* visual_requirement: keyboard_focus_indicator [focus_ring]

## LAYER: PRESSED
* state: touch_down | click_down
* value: `0.10` [10% opacity]
* mechanism: ripple_animation [expanding_from_contact_point]
* application: all_interactive_components

## LAYER: DRAGGED
* state: long_press + move
* value: `0.16` [16% opacity]
* feedback: often_paired_with_elevation_increase [+1 level]
* application: cards, chips, list_items

## LAYER: DISABLED
* state: inoperable
* value[container]: `0.12` [12% opacity] | `transparent`
* value[content]: `0.38` [38% opacity]
* rule: disabled_states !require_contrast_minimums

# INTERACTION_TARGET_GEOMETRY

## TARGET: TOUCH_INPUT
* context: mobile | tablet | handheld
* min_size: `48dp` x `48dp`
* physical_size: ~9mm
* logic: `visual_element_size` + `padding` == `touch_target`
* mapping: `24dp_icon` -> needs -> `12dp_padding_perimeter`

## TARGET: POINTER_INPUT
* context: desktop | laptop | mouse_connected
* min_size: `44dp` x `44dp`
* usage: high_density_layouts
* logic: allowable_for_mouse_precision

## TARGET: SPACING_LAW
* rule: targets_separated_by >= `8dp`
* result: prevent_accidental_triggers

# FOCUS_TRAVERSAL_PROTOCOL

## TRAVERSAL_LOGIC
* order: DOM_sequence [source_code_order]
* direction: {left -> right, top -> bottom} [LTR context]
* key_mapping:
  * `Tab`: move_forward
  * `Shift + Tab`: move_backward
  * `Enter | Space`: activate_focused_element
  * `Arrows`: navigate_within_groups [e.g., menu_items, radio_buttons]
  * `Escape`: dismiss_modal | remove_focus

## FOCUS_RING_ANATOMY
* entity: `md-focus-ring`
* width: `3px`
* offset[outward]: `2px` from container_edge
* offset[inward]: `0px` [used for list_items or edge_aligned_elements]
* color: `secondary` [default]
* shape: matches_parent_container_shape

# COMPONENT_STATE_INHERITANCE

## DOMAIN: ACTIONS [Button, FAB, Chip]
* inherits: {hover, focus, pressed, disabled}
* state_change: visual_overlay + elevation_shift

## DOMAIN: SELECTION [Checkbox, Radio, Switch]
* inherits: {hover, focus, pressed, disabled}
* special_case: `selected` + `hover` combination allowed

## DOMAIN: CONTAINMENT [Card, Dialog, Sheet]
* inherits: {hover, focus, dragged}
* rule: modal_containment => traps_focus [sequential_tabbing_limited_to_modal]

## DOMAIN: NAVIGATION [Bar, Rail, Tab]
* inherits: {hover, focus, pressed}
* state_indicator: `active_indicator` [shape_morph | color_shift]
* constraint: !inherits_dragged [fixed_position_requirement]

# INTERACTION_DENSITY_ALGORITHM
* role: manual_scaling_logic
* scale_step: `4dp`
* mapping:
  * Default [0]: standard_padding
  * Dense [-1]: `padding` - `4dp`
  * Denser [-2]: `padding` - `8dp`
* constraint: !allow_target < `48dp` [touch] | `40dp` [pointer]

# GESTURE_MAPPING_LAWS
* gesture[tap]: trigger_action [primary]
* gesture[long_press]: enter_selection_mode | reveal_tooltip
* gesture[swipe]: horizontal_navigation | lateral_action [delete/archive]
* gesture[drag]: reorder_content | resize_pane
* gesture[predictive_back]:
  * logic: preview_previous_view during swipe
  * compatibility: {bottom_sheet, navigation_bar, navigation_rail, side_sheet}

# FEEDBACK_PHYSICS
* ripple:
  * duration: ~200ms
  * easing: `standard`
  * behavior: expands_from_origin
* shape_morph:
  * interaction: `press` | `hover`
  * logic: corner_radius_interpolation [e.g., 12dp -> 16dp]
