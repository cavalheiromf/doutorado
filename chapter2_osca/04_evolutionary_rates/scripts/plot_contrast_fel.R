library(ggplot2)
library(dplyr)

# Data extracted from contrast_fel_summary.tsv
data <- data.frame(
  Clade = c(rep("OSCA1", 5), rep("OSCA2", 11), rep("OSCA3", 1)),
  Site = c(
    98, 181, 252, 710, 973, 
    8, 71, 76, 147, 191, 308, 394, 395, 432, 596, 720, 
    593
  ),
  Length = c(
    rep(1029, 5),
    rep(889, 11),
    rep(904, 1)
  )
)

# Set Clade as factor with desired order
data$Clade <- factor(data$Clade, levels = c("OSCA1", "OSCA2", "OSCA3"))

# Create the Lollipop plot
p <- ggplot(data) +
  # Protein backbone (alignment length)
  geom_segment(aes(x = 1, xend = Length, y = 0, yend = 0), color = "grey70", size = 3, lineend = "round") +
  # Lollipops
  geom_segment(aes(x = Site, xend = Site, y = 0, yend = 1, color = Clade), size = 1.2) +
  geom_point(aes(x = Site, y = 1, color = Clade), size = 4) +
  # Add site labels on top of the lollipops
  geom_text(aes(x = Site, y = 1.2, label = Site, color = Clade), size = 3.5, fontface = "bold", angle = 45, hjust = 0) +
  facet_wrap(~ Clade, ncol = 1, strip.position = "right") +
  theme_minimal() +
  scale_y_continuous(limits = c(-0.5, 2.0), breaks = NULL) +
  scale_color_manual(values = c("OSCA1" = "#1b9e77", "OSCA2" = "#d95f02", "OSCA3" = "#7570b3")) +
  labs(title = "Contrast-FEL: Significant Sites of Selective Divergence",
       subtitle = "Sites with significantly different evolutionary rates between V. peripherica and V. tubiflora",
       x = "Codon Position (Alignment)",
       y = NULL) +
  theme(
    plot.title = element_text(face = "bold", size = 18, hjust = 0.5),
    plot.subtitle = element_text(size = 12, hjust = 0.5, color = "grey40", margin = margin(b = 20)),
    axis.title.x = element_text(face = "bold", size = 12, margin = margin(t = 15)),
    strip.text = element_text(face = "bold", size = 14),
    panel.grid = element_blank(),
    legend.position = "none",
    plot.margin = margin(20, 20, 20, 20)
  )

# Output paths
output_png <- "/home/mfcaval/github/doutorado/analyses/04_evolutionary_rates/results/contrast_fel_sites.png"
output_svg <- "/home/mfcaval/github/doutorado/analyses/04_evolutionary_rates/results/contrast_fel_sites.svg"

# Save plots
ggsave(output_png, p, width = 12, height = 7, dpi = 300, bg = "white")
ggsave(output_svg, p, width = 12, height = 7, bg = "white")

cat("Plots saved to:\n", output_png, "\n", output_svg, "\n")
