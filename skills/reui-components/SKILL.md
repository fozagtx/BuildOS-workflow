---
name: reui-components
description: Modern React & Tailwind CSS component patterns, headless accessible primitives, and composable UI architecture from ReUI (reui.io/components). Use when building React component libraries, compound components, polymorphic elements (asChild pattern), and Tailwind CSS v3/v4 integrations.
---

# ReUI: Composable React & Tailwind Component Architecture

Source: [ReUI](https://reui.io/components)

ReUI defines modern architectural patterns for building headless, composable, and accessible UI component libraries in React with Tailwind CSS.

---

## 1. Core Architectural Pillars

### Pillar 1: Composable Compound Components
Avoid monolithic components with dozens of config props. Break widgets down into sub-components that share context:

```tsx
// Good: Composable, flexible sub-parts
<Card>
  <CardHeader>
    <CardTitle>Usage Metrics</CardTitle>
    <CardDescription>Real-time agent tool invocations.</CardDescription>
  </CardHeader>
  <CardContent>
    <MetricsTable data={metrics} />
  </CardContent>
  <CardFooter>
    <Button variant="outline">Export CSV</Button>
  </CardFooter>
</Card>
```

### Pillar 2: Class Variance & Merging with `cn()`
Use `clsx` and `tailwind-merge` to allow users to override default styles safely without class specificity conflicts:

```tsx
import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export function Button({ className, variant = "default", ...props }: ButtonProps) {
  return (
    <button
      className={cn(
        "inline-flex items-center justify-center rounded-xl font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 disabled:opacity-50",
        variant === "default" && "bg-neutral-900 text-white hover:bg-neutral-800",
        variant === "outline" && "border border-neutral-200 hover:bg-neutral-50",
        className
      )}
      {...props}
    />
  );
}
```

### Pillar 3: Polymorphism with `asChild` / `Slot`
Allow buttons, cards, and list items to render as links (`<a>` or Next.js `<Link>`) without wrapping extra redundant DOM elements:

```tsx
import { Slot } from "@radix-ui/react-slot";

export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  asChild?: boolean;
}

export const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ asChild = false, className, ...props }, ref) => {
    const Comp = asChild ? Slot : "button";
    return <Comp className={cn(buttonVariants(), className)} ref={ref} {...props} />;
  }
);

// Usage as a Link:
<Button asChild>
  <Link href="/dashboard">Go to Dashboard</Link>
</Button>
```

---

## 2. Accessible State Machine Integration
* Base interactive states on **WAI-ARIA specifications** using Radix Primitives or React Aria.
* Handle focus trapping in overlays, portal rendering at body level (`<Portal>`), and keyboard shortcuts (`Escape`, `Arrow keys`, `Space`, `Enter`).
