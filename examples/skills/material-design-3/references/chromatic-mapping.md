# MODULE: CHROMATIC_SEMANTICS
* domain: m3_color_science
* nature: algorithmic_color_mapping
* context: dynamic_scheme_application
* tool_dependency: matugen | material-color-utilities

# COLOR_SPACE_FOUNDATION
* model: HCT [Hue, Chroma, Tone]
  * Hue: 0-360 [perceptual_hue]
  * Chroma: 0-120+ [colorfulness]
  * Tone: 0-100 [perceptual_lightness]
* invariant: Tone 100 == White
* invariant: Tone 0 == Black
* invariant: Contrast ~ delta(Tone)
  * min_delta(3.0:1) ~ 40 Tone
  * min_delta(4.5:1) ~ 50 Tone
  * min_delta(7.0:1) ~ 70 Tone

# SCHEME_GENERATION_LOGIC
* input: source_seed_color [HCT]
* process: algorithmic_generation
* output: 5_key_tonal_palettes -> 26+_semantic_roles

## KEY_PALETTES
* Primary: {hue: source, chroma: 48}
* Secondary: {hue: source, chroma: 16}
* Tertiary: {hue: source + 60, chroma: 24}
* Neutral: {hue: source, chroma: 4}
* NeutralVariant: {hue: source, chroma: 8}
* Error: {hue: 25, chroma: 84} [Static]

# SEMANTIC_ROLE_MAPPING [THE_GOLDEN_TABLE]
* logic: role -> mapped_to -> tonal_palette_tone
* scope: light_theme | dark_theme

## ACCENT_ROLES [High Emphasis]
* `primary`:
  * Light: Primary-40
  * Dark: Primary-80
  * usage: {FAB, active_states, prominent_buttons}
* `on-primary`:
  * Light: Primary-100
  * Dark: Primary-20
  * usage: {text_on_primary, icons_on_primary}
* `primary-container`:
  * Light: Primary-90
  * Dark: Primary-30
  * usage: {segmented_button_selected, low_emphasis_active_states}
* `on-primary-container`:
  * Light: Primary-10
  * Dark: Primary-90
  * usage: {text_on_primary_container}

* `secondary`:
  * Light: Secondary-40
  * Dark: Secondary-80
  * usage: {selection_controls, filter_chips}
* `on-secondary`:
  * Light: Secondary-100
  * Dark: Secondary-20
* `secondary-container`:
  * Light: Secondary-90
  * Dark: Secondary-30
* `on-secondary-container`:
  * Light: Secondary-10
  * Dark: Secondary-90

* `tertiary`:
  * Light: Tertiary-40
  * Dark: Tertiary-80
  * usage: {accents, contrasting_elements}
* `on-tertiary`:
  * Light: Tertiary-100
  * Dark: Tertiary-20
* `tertiary-container`:
  * Light: Tertiary-90
  * Dark: Tertiary-30
* `on-tertiary-container`:
  * Light: Tertiary-10
  * Dark: Tertiary-90

* `error`:
  * Light: Error-40
  * Dark: Error-80
* `on-error`:
  * Light: Error-100
  * Dark: Error-20
* `error-container`:
  * Light: Error-90
  * Dark: Error-30
* `on-error-container`:
  * Light: Error-10
  * Dark: Error-90

## SURFACE_ROLES [Backgrounds & Containers]
* `surface`:
  * Light: Neutral-98 [or 99 depending on scheme variant]
  * Dark: Neutral-6
  * usage: {app_background, scrolling_container}
* `on-surface`:
  * Light: Neutral-10
  * Dark: Neutral-90
  * usage: {body_text, icons, default_ink}
* `surface-variant`:
  * Light: NeutralVariant-90
  * Dark: NeutralVariant-30
  * usage: {card_background_unselected, input_field_background}
* `on-surface-variant`:
  * Light: NeutralVariant-30
  * Dark: NeutralVariant-80
  * usage: {medium_emphasis_text, subheaders, icons_inactive}

## SURFACE_CONTAINER_ROLES [Elevation Replacement]
* logic: strictly_hierarchical_tonality
* `surface-container-lowest`:
  * Light: Neutral-100
  * Dark: Neutral-4
  * usage: {scaffold_background_low_contrast}
* `surface-container-low`:
  * Light: Neutral-96
  * Dark: Neutral-10
  * usage: {cards_low_elevation}
* `surface-container`:
  * Light: Neutral-94
  * Dark: Neutral-12
  * usage: {default_cards, sheets}
* `surface-container-high`:
  * Light: Neutral-92
  * Dark: Neutral-17
  * usage: {dialogs, modal_bottom_sheets}
* `surface-container-highest`:
  * Light: Neutral-90
  * Dark: Neutral-22
  * usage: {pickers, input_fields}

## UTILITY_ROLES
* `outline`:
  * Light: NeutralVariant-50
  * Dark: NeutralVariant-60
  * usage: {text_field_border, active_borders, dividers_strong}
* `outline-variant`:
  * Light: NeutralVariant-80
  * Dark: NeutralVariant-30
  * usage: {dividers_subtle, disabled_borders, decorations}
* `scrim`:
  * Value: Neutral-0 [with opacity]
  * usage: {modal_backdrop}
* `shadow`:
  * Value: Neutral-0
  * usage: {elevation_shadow}
* `inverse-surface`:
  * Light: Neutral-20
  * Dark: Neutral-90
  * usage: {snackbars, inverse_tooltips}
* `inverse-on-surface`:
  * Light: Neutral-95
  * Dark: Neutral-20
* `inverse-primary`:
  * Light: Primary-80
  * Dark: Primary-40
  * usage: {actions_on_inverse_surface}

# FIXED_ACCENT_COLORS [Add-on Roles]
* definition: colors_that_do_not_swap_tone_in_dark_mode
* use_case: brand_specific_elements_requiring_consistency
* `primary-fixed`: Primary-90
* `on-primary-fixed`: Primary-10
* `primary-fixed-dim`: Primary-80
* `on-primary-fixed-variant`: Primary-30
* `secondary-fixed`: Secondary-90
* `on-secondary-fixed`: Secondary-10
* `secondary-fixed-dim`: Secondary-80
* `on-secondary-fixed-variant`: Secondary-30
* `tertiary-fixed`: Tertiary-90
* `on-tertiary-fixed`: Tertiary-10
* `tertiary-fixed-dim`: Tertiary-80
* `on-tertiary-fixed-variant`: Tertiary-30

# SCHEME_VARIANTS [Matugen Configs]
* `TONAL_SPOT` [Default]:
  * Primary: Source Hue, Chroma 36-48
  * Secondary: Source Hue, Chroma 16
  * Tertiary: Source Hue + 60, Chroma 24
  * Vibe: Calm, Supportive, Default.
* `VIBRANT`:
  * Primary: Source Hue, Chroma Max
  * Secondary: Source Hue, Chroma 24
  * Tertiary: Source Hue + randomly_shifted, Chroma 32
  * Vibe: Loud, Colorful, Content-focused.
* `EXPRESSIVE`:
  * Primary: Source Hue + 120, Chroma 40
  * Secondary: Source Hue - 120, Chroma 24
  * Tertiary: Source Hue + 180, Chroma 32
  * Vibe: Unexpected, Triadic, Bold.
* `CONTENT`:
  * Logic: Fidelity to source image colors
  * Usage: Media players, Album art extraction.
* `NEUTRAL`:
  * All Chromas -> reduced near 0
  * Vibe: Minimalist, Professional, Utility.
* `FRUIT_SALAD`:
  * Tertiary hue shifted +180
  * Vibe: Playful, Experimental.

# PAIRING_INVARIANTS [Accessibility Laws]
* rule: `*-container` MUST pair with `on-*-container`
* rule: `primary` MUST pair with `on-primary`
* rule: `surface` MUST pair with `on-surface`
* rule: `error` MUST pair with `on-error`
* anti_pattern: `primary` text on `primary-container` background [Low Contrast]
* anti_pattern: `outline` text on `surface` [Wrong Semantics]
* anti_pattern: `on-surface` on `inverse-surface` [Invisible]

# SURFACE_TINT_LOGIC
* context: elevation_representation
* mechanism: overlay `primary` color on `surface` color with opacity
* formula: `surface` + (`primary` @ `alpha`)
* levels:
  * 0dp -> 0% alpha
  * 1dp -> 5% alpha
  * 3dp -> 8% alpha
  * 6dp -> 11% alpha
  * 8dp -> 12% alpha
  * 12dp -> 14% alpha
* result: surface_tinted_color

# EXTENDED_COLOR_APPLICATION
* context: custom_semantic_colors [e.g. Success, Warning, Info]
* logic: generate_key_palette(source_hex)
* mapping:
  * `CustomColor`: Tone 40 [Light] / 80 [Dark]
  * `OnCustomColor`: Tone 100 [Light] / 20 [Dark]
  * `CustomColorContainer`: Tone 90 [Light] / 30 [Dark]
  * `OnCustomColorContainer`: Tone 10 [Light] / 90 [Dark]
* harmonization: `blend(custom_hue, primary_hue)` -> shift custom hue slightly towards primary
