# MODULE: TEMPORAL_DYNAMICS
* domain: m3_choreography
* nature: kinematic_laws_and_timing_specs
* context: manual_tween_implementation
* goal: fluid_natural_response + spatial_logic_communication

# MOTION_SYSTEM_ARCHETYPES
* role: defining_product_personality
* types: {EXPRESSIVE_PHYSICS, STANDARD_EASING}

## SCHEME: EXPRESSIVE
* nature: physics_driven [spring_based]
* characteristic: overshoot + bounce
* use_case: hero_moments, primary_actions, attention_seeking_elements
* logic: communicate_weight_and_energy

## SCHEME: STANDARD
* nature: functional_response
* characteristic: smooth_entry + soft_exit [no_overshoot]
* use_case: utilitarian_apps, high_frequency_interactions, dense_data_editing
* logic: efficiency_and_focus

# SPRING_TO_BEZIER_CONVERSION [THE_MANUAL_TWEEN_MAP]
* role: implementing_physics_on_non_physics_engines
* logic: `spring_token` -> converted_to -> {`cubic_bezier` + `duration`}

## EXPRESSIVE_SPRING_TOKENS [Overshoot]
* **fast_spatial**:
  * curve: `cubic-bezier(0.42, 1.67, 0.21, 0.90)`
  * duration: `350ms`
  * usage: small_movement, rotation, size_change
* **default_spatial**:
  * curve: `cubic-bezier(0.38, 1.21, 0.22, 1.00)`
  * duration: `500ms`
  * usage: medium_screen_coverage, drawer_opening
* **slow_spatial**:
  * curve: `cubic-bezier(0.39, 1.29, 0.35, 0.98)`
  * duration: `650ms`
  * usage: full_screen_transitions
* **fast_effects**:
  * curve: `cubic-bezier(0.31, 0.94, 0.34, 1.00)`
  * duration: `150ms`
  * usage: color_tint, opacity_fade [no_overshoot_allowed]
* **default_effects**:
  * curve: `cubic-bezier(0.34, 0.80, 0.34, 1.00)`
  * duration: `200ms`
* **slow_effects**:
  * curve: `cubic-bezier(0.34, 0.88, 0.34, 1.00)`
  * duration: `300ms`

## STANDARD_SPRING_TOKENS [No Overshoot]
* **fast_spatial**:
  * curve: `cubic-bezier(0.27, 1.06, 0.18, 1.00)`
  * duration: `350ms`
* **default_spatial**:
  * curve: `cubic-bezier(0.27, 1.06, 0.18, 1.00)`
  * duration: `500ms`
* **slow_spatial**:
  * curve: `cubic-bezier(0.27, 1.06, 0.18, 1.00)`
  * duration: `750ms`

# DURATION_SCALE [ATOMIC_TIMINGS]
* nature: discrete_temporal_steps
* unit: `ms` [milliseconds]

## SCALE: SHORT [Utility]
* `short_1`: `50ms`   => interaction: micro_feedback
* `short_2`: `100ms`  => interaction: switch_toggle
* `short_3`: `150ms`  => interaction: icon_state_change
* `short_4`: `200ms`  => interaction: selection_control_ripple

## SCALE: MEDIUM [Transitions]
* `medium_1`: `250ms` => scope: small_component_entry
* `medium_2`: `300ms` => scope: card_expansion_start
* `medium_3`: `350ms` => scope: menu_deployment
* `medium_4`: `400ms` => scope: fab_to_sheet_expansion

## SCALE: LONG [Expressive]
* `long_1`: `450ms`   => scope: modal_dialog_entry
* `long_2`: `500ms`   => scope: card_to_fullscreen [standard]
* `long_3`: `550ms`
* `long_4`: `600ms`   => scope: complex_multistage_animation

## SCALE: EXTRA_LONG [Ambient]
* `extra_long_1`: `700ms`
* `extra_long_2`: `800ms`
* `extra_long_3`: `900ms`
* `extra_long_4`: `1000ms` => usage: auto_advance_carousel

# EASING_CURVE_SETS [LEGACY_FALLBACKS]

## SET: EMPHASIZED [M3_Default]
* **emphasized**: `(0.2, 0.0, 0, 1.0)`
  * behavior: fast_acceleration -> very_slow_deceleration
  * usage: full_screen_transitions, hero_moments
* **decelerate**: `(0.05, 0.7, 0.1, 1.0)`
  * usage: entering_the_screen
* **accelerate**: `(0.3, 0.0, 0.8, 0.15)`
  * usage: exiting_the_screen_permanently

## SET: STANDARD [M2_Compatibility]
* **standard**: `(0.2, 0.0, 0, 1.0)`
* **decelerate**: `(0.0, 0.0, 0.2, 1)`
* **accelerate**: `(0.4, 0.0, 1, 1)`

# TRANSITION_PATTERNS

## PATTERN: CONTAINER_TRANSFORM
* mechanism: persistent_container_interpolation
* logic: `start_bounds` -> `end_bounds`
* element_persistence: {container, hero_image, icon}
* easing: `emphasized` | `expressive_default_spatial`

## PATTERN: HIERARCHICAL_NAV [Forward/Backward]
* mechanism: horizontal_slide + cross_fade
* Android_logic: slide_distance < screen_width
* iOS_logic: parallax_background_offset
* easing: `emphasized` | `platform_default`

## PATTERN: LATERAL_NAV [Peer-to-Peer]
* mechanism: horizontal_slide [no_fade]
* logic: elements_slide_in_unison
* usage: {tabs, carousels, image_galleries}

## PATTERN: ENTER_EXIT
* direction: expand_away_from_edge
* behavior:
  * Android => x/y axis stretch [scale_avoided_to_reduce_depth_implication]
  * iOS => uniform_scale + fade
* spatial_model:
  * notifications => from_top
  * bottom_sheets => from_bottom
  * drawers => from_left

# CHOREOGRAPHY_HEURISTICS
* rule[unified_direction]: all_moving_elements -> align_to -> primary_axis
* rule[clean_fades]: `content_a` -> fully_fade_out -> before -> `content_b` -> fade_in
  * exception: cross_fade_allowed_if_very_fast [< 100ms]
* rule[stable_layouts]: usage: skeleton_loaders [pulse_animation_top_left_to_bottom_right]
* rule[responsive_duration]: `duration` ~ proportional_to -> `travel_distance` | `surface_area`
* constraint[accessibility]:
  * condition: system_reduced_motion == true
  * action: disable_overshoot, disable_parallax
  * replace: sliding/scaling -> subtle_fade_only
