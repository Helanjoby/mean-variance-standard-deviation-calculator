from medical_data_visualizer import draw_cat_plot, draw_heat_map
import matplotlib.pyplot as plt

# Draw categorical plot
fig1 = draw_cat_plot()
fig1.savefig("catplot.png")

# Draw heat map
fig2 = draw_heat_map()
fig2.savefig("heatmap.png")

plt.show()