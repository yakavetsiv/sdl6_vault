---
tags:
  - ai
  - type/skill
  - visualization
  - sdl6
name: research-plots
description: "Use this skill for creating, formatting, and reviewing publication-quality research figures with statistics for high-profile journals (Nature, Science, Cell, and their family journals), and for reproducing the SDL6 reproducibility repository R plot style. Triggers on: 'publication figure', 'research plot', 'journal figure', 'Nature figure', 'Science figure', 'plot for paper', 'format statistics', 'error bars', 'p-value plot', 'manuscript figure', 'reproducibility plot', 'CV plot', 'robot plot', 'participant plot', or any request to make or improve a scientific figure intended for submission. Covers technical specs (size, DPI, font, color), statistical display standards, plot type selection, and Python/R code templates."
tags:
  - ai
  - type/skill
  - sdl6
---

# Research Plot Formatting Skill
## For Nature, Science, Cell & High-Profile Journals

---

## 1. Figure Size Specifications

### Nature (and Nature family journals)

| Column | Width (mm) | Width (inches) |
|--------|-----------|----------------|
| 1-column | 88 mm | 3.46 in |
| 1.5-column | 120 mm | 4.72 in |
| 2-column (full) | 180 mm | 7.09 in |

- **Max height:** 247 mm (full page)
- **Panel labels:** uppercase bold (A, B, C…), 8 pt, top-left of each panel

### Science / AAAS

| Column | Width (inches) | Width (cm) |
|--------|---------------|------------|
| 1-column | 3.5 in | 9 cm |
| 1.5-column | 5.0 in | 12.7 cm |
| 2-column (full) | 7.3 in | 18.4 cm |

- **Max height:** 9 in (full page)
- **Panel labels:** lowercase bold italic (a, b, c…), 8 pt

### Cell Press

| Column | Width (mm) |
|--------|-----------|
| 1-column | 85 mm |
| 1.5-column | 114 mm |
| 2-column | 174 mm |

- **Max height:** 235 mm

---

## 2. Resolution & File Format

| Use case | DPI | Format |
|----------|-----|--------|
| Line art (graphs, diagrams) | 1200 dpi | TIFF, EPS, PDF, SVG |
| Halftone (photographs) | 300 dpi | TIFF |
| Combination (line + photo) | 600 dpi | TIFF, EPS, PDF |
| Vector (preferred) | N/A | EPS, PDF, SVG, AI |

**Rules:**
- Vector format always preferred — lines, arrows, text remain editable for journal resizing
- File size max: **10 MB** per figure
- RGB color mode for online; journal auto-converts to CMYK for print
- Do NOT embed fonts — outline all text in vector files

---

## 3. Typography

| Element | Font | Size | Style |
|---------|------|------|-------|
| Panel labels (Nature) | Helvetica/Arial | 8 pt | **Bold, upright** |
| Panel labels (Science) | Helvetica/Myriad | 8 pt | **Bold italic** |
| Axis titles | Arial/Helvetica | 7 pt | Regular |
| Tick labels | Arial/Helvetica | 5–7 pt | Regular |
| Legend text | Arial/Helvetica | 5–7 pt | Regular |
| Annotations | Arial/Helvetica | ≥ 5 pt | Regular |

**Rules:**
- Minimum text size: **5 pt** (printed, not screen)
- Maximum text size: **7 pt** (all non-panel-label text)
- Sans-serif only — Helvetica preferred for Nature, Myriad for Science revised manuscripts
- No decorative fonts; no Times New Roman in figures

---

## 4. Color Standards

### Colorblind-Safe Palettes (Required by Nature)

```python
# Okabe-Ito palette — universal colorblind safe
OKABE_ITO = {
    "black":          "#000000",
    "orange":         "#E69F00",
    "sky_blue":       "#56B4E9",
    "bluish_green":   "#009E73",
    "yellow":         "#F0E442",
    "blue":           "#0072B2",
    "vermillion":     "#D55E00",
    "reddish_purple": "#CC79A7",
}

# Viridis — sequential data, heatmaps
# Use: plt.cm.viridis / "viridis" colormap

# Categorical (max 6 classes without texture)
NATURE_CATEGORICAL = ["#0072B2", "#E69F00", "#009E73", "#D55E00", "#CC79A7", "#56B4E9"]
```

**Rules:**
- NEVER use red-green combinations (most common colorblindness: deuteranopia)
- NEVER use rainbow/jet colormap for sequential data
- Use pattern/texture + color for >6 categories or print-only figures
- Check figures with colorblindness simulator (e.g., Coblis, Color Oracle)
- Provide keys/keylines in figure, not just color descriptions in captions

### Color Roles
- **Black/dark gray:** axes, tick marks, annotation lines
- **White:** backgrounds, type over dark image areas
- **Color:** data series only — not decorative fills or chart junk

---

## 5. Statistical Display Standards

### Error Bars — Mandatory Labeling

Always specify in caption. Never leave ambiguous.

| Measure | Use when | Caption phrase |
|---------|----------|----------------|
| SD (standard deviation) | Showing data spread/variability | "Error bars, SD" |
| SEM (standard error of mean) | Showing precision of mean estimate | "Error bars, SEM" |
| 95% CI | Preferred for effect size interpretation | "Error bars, 95% CI" |
| IQR | Non-parametric / skewed data | "Boxes show IQR; whiskers, 10th–90th percentile" |

**Rules:**
- Error bars only for **independently repeated experiments** — NOT technical replicates of one experiment
- State N (sample size) in legend: "n = 12 mice" or "n = 6 independent experiments"
- Distinguish biological replicates (N) from technical replicates (n)

### P-value Reporting

```
Preferred (Nature, Cell): exact values — p = 0.023, p = 0.001
Acceptable threshold notation: p < 0.001
Avoid: p < 0.05 without exact value; asterisks alone without values

Asterisk convention (if used — must define in caption):
  * p < 0.05
  ** p < 0.01
  *** p < 0.001
  **** p < 0.0001
  ns = not significant (always show, never omit ns comparisons)
```

**Statistical test requirement:** Name the test in caption or Methods:
> "Two-tailed unpaired Student's t-test. ***p < 0.001, ns = not significant."

### Effect Size — Strongly Recommended

Report alongside p-values. P alone is insufficient for high-profile journals.

| Comparison type | Effect size metric |
|----------------|-------------------|
| Two groups (continuous) | Cohen's d, Hedges' g |
| Correlation | Pearson r, Spearman ρ |
| ANOVA | η² (eta-squared), ω² |
| Categorical | Odds ratio, relative risk |
| Survival | Hazard ratio (HR) with 95% CI |

### Confidence Intervals

- Report 95% CI for all primary effect estimates
- Format: "mean ± 95% CI" or "HR = 2.3 (95% CI: 1.4–3.8)"
- CI preferred over p-value alone for Nature and Science

---

## 6. Plot Type Selection

### Replace Bar Graphs When Possible

| Instead of | Use | Why |
|-----------|-----|-----|
| Bar graph (n < 20) | Dot plot / strip plot | Shows individual data points |
| Bar graph (n ≥ 20) | Violin or box-and-whisker | Shows distribution shape |
| Stacked bar (proportions) | Mosaic plot or waffle | Avoids part-whole distortion |
| Line graph (categories) | Connected dot plot | Clearer for small n |

### Plot Type → Use Case Map

```
Scatter plot        → Correlation, regression, individual data points
Box-and-whisker     → Distribution comparison, n ≥ 8 per group
Violin plot         → Distribution shape, large n (≥ 20)
Strip/dot plot      → Small n (< 20), show all points
Heatmap             → Matrix data, expression data, correlation matrices
Kaplan-Meier curve  → Survival/time-to-event data (must include at-risk table)
Forest plot         → Meta-analysis, multiple effect estimates
ROC curve           → Classifier performance (include AUC ± 95% CI)
Volcano plot        → Differential expression / GWAS (label top hits)
```

---

## 7. Axis & Legend Standards

### Axes
- Label ALL axes with units in parentheses: `Time (min)`, `Expression (log₂ FC)`
- Tick marks required; tick labels must match axis label units
- Start at zero ONLY if zero is meaningful — do not force zero for fold-change data
- Use break symbols (≠) when axis is interrupted
- Log scale: label as `log₁₀(value)` or use log-transformed axis explicitly

### Legends
- Inside figure box only if space permits and does not obscure data
- Otherwise: below or to right of panel
- List all groups/conditions — do not rely solely on color
- Font: 5–7 pt, matching axis labels

### Scale Bars (Microscopy)
- White bar over darker region of image
- Label: length + unit directly on bar (e.g., "50 μm")
- Never use a separate legend entry for scale bar

---

## 8. Multi-Panel Layout

```
Standard layout rules:
- Consistent margins between panels (recommend 2–5 mm gap)
- All panels same height within a row unless explicitly justified
- Panel label position: top-left corner, 1–2 mm from edge
- Align axes across related panels (same x-scale for time series)
- White space > crowded panels — reduce data density before font size
```

### Composite figure assembly (recommended tools):
- Adobe Illustrator — industry standard, full vector control
- Inkscape — free, vector, good for EPS/SVG
- Python: `matplotlib.gridspec` or `plt.subplot_mosaic()`
- R: `patchwork`, `cowplot`

---

## 9. Python Code Templates

### Global rcParams for Nature-Style Figures

```python
import matplotlib as mpl
import matplotlib.pyplot as plt

# Nature single-column figure
NATURE_1COL_IN = 3.46   # 88 mm
NATURE_2COL_IN = 7.09   # 180 mm

def set_nature_style():
    mpl.rcParams.update({
        # Font
        "font.family":        "Arial",
        "font.size":          7,
        "axes.titlesize":     7,
        "axes.labelsize":     7,
        "xtick.labelsize":    6,
        "ytick.labelsize":    6,
        "legend.fontsize":    6,

        # Lines & ticks
        "axes.linewidth":     0.75,
        "xtick.major.width":  0.75,
        "ytick.major.width":  0.75,
        "xtick.minor.width":  0.5,
        "ytick.minor.width":  0.5,
        "xtick.major.size":   3,
        "ytick.major.size":   3,
        "xtick.direction":    "out",
        "ytick.direction":    "out",
        "lines.linewidth":    1.0,

        # Layout
        "figure.dpi":         300,
        "savefig.dpi":        600,
        "savefig.bbox":       "tight",
        "savefig.pad_inches": 0.02,

        # No top/right spines
        "axes.spines.top":    False,
        "axes.spines.right":  False,
    })

set_nature_style()
```

### Single-Column Figure Template

```python
fig, ax = plt.subplots(figsize=(NATURE_1COL_IN, 2.2))  # width × height in inches

# Okabe-Ito colors
COLORS = ["#0072B2", "#E69F00", "#009E73", "#D55E00"]

# Example: scatter + regression
import numpy as np
from scipy import stats

x = np.array([...])
y = np.array([...])
groups = np.array([...])  # 0, 1, 2...

for i, (grp, color) in enumerate(zip(np.unique(groups), COLORS)):
    mask = groups == grp
    ax.scatter(x[mask], y[mask], c=color, s=10, alpha=0.8,
               linewidths=0, label=f"Group {grp}")

slope, intercept, r, p, se = stats.linregress(x, y)
ax.plot(x, slope*x + intercept, color="black", lw=1, ls="--")

ax.set_xlabel("Variable X (units)")
ax.set_ylabel("Variable Y (units)")
ax.legend(frameon=False, loc="upper left")

# Annotation — p-value and r
ax.text(0.05, 0.95, f"r = {r:.2f}, p = {p:.3f}",
        transform=ax.transAxes, va="top", fontsize=6)

fig.savefig("figure1a.pdf", format="pdf")   # vector for submission
fig.savefig("figure1a.tiff", dpi=600)       # raster backup
```

### Box/Strip Plot with Statistics

```python
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy import stats

def plot_groups_with_stats(data, group_col, value_col, ax,
                            colors=None, test="ttest"):
    """
    Strip plot + box overlay + p-value bracket.
    Shows individual points — recommended for n < 20.
    """
    groups = data[group_col].unique()
    colors = colors or ["#0072B2", "#E69F00", "#009E73", "#D55E00"]

    for i, (grp, color) in enumerate(zip(groups, colors)):
        vals = data.loc[data[group_col] == grp, value_col].dropna()
        # Jitter x
        import numpy as np
        jitter = np.random.uniform(-0.15, 0.15, len(vals))
        ax.scatter(np.full(len(vals), i) + jitter, vals,
                   c=color, s=8, alpha=0.7, zorder=3, linewidths=0)
        # Box
        bp = ax.boxplot(vals, positions=[i], widths=0.3,
                        patch_artist=True, zorder=2,
                        boxprops=dict(facecolor="none", color=color, lw=1),
                        medianprops=dict(color=color, lw=1.5),
                        whiskerprops=dict(color=color, lw=0.75),
                        capprops=dict(color=color, lw=0.75),
                        flierprops=dict(marker=""))
        # N label
        ax.text(i, vals.min() - 0.05 * vals.ptp(),
                f"n={len(vals)}", ha="center", va="top", fontsize=5)

    # P-value brackets (all pairwise)
    if len(groups) == 2:
        g1 = data.loc[data[group_col] == groups[0], value_col].dropna()
        g2 = data.loc[data[group_col] == groups[1], value_col].dropna()
        if test == "ttest":
            _, p = stats.ttest_ind(g1, g2)
        else:
            _, p = stats.mannwhitneyu(g1, g2, alternative="two-sided")

        y_max = max(g1.max(), g2.max()) * 1.1
        ax.plot([0, 0, 1, 1], [y_max, y_max*1.02, y_max*1.02, y_max],
                lw=0.75, color="black")
        p_str = f"p = {p:.3f}" if p >= 0.001 else "p < 0.001"
        ax.text(0.5, y_max * 1.03, p_str, ha="center", va="bottom", fontsize=6)

    ax.set_xticks(range(len(groups)))
    ax.set_xticklabels(groups)
    return ax
```

### Error Bar Plot (Means ± 95% CI)

```python
import numpy as np
from scipy import stats

def plot_means_ci(data_dict, ax, colors=None):
    """
    data_dict: {"GroupA": array, "GroupB": array, ...}
    Plots mean ± 95% CI — preferred over SEM for Nature/Science.
    """
    colors = colors or ["#0072B2", "#E69F00", "#009E73"]
    labels, means, ci_low, ci_high = [], [], [], []

    for i, (label, vals) in enumerate(data_dict.items()):
        n = len(vals)
        m = np.mean(vals)
        se = stats.sem(vals)
        ci = se * stats.t.ppf(0.975, df=n-1)
        labels.append(label)
        means.append(m)
        ci_low.append(ci)
        ci_high.append(ci)

    x = np.arange(len(labels))
    for i, (m, cl, ch, color) in enumerate(zip(means, ci_low, ci_high, colors)):
        ax.errorbar(x[i], m, yerr=[[cl], [ch]],
                    fmt="o", color=color, capsize=3,
                    capthick=0.75, elinewidth=0.75, ms=5)

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("Mean ± 95% CI")
    return ax
```

### Heatmap (Expression / Correlation)

```python
import seaborn as sns

def plot_heatmap(matrix_df, ax, cmap="viridis", center=None):
    """
    matrix_df: rows = features, cols = samples/conditions
    For correlation matrices: cmap="RdBu_r", center=0
    For expression: cmap="viridis"
    """
    g = sns.heatmap(
        matrix_df,
        ax=ax,
        cmap=cmap,
        center=center,
        linewidths=0,           # no cell borders (cleaner for large matrices)
        yticklabels=True,
        xticklabels=True,
        cbar_kws={"shrink": 0.5, "label": "Value"},
    )
    ax.tick_params(labelsize=5, length=2)
    return ax
```

---

## 10. R Code Templates

### SDL6 Reproducibility Repository Plot Style

Use this style when working inside the SDL6 reproducibility repository or when the user asks to match the existing R plots. The house style is compact, data-first, and optimized for reports/slides rather than decorative publication layouts.

Core conventions from `scripts/plot_functions.R`, `scripts/robot_plot_functions.R`, and `scripts/compare_human_robot_cv.R`:

- Use `theme_bw()` plus a shared `common_theme`.
- Keep text small and compact: axis text 5 pt, axis titles 6 pt, plot titles 7 pt bold, facet strips 5 pt bold, legend text/title 4 pt.
- Remove major/minor panel grids; keep the panel border from `theme_bw()`.
- Put legends at the top by default, horizontal, left-justified, with very small keys and spacing.
- Save standard report plots as 300 dpi PNG, usually `12 x 5 cm` or `12 x 8 cm`, with `bg = "transparent"` unless the plot contains dense white layout or image-derived material.
- Show raw observations with jittered points. For small-N comparisons, pair boxplots or medians with individual points.
- For CV and median CV, use log10 y scales and preserve the 5% CV performance threshold as a dashed reference line.
- Use `scale_color_brewer(palette = "Dark2")` / `scale_fill_brewer(palette = "Dark2")` for categories; use `Set1` for many robot IDs and blue-red gradients for target volume only when the variable is ordered.
- Use point shape to encode run number: `scale_shape_manual(values = c(1, 2, 3, 4))` or filled symbols for volume-accuracy plots.
- Add concise in-panel statistics where useful: `R²`, Pearson `r`, median CV, median time, or MAE.
- Use axis padding helpers instead of hard-coded maxima, except volume accuracy plots where fixed 0-250 µL axes and `coord_fixed()` make the identity line interpretable.

```r
library(ggplot2)
library(dplyr)

common_theme <- theme(
  axis.text = element_text(size = 5),
  axis.title = element_text(size = 6, face = "bold"),
  title = element_text(size = 7, face = "bold"),
  strip.text = element_text(size = 5, face = "bold"),
  legend.text = element_text(size = 4),
  legend.title = element_text(size = 4, face = "bold"),
  panel.grid.major = element_blank(),
  panel.grid.minor = element_blank(),
  legend.key.size = unit(0.04, "cm"),
  legend.margin = margin(0, 0, 0, 0),
  legend.spacing = unit(0.03, "cm"),
  legend.position = "top",
  legend.box.margin = margin(0, 0, 0, 0),
  plot.margin = margin(4, 4, 4, 4),
  legend.box.just = "left",
  legend.justification = "left",
  legend.direction = "horizontal",
  legend.box = "vertical",
  legend.text.align = 0,
  legend.box.spacing = unit(0.03, "cm")
)

save_repo_plot <- function(p, save, save_folder, filename,
                           width = 12, height = 5, bg = "transparent") {
  if (!save) return(NULL)
  if (!dir.exists(save_folder)) dir.create(save_folder, recursive = TRUE)
  if (is.null(filename)) filename <- paste0("plot_", Sys.Date(), ".png")
  save_path <- file.path(save_folder, filename)
  ggsave(
    file = save_path,
    plot = p,
    device = "png",
    dpi = 300,
    width = width,
    height = height,
    units = "cm",
    bg = bg
  )
  cat("Plot saved to:", save_path, "\n")
  save_path
}

calculate_axis_limits <- function(data, y_col, x_col = NULL,
                                  y_padding = 0.3, x_padding = 0.1) {
  y_min <- max(min(data[[y_col]], na.rm = TRUE) * 0.9, 0.1)
  y_max <- max(data[[y_col]], na.rm = TRUE) * (1 + y_padding)
  if (!is.null(x_col)) {
    x_min <- max(min(data[[x_col]], na.rm = TRUE) * 0.9, 0)
    x_max <- max(data[[x_col]], na.rm = TRUE) * (1 + x_padding)
    return(list(y_min = y_min, y_max = y_max, x_min = x_min, x_max = x_max))
  }
  list(y_min = y_min, y_max = y_max)
}
```

#### SDL6 CV Comparison Template

Use this for participant/robot CV comparisons. Filter invalid CV values before plotting, use a log y-axis, and keep the threshold visible.

```r
plot_cv_comparison_repo <- function(df, save = FALSE, save_folder = "reports/",
                                    filename = "cv_comparison.png") {
  df <- df %>% filter(!is.na(cv), cv > 0)
  limits <- calculate_axis_limits(df, "cv")

  stats <- df %>%
    group_by(group) %>%
    summarise(
      median_cv = median(cv, na.rm = TRUE),
      mean_cv = mean(cv, na.rm = TRUE),
      sd_cv = sd(cv, na.rm = TRUE),
      n = n(),
      .groups = "drop"
    )

  p <- ggplot(df, aes(x = group, y = cv, fill = group)) +
    geom_boxplot(alpha = 0.7, width = 0.5, outlier.shape = NA) +
    geom_jitter(width = 0.2, height = 0, alpha = 0.5, size = 1, shape = 21) +
    geom_hline(yintercept = 5, color = "red", linetype = "dashed",
               alpha = 0.5, linewidth = 0.2) +
    geom_text(
      data = stats,
      aes(x = group, y = limits$y_max * 0.35,
          label = sprintf("Median = %.2f%%", median_cv)),
      size = 2,
      inherit.aes = FALSE
    ) +
    theme_bw() +
    common_theme +
    theme(
      legend.position = "none",
      axis.text.x = element_text(angle = 45, hjust = 1)
    ) +
    scale_y_log10(
      limits = c(limits$y_min, limits$y_max),
      breaks = c(0.1, 0.5, 1, 5, 10, 50, 100),
      labels = c("0.1", "0.5", "1", "5", "10", "50", "100")
    ) +
    scale_fill_brewer(palette = "Dark2") +
    labs(
      x = "Group",
      y = "Coefficient of Variation (%)",
      title = "CV Comparison"
    )

  save_repo_plot(p, save, save_folder, filename, width = 8, height = 6)
  p
}
```

#### SDL6 Median CV vs Continuous Variable Template

Use this pattern for median CV vs price, time, experience, or other continuous metadata.

```r
plot_median_cv_scatter_repo <- function(df_with_cv, x_col, x_label,
                                        color_col = "price_category",
                                        save = FALSE,
                                        save_folder = "reports/",
                                        filename = "median_cv_scatter.png") {
  df_median <- df_with_cv %>%
    filter(!is.na(cv), cv > 0, !is.na(.data[[x_col]])) %>%
    mutate(
      x_value = .data[[x_col]],
      color_value = .data[[color_col]]
    ) %>%
    group_by(id, run, solvent, color_value, x_value) %>%
    summarise(median_cv = median(cv, na.rm = TRUE), n = n(), .groups = "drop")

  stats_values <- df_median %>%
    group_by(solvent) %>%
    summarise(
      r2 = round(summary(lm(median_cv ~ x_value))$r.squared, 3),
      pearson_cor = round(cor(median_cv, x_value, use = "complete.obs"), 3),
      overall_median_cv = round(median(median_cv, na.rm = TRUE), 2),
      .groups = "drop"
    )

  limits <- calculate_axis_limits(df_median, "median_cv", "x_value")

  p <- ggplot(df_median, aes(x = x_value, y = median_cv)) +
    geom_point(aes(color = color_value, shape = factor(run)),
               alpha = 0.95, size = 1, stroke = 0.3) +
    geom_smooth(method = "lm", se = TRUE, color = "red",
                alpha = 0.2, linewidth = 0.2) +
    geom_hline(yintercept = 5, color = "blue", linetype = "dashed",
               alpha = 0.5, linewidth = 0.2) +
    facet_wrap(~ solvent, scales = "free") +
    geom_text(
      data = stats_values,
      aes(
        x = limits$x_max,
        y = limits$y_max,
        label = sprintf("R² = %.3f\nr = %.3f\nMedian CV = %.2f%%",
                        r2, pearson_cor, overall_median_cv)
      ),
      hjust = 1,
      vjust = 1,
      size = 1.5,
      color = "black",
      fontface = "bold",
      inherit.aes = FALSE
    ) +
    theme_bw() +
    common_theme +
    scale_color_brewer(palette = "Dark2") +
    scale_fill_brewer(palette = "Dark2") +
    scale_shape_manual(values = c(1, 2, 3, 4)) +
    scale_x_continuous(limits = c(limits$x_min, limits$x_max)) +
    scale_y_log10(
      limits = c(limits$y_min, limits$y_max),
      breaks = c(0.1, 0.5, 1, 5, 10, 50, 100),
      labels = c("0.1", "0.5", "1", "5", "10", "50", "100")
    ) +
    labs(
      x = x_label,
      y = "Median CV (%)",
      title = paste("Median CV vs", x_label),
      color = "Category",
      shape = "Run"
    ) +
    guides(color = guide_legend(nrow = 1), shape = guide_legend(nrow = 1))

  save_repo_plot(p, save, save_folder, filename, width = 12, height = 5)
  p
}
```

#### SDL6 Volume Accuracy Template

For volume accuracy, use a fixed 1:1 coordinate system with the identity line, not a log axis.

```r
plot_volume_accuracy_repo <- function(df_with_cv, save = FALSE,
                                      save_folder = "reports/",
                                      filename = "volume_accuracy.png") {
  df_plot <- df_with_cv %>%
    filter(!is.na(vol_theor_calc), !is.na(target_volume))

  stats_values <- df_plot %>%
    group_by(solvent) %>%
    summarise(
      r2 = round(summary(lm(vol_theor_calc ~ target_volume))$r.squared, 3),
      pearson_cor = round(cor(vol_theor_calc, target_volume, use = "complete.obs"), 3),
      mae = round(mean(abs(vol_theor_calc - target_volume), na.rm = TRUE), 2),
      .groups = "drop"
    )

  p <- ggplot(df_plot, aes(x = target_volume, y = vol_theor_calc)) +
    geom_abline(intercept = 0, slope = 1, color = "red",
                linetype = "dashed", alpha = 0.7, linewidth = 0.5) +
    geom_point(aes(color = factor(id), shape = factor(run)),
               alpha = 0.6, size = 1.5, stroke = 0.3) +
    geom_smooth(method = "lm", se = TRUE, color = "blue",
                alpha = 0.2, linewidth = 0.5) +
    facet_wrap(~ solvent) +
    geom_text(
      data = stats_values,
      aes(x = 55, y = 240,
          label = sprintf("R² = %.3f\nr = %.3f\nMAE = %.2f µL",
                          r2, pearson_cor, mae)),
      hjust = 0,
      vjust = 1,
      size = 2,
      color = "black",
      fontface = "bold",
      inherit.aes = FALSE
    ) +
    theme_bw() +
    common_theme +
    theme(legend.position = "right") +
    scale_color_brewer(palette = "Set1") +
    scale_shape_manual(values = c(16, 17, 15, 3)) +
    scale_x_continuous(limits = c(0, 250), breaks = c(50, 100, 150, 200)) +
    scale_y_continuous(limits = c(0, 250), breaks = c(50, 100, 150, 200)) +
    coord_fixed(ratio = 1) +
    labs(
      x = "Target Volume (µL)",
      y = "Calculated Volume (µL)",
      title = "Volume Accuracy: Calculated vs Target",
      color = "Robot ID",
      shape = "Run"
    )

  save_repo_plot(p, save, save_folder, filename,
                 width = 18, height = 14, bg = "white")
  p
}
```

### ggplot2 Nature Theme

```r
library(ggplot2)
library(ggpubr)

# Okabe-Ito palette
okabe_ito <- c("#0072B2","#E69F00","#009E73","#D55E00","#CC79A7","#56B4E9","#F0E442")

nature_theme <- theme_classic(base_size = 7, base_family = "Arial") +
  theme(
    axis.line        = element_line(linewidth = 0.5),
    axis.ticks       = element_line(linewidth = 0.5),
    axis.ticks.length = unit(2, "pt"),
    legend.position  = "right",
    legend.key.size  = unit(8, "pt"),
    legend.text      = element_text(size = 6),
    plot.margin      = margin(2, 2, 2, 2, "mm"),
    strip.background = element_blank(),
    strip.text       = element_text(size = 7, face = "bold")
  )

# Save at correct dimensions
ggsave("figure1.pdf", plot = p, width = 88, height = 60, units = "mm",
       device = cairo_pdf)
ggsave("figure1.tiff", plot = p, width = 88, height = 60, units = "mm",
       dpi = 600, compression = "lzw")
```

### Strip + Box Plot with ggpubr Stats

```r
library(ggplot2)
library(ggpubr)
library(rstatix)

# Stat test annotation — exact p-values
stat_test <- df %>%
  t_test(value ~ group) %>%
  add_significance() %>%
  add_xy_position(x = "group")

p <- ggplot(df, aes(x = group, y = value, color = group)) +
  geom_boxplot(outlier.shape = NA, width = 0.4, linewidth = 0.5) +
  geom_jitter(width = 0.1, size = 1, alpha = 0.7, stroke = 0) +
  scale_color_manual(values = okabe_ito) +
  stat_pvalue_manual(stat_test, label = "p = {p}", tip.length = 0.01,
                     size = 2, bracket.size = 0.3) +
  nature_theme +
  guides(color = "none")   # remove redundant legend if x-axis labels suffice
```

---

## 11. Caption Checklist

Every figure caption must include:

- [ ] Panel label definitions (A–F, etc.)
- [ ] Full description of what each panel shows
- [ ] Statistical test name(s) used
- [ ] N per group (biological replicates)
- [ ] n per group (technical replicates, if different)
- [ ] Error bar definition ("Error bars, mean ± SD")
- [ ] P-value threshold definitions if asterisks used
- [ ] Scale bar value and unit (microscopy)
- [ ] Number of independent experiments if pooled
- [ ] Software/package versions (Methods section, not caption)

**Template:**
> "(A) [Panel description]. (B) [Panel description]. n = [N] [unit] per group from [X] independent experiments. Error bars, mean ± 95% CI. Statistical comparisons by two-tailed unpaired t-test. ***p < 0.001; ns, not significant (p ≥ 0.05)."

---

## 12. Figure Integrity Rules

- **No selective cropping** that removes relevant signal
- **No brightness/contrast adjustments** that eliminate data (apply equally across whole image)
- **No splicing** lanes/panels without explicit dividing line and caption disclosure
- **No duplication** of image panels across figures without disclosure
- **Western blots:** show full blot in Supplementary; cropped version in main figure with clear crop marks
- **Microscopy:** state acquisition parameters (objective, scale bar, N fields imaged)

Nature and Science require a statistics/methods checklist at submission — prepare alongside figure.

---

## 13. Pre-submission QA Checklist

```
Dimensions:
[ ] Width matches 1-col / 1.5-col / 2-col spec for target journal
[ ] Max height not exceeded
[ ] All panels consistent margins

Resolution & format:
[ ] Line art ≥ 1200 dpi OR vector format submitted
[ ] Photos ≥ 300 dpi
[ ] File size < 10 MB per figure
[ ] Fonts outlined (vector) OR embedded (PDF)

Typography:
[ ] All text ≥ 5 pt at print size
[ ] Panel labels correct style (Nature: bold upright / Science: bold italic)
[ ] No serif fonts in figure

Color:
[ ] Colorblind simulation passed (Coblis or Color Oracle)
[ ] No red-green combinations
[ ] No rainbow/jet colormap on sequential data
[ ] RGB color mode

Statistics:
[ ] Error bars defined in caption
[ ] N stated per group
[ ] Exact p-values reported (or p < 0.001 for very small)
[ ] Statistical test named
[ ] Effect size reported for primary comparisons
[ ] ns (not significant) shown, not omitted

Content:
[ ] All axes labeled with units
[ ] All panel labels present
[ ] Legend complete (no color-only identification)
[ ] Scale bars on all microscopy panels
```

---

## Sources

- [Nature Formatting Guide](https://www.nature.com/nature/for-authors/formatting-guide)
- [Nature Research Figure Guide — Preparing Figures](https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/)
- [Science AAAS — Instructions for Preparing Initial Manuscript](https://www.science.org/content/page/instructions-preparing-initial-manuscript)
- [Nature Figure Guidelines 2025–2026 with Python Templates (PlotIvy)](https://plotivy.app/blog/nature-journal-figure-guidelines-2025)
- [Nature, Science & Cell Figure Guidelines: Size, DPI, Fonts (ConceptViz)](https://conceptviz.app/blog/how-to-make-figures-for-nature-science-journals)
- [Journal Figure Requirements Cheat Sheet 2026 (PlotIvy)](https://plotivy.app/blog/journal-figure-requirements-cheat-sheet)
- [New Author Guidelines for Statistical Reporting in Experimental Biology](https://www.researchgate.net/publication/338218825_New_Author_Guidelines_for_Displaying_Data_and_Reporting_Data_Analysis_and_Statistical_Methods_in_Experimental_Biology)
- [Improving Statistical Reporting in Psychology — Nature Communications Psychology](https://www.nature.com/articles/s44271-025-00356-w)
- [What exactly is N in cell culture and animal experiments? (biorXiv)](https://www.biorxiv.org/content/10.1101/183962.full.pdf)
