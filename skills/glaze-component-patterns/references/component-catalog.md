# Component Catalog

Import components from `@glaze/core/components`, hooks from `@glaze/core/hooks`, and utilities from `@glaze/core/utils`.

```typescript
import { Button, Dialog, Panel, Sidebar } from "@glaze/core/components";
import { useConnection, useEnvironment, useTheme } from "@glaze/core/hooks";
import { cn, initLogging } from "@glaze/core/utils";
```

Read the linked component documentation with `glaze-component-docs-reader` before use.

| Pattern | Component(s) | Doc |
| --- | --- | --- |
| **Layout** |  |  |
| App shell | `SplitView` | `split-view.md` |
| Custom resizable panels | `PanelGroup`, `Panel` | `panel.md` |
| Application sidebar | `Sidebar`, `SidebarList`, `SidebarListItem`, `SidebarListGroup`, `SidebarFooter`, `SidebarListItemContent/Title/Subtitle/Accessory` | `sidebar.md` |
| Top/bottom toolbar | `Toolbar`, `ToolbarRow`, `ToolbarActions`, `ToolbarContent`, `ToolbarTitle`, `ToolbarDescription` | `toolbar.md` |
| Toolbar search | `ToolbarSearchButton` | `toolbar.md` |
| Detail-page back button | `ToolbarBackButton`, or `ScrollArea`'s `leading` prop | `toolbar.md` |
| Scrollable container | `ScrollArea` | `scroll-area.md` |
| Grid with keyboard navigation | `Grid.Root`, `Grid.Item` | `grid.md` |
| Vertical list with selection | `List.Root`, `List.Item`, `List.ItemTitle` | `list.md` |
| Inspector/detail panel | `Inspector`, `InspectorRow`, `InspectorSection`, `InspectorToggle` | `inspector.md` |
| Expandable section | `CollapsibleRoot`, `CollapsibleTrigger`, `CollapsibleContent`, `CollapsibleChevron` | `collapsible.md` |
| Visual divider | `Separator` | `separator.md` |
| **Forms** |  |  |
| Text input | `Input` | `input.md` |
| Multi-line text | `Textarea` | `textarea.md` |
| Numeric input | `NumberInput` | `number-input.md` |
| Date/time picker | `NativeDatePickerRoot`, `NativeDatePickerTrigger`, `NativeDatePickerValue` | `date-picker.md` |
| Color picker | `ColorWell` | `color-well.md` |
| Dropdown select | `Select`, `SelectTrigger`, `SelectContent`, `SelectItem` | `select.md` |
| Dropdown with custom children | `CustomSelect`, its trigger/content/item primitives | `custom-select.md` |
| Boolean checkbox | `Checkbox` | `checkbox.md` |
| Boolean switch | `Switch` | `switch.md` |
| Radio group | `RadioGroup`, `RadioGroupItem` | `radio-group.md` |
| Range slider | `Slider` | `slider.md` |
| Form field wrapper | `FieldSet`, `Field` | `field.md` |
| Form label | `Label` | `label.md` |
| **Actions** |  |  |
| Button | `Button` | `button.md` |
| Grouped buttons | `ButtonGroup`, `ButtonGroupSeparator` | `button-group.md` |
| Back/forward navigation | `NavigationButtonGroup` | `button-group.md` |
| Pressed-state button | `ToggleButton` | `toggle-button.md` |
| Dropdown menu | `DropdownMenu`, `DropdownMenuTrigger`, `DropdownMenuContent`, `DropdownMenuItem` | `dropdown-menu.md` |
| Native share sheet | `ShareSheet`, `ShareSheetTrigger` | `share-sheet.md` |
| Custom-child dropdown | `CustomDropdownMenu` and its primitives | `custom-dropdown-menu.md` |
| Command palette | `Command`, `CommandDialog`, `CommandInput`, `CommandList`, `CommandItem` | `command.md` |
| Right-click menu | `ContextMenu`, `ContextMenuTrigger`, `ContextMenuContent`, `ContextMenuItem` | `context-menu.md` |
| Custom-child context menu | `CustomContextMenu` and its primitives | `custom-context-menu.md` |
| **Dialogs and overlays** |  |  |
| Modal dialog | `Dialog` and its primitives | `dialog.md` |
| Must-decide dialog | `AlertDialog` | `alert-dialog.md` |
| Hover tooltip | `Tooltip`, `TooltipTrigger`, `TooltipContent`, `TooltipProvider` | `tooltip.md` |
| **Feedback** |  |  |
| Toast | `Toaster`, `toast()` | `sonner.md` |
| Live status | `Status` | `status.md` |
| New/unseen indicator | `NotificationDot` | `notification-dot.md` |
| Inline notice/banner | `Callout` | `callout.md` |
| Empty content | `EmptyState` and its title/description/actions/media | `empty-state.md` |
| Error fallback | `ErrorBoundaryView` | `error-boundary-view.md` |
| Edge blur | `ProgressiveBlur` | `progressive-blur.md` |
| **Data display** |  |  |
| Text | `Text` | `text.md` |
| Avatar/stack | `Avatar`, `AvatarImage`, `AvatarFallback`, `AvatarBadge`, `AvatarStack` | `avatar.md` |
| Static label/tag/count | `Badge` | `badge.md` |
| Data table | `Table`, `TableHeader`, `TableBody`, `TableRow`, `TableHead`, `TableCell` | `table.md` |
| Tabs | `TabsRoot`, `Tabs`, `TabsTrigger`, `TabsSeparator`, `TabsContent` | `tabs.md` |
| Segmented control | `SegmentedControl`, `SegmentedControlItem`, `SegmentedControlSeparator` | `segmented-control.md` |
| Shortcut hint | `Key`, `KeyGroup` | `key.md` |

## Raw element replacements

Use `Button` for `<button>`, `Input` for text input, `Checkbox`/`RadioGroup`/`Slider`/`NumberInput` for typed inputs, `Select` for `<select>`, `Textarea`, `Table`, `Dialog`, `List` for interactive lists, `Sidebar` for navigation, and `Label`/`Field` for form structure.

## Hooks and utilities

| Symbol                | Purpose                          |
| --------------------- | -------------------------------- |
| `useTheme`            | Apply theme to the document      |
| `useConnection`       | Track IPC connection             |
| `useEnvironment`      | Read app environment information |
| `useWindowFocusState` | Track window focus               |
| `useGlazeAI`          | Run renderer-triggered Glaze AI  |
| `cn`                  | Merge class names                |
| `initLogging`         | Initialize renderer logging      |
