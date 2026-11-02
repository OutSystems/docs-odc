---
summary: OutSystems Developer Cloud (ODC) container layout configures Flexbox and Grid for responsive nav bars, product grids, and checkout forms.
tags:
  - CSS
  - Forms
  - Front-End
  - Layouts
  - Screens
  - UI
  - Widgets
locale: en-us
guid: 0ad9d5bd-0cf8-4c23-9c4b-6cba67f3a7a8
app_type: mobile apps, reactive web apps
figma:
platform-version: odc
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - odc studio
coverage-type:
  - remember
  - apply
content-type:
  - reference
  - procedure
topic:
  - configure-flexbox-layout
  - configure-grid-layout
isautopublish: true
---

# Configure container layout

The **Container**, **Placeholder**, and **Form** widgets each have a **Layout**
section on their **Styles** tab. Use the **Type** property to align, distribute, and
reflow child elements with standard CSS Flexbox or Grid, directly in the **Properties**
panel, with the result visible immediately on the canvas.

Layout properties apply to a single widget at a time and work independently of the
app's theme. Setting `Type` on one container doesn't change the theme's Grid Type or
any other container on the screen. For more information about the theme-level grid,
refer to [Themes](themes/intro.md).

The examples use a retail app that customers use to browse and buy products from
a phone, a tablet, or a desktop browser.

## Configure a responsive nav bar with flexbox

A nav bar with a fixed logo and navigation links that fill the remaining space is
a common header pattern, but building it usually meant writing custom CSS to
align and distribute the elements. This procedure achieves the same result using
Flexbox layout properties only, so you get a responsive nav bar without writing
or maintaining CSS.

To place the retail app's logo on one side of the nav bar and navigation links on
the other, and to keep the logo a fixed size while the links fill the remaining
space, follow these steps:

1. Select the Container that holds the logo and the navigation links.
1. On the **Styles** tab, in the **Layout** section, set **Type** to **Flexbox**.
1. Set **Direction** to **Row** and **Justify Content** to **Space Between** so the
    logo and the links sit at opposite ends of the container.
1. Select the logo element. In its **Flex Item** section, set **Self** to **Fixed**
    so it keeps its natural size.
1. Select the navigation links element. In its **Flex Item** section, set **Self**
    to **Grow** so it fills the remaining space.

### Layout properties

| Name | Description | Mandatory | Default value | Observations |
| --- | --- | --- | --- | --- |
| Type | Sets how the widget lays out its child elements: `None` for standard document flow, `Flexbox` for one-dimensional layout, or `Grid` for two-dimensional layout. | Yes | `None` for existing containers, `Flexbox` for new containers. | Selecting `Flexbox` or `Grid` shows the properties below. |
| Direction | Sets the main axis of a Flexbox container. | No | Row | Shown only when `Type` is `Flexbox`. |
| Justify Content | Aligns child elements along the main axis, for example `Space Between` or `Center`. | No | Start | Shown only when `Type` is `Flexbox`. |
| Gap | Sets the space between child elements. | No | `0px` | Shown only when `Type` is `Flexbox` or `Grid`. |
| Align Items | Aligns child elements along the cross axis. | No | Stretch | Shown only when `Type` is `Flexbox`. |

| Wrap | Sets whether child elements wrap onto multiple lines. | No | No Wrap | Shown only when `Type` is `Flexbox`.|
| Edit grid | Opens the grid builder, where you set the number of columns, rows, and the gap for each breakpoint (Small, Medium, Large, Extra Large). | No | — | Shown only when `Type` is `Grid`. |

### Flex item properties

Shown on a child element only when its parent's `Type` is `Flexbox`.

| Name | Description | Mandatory | Default value | Observations |
| --- | --- | --- | --- | --- |
| Self | Sets how the element grows or shrinks inside the parent container: `Fixed` keeps its natural size, `Grow` expands to fill available space, `Shrink` compresses when space is tight, and `Both` grows and shrinks. | No | Shrink | — |

## Configure a responsive product grid

A product catalog that shows a different number of columns on a desktop, a
tablet, and a phone traditionally required custom CSS media queries to reflow
the grid at each screen size. This procedure achieves the same result using Grid
layout properties only, so the catalog reflows without writing or maintaining
CSS.

To arrange product cards into columns that reflow at different screen sizes,
follow these steps:

1. Select the Container that holds the product cards.
1. On the **Styles** tab, in the **Layout** section, set **Type** to **Grid**.
1. Click **Edit grid** to open the grid builder.
1. For the **Large** breakpoint, set **Columns** to `4`. For **Medium**, set
    **Columns** to `2`. For **Small**, set **Columns** to `1`.
1. Select a product card. In its **Grid Item** section, set **Column Span** to `1`
    for each breakpoint.

### Grid item properties

Shown on a child element only when its parent's `Type` is `Grid`. Set independently
for each breakpoint (Small, Medium, Large, Extra Large).

| Name | Description | Mandatory | Default value | Observations |
| --- | --- | --- | --- | --- |
| Column Span | Sets how many columns the element spans. | No | `1` for each breakpoint | Can't exceed the parent's column count for that breakpoint. |
| Row Span | Sets how many rows the element spans. | No | `1` for each breakpoint | Can't exceed the parent's row count for that breakpoint. |

## Configure a responsive product detail screen with flexbox

A product detail screen that places an image and its description side by side
on a desktop, but stacks them vertically on a phone, traditionally meant
maintaining two versions of the screen or writing custom CSS breakpoints. This
procedure achieves the same result by switching the Flexbox **Direction** property
per breakpoint, without duplicating the screen or writing CSS.

To place a product image and its description side by side on larger screens,
and stack them vertically on a phone, follow these steps:

1. Select the Container that holds the product image and the description.
1. On the **Styles** tab, in the **Layout** section, set **Type** to **Flexbox**.
1. Set **Direction** to **Row** so the image and the description sit side by side.
1. Select the **Small** breakpoint on the canvas, then set **Direction** to
    **Column** so the image and the description stack vertically on a phone.

## Configure a checkout form with grid column spanning

A checkout form that combines a full-width field, such as a shipping address,
with two half-width fields in the same row, such as city and postal code,
traditionally required a custom CSS class to control column widths. This
procedure achieves the same result using Grid column spanning only, without
adding a custom CSS class.

To combine a full-width field with two half-width fields in the same row,
without adding a custom CSS class, follow these steps:

1. Select the Container that holds the checkout form fields.
1. On the **Styles** tab, in the **Layout** section, set **Type** to **Grid**.
1. Click **Edit grid** to open the grid builder, and set **Columns** to `2` for
    the breakpoints where you want two fields per row.
1. Select the shipping address field. In its **Grid Item** section, set
    **Column Span** to `2` for each breakpoint, so it spans the full row.
1. Select the city field and the postal code field. In their **Grid Item**
    sections, set **Column Span** to `1` for each breakpoint, so they sit side by
    side in the same row.

## When to use custom CSS

Use the **Properties** panel first, and write CSS only for cases that the panel
doesn't support.

Layout properties cover the following cases without CSS:

* Direction and alignment (**Direction**, **Justify Content**, and **Align Items**).
* Wrapping between elements.
* Column count and row count in Grid.
* A child's grow and shrink behavior (**Self**).
* A child's column span and row span in Grid.

Add a custom CSS class in the following cases:

* The grid builder only supports equal-width columns. For custom column widths,
    such as a fixed-width sidebar next to a fluid content area, add a custom CSS
    class.
* Properties such as `align-content` for multi-line Flexbox wrapping, and
    `justify-self` or `align-self` for individual grid cells, aren't exposed on the
    Styles tab and require a custom CSS class.

A custom CSS class takes precedence over Layout properties, so you can extend the
generated layout without conflicts. For example, if a Container has **Direction** set to **Row**, adding a CSS class with `flex-direction` column overrides it and the container lays out as a column.

## Related resources

For more information about the Screen, Block, and Placeholder elements a
Container works alongside, refer to [Screens](screen-about.md).
