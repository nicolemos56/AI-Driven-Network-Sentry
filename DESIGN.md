---
name: Synthetic Intelligence Network
colors:
  surface: '#10131a'
  surface-dim: '#10131a'
  surface-bright: '#363940'
  surface-container-lowest: '#0b0e14'
  surface-container-low: '#191c22'
  surface-container: '#1d2026'
  surface-container-high: '#272a31'
  surface-container-highest: '#32353c'
  on-surface: '#e1e2eb'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#e1e2eb'
  inverse-on-surface: '#2e3037'
  outline: '#849495'
  outline-variant: '#3b494b'
  surface-tint: '#00dbe9'
  primary: '#dbfcff'
  on-primary: '#00363a'
  primary-container: '#00f0ff'
  on-primary-container: '#006970'
  inverse-primary: '#006970'
  secondary: '#ffb77f'
  on-secondary: '#4e2600'
  secondary-container: '#ff8a00'
  on-secondary-container: '#613100'
  tertiary: '#faf3ff'
  on-tertiary: '#3c0090'
  tertiary-container: '#e1d2ff'
  on-tertiary-container: '#7213ff'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#7df4ff'
  primary-fixed-dim: '#00dbe9'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#ffdcc4'
  secondary-fixed-dim: '#ffb77f'
  on-secondary-fixed: '#2f1500'
  on-secondary-fixed-variant: '#6f3900'
  tertiary-fixed: '#e9ddff'
  tertiary-fixed-dim: '#d1bcff'
  on-tertiary-fixed: '#23005b'
  on-tertiary-fixed-variant: '#5700c9'
  background: '#10131a'
  on-background: '#e1e2eb'
  surface-variant: '#32353c'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-sm:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  body-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 18px
  mono-label:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
  mono-data:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 20px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 16px
  margin-page: 24px
  container-padding: 12px
---

## Brand & Style

The design system is engineered for high-stakes Network AIOps environments, where rapid data synthesis and precision are paramount. The brand personality is technical, vigilant, and authoritative—evoking the feeling of a futuristic Network Operations Center (NOC). 

The visual style is a fusion of **Modern Minimalism** and **Technical Glassmorphism**. It prioritizes data density and legibility without sacrificing the "high-tech" aesthetic. Key visual markers include:
- **Luminous HUD Elements:** Utilizing glowing indicators and neon accents to draw attention to critical system states.
- **Micro-interactions:** Snappy, precise transitions that provide immediate feedback for automated AI actions.
- **Data-First Hierarchy:** A UI that recedes into the background, allowing real-time telemetry and network topologies to take center stage.

## Colors

The palette is optimized for long-duration monitoring in low-light environments, reducing eye strain while highlighting anomalies.

- **Base Layers:** `#0B0E14` serves as the foundation. Surfaces and containers use `#151921` to create subtle depth.
- **Primary (Active):** Neon Cyan (`#00F0FF`) is reserved for active states, successful AI optimizaitons, and healthy data flows. It should be used sparingly for maximum impact.
- **Secondary (Alert/Critical):** Critical Orange (`#FF8A00`) signifies "Zombie States," hardware failures, or high-latency nodes. It uses an outer glow effect in the UI to imply urgency.
- **Tertiary (Processing):** Deep Violet (`#7000FF`) represents background AI processing and automated heuristics.
- **Borders:** Use low-opacity `#2D3544` for container strokes to maintain structure without visual clutter.

## Typography

Typography balances clean, modern readability with the utilitarian feel of terminal interfaces.

- **Headlines:** Use **Inter** with tight letter spacing for a structured, professional look.
- **Technical Data:** All logs, IP addresses, and telemetry metrics must use **JetBrains Mono**. This ensures character alignment in data-heavy tables.
- **Hierarchy:** Use uppercase styling for `mono-label` to denote section headers within sidebars and small widget titles. 
- **Scale:** On mobile, `display-lg` should scale down to `32px` to maintain layout integrity.

## Layout & Spacing

This design system utilizes a **12-column fluid grid** for the main dashboard area, with a fixed 280px sidebar for global navigation. 

- **Density:** The layout is "High-Density." Use a 4px base unit. Standard component padding is `12px` to maximize the amount of data visible on a single screen.
- **Modules:** Dashboard widgets should use a "Bento-box" style layout, where each module is clearly defined by a thin border.
- **Breakpoints:** 
  - **Desktop (1440px+):** Full 12-column visibility.
  - **Tablet (768px-1439px):** Sidebar collapses to icons; grid shifts to 6 columns.
  - **Mobile (<767px):** Single column stack; technical logs use horizontal scrolling.

## Elevation & Depth

Hierarchy is achieved through **Tonal Layering** and **Glassmorphism** rather than traditional heavy shadows.

- **Backdrop Blur:** Use a `12px` blur on modal overlays and dropdown menus to create a "glass" effect over live data feeds.
- **Surface Strokes:** Instead of shadows, use 1px inner borders with a 10% white opacity to define the top edge of containers ("rim lighting").
- **Glow Effects:** Use `0px 0px 8px` blurs for active status indicators (Cyan) and critical alerts (Orange) to simulate a self-illuminated display.
- **Z-Axis:** 
  - Level 0: Background (`#0B0E14`)
  - Level 1: Cards/Widgets (`#151921`)
  - Level 2: Popovers/Tooltips (Glassmorphic blur + `#1C222D`)

## Shapes

The shape language is "Soft-Industrial." 

- **Primary Radius:** Use `4px` (Soft) for all main containers, cards, and buttons. This provides a precise, engineered look that feels more modern than sharp corners but more professional than fully rounded ones.
- **Speciality Shapes:** Terminal-style input fields should maintain a `2px` radius to emphasize their technical nature.

## Components

### Buttons
- **Primary:** Solid Cyan (`#00F0FF`) with black text. High visibility for primary actions.
- **Ghost:** Thin `1px` border with Cyan text. Used for secondary dashboard controls.
- **Alert:** Solid Orange (`#FF8A00`) with a subtle outer pulse animation for critical overrides.

### Technical Logs
- Rendered in **JetBrains Mono**.
- Zebra-striping using a 2% contrast difference between rows.
- Hover state highlights the entire row with a subtle Cyan left-border accent.

### Chips & Indicators
- **Status Chips:** Small, pill-shaped with a 4px dot indicator. 
- **Active:** Cyan dot. **Zombie:** Pulsing Orange dot. **Idle:** Muted Grey dot.

### Input Fields
- Dark background (`#0B0E14`) with a `1px` stroke. 
- Focus state: Stroke changes to Cyan with a `0px 0px 4px` Cyan outer glow.

### Cards (Widgets)
- Background: `#151921` at 80% opacity with backdrop-filter: blur(10px).
- Header: Includes a `mono-label` title and a "Full Screen" icon toggle.

### Additional Components
- **Network Topology Map:** Nodes utilize the elevation glow rules; lines between nodes (edges) use varying stroke weights to represent bandwidth.
- **Sparklines:** Compact, sans-axis charts embedded in list rows to show 24h trends.