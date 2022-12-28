import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd





def pitch(ax, color = "black"):
	sidelines = [[0,105,105,0, 0], [0,0,68,68, 0]]
	box_left = [[0, 16.5, 16.5, 0, 0], [14, 14, 54, 54, 14]]
	box_right = [[105-0, 105-16.5, 105-16.5, 105-0, 105-0], [14, 14, 54, 54, 14]]
	sixbox_left = [[0, 5.5, 5.5, 0], [25, 25, 43, 43]]
	sixbox_right = [[105-0, 105-5.5, 105-5.5, 105-0], [25, 25, 43, 43]]
	goal_left = [[0, -2.44, -2.44, 0], [30, 30, 38, 38]]
	goal_right = [[105+0, 105+2.44, 105+2.44, 105+0], [30, 30, 38, 38]]

	penalty_spots = [[11, 105-11], [34, 34]]
	semi_circle =  [52.5, 34]
	halfway_line = [[52.5, 52.5], [0, 68]]
	lines = [sidelines, 
			 box_left, 
			 box_right, 
			 halfway_line, 
			 sixbox_left, 
			 sixbox_right,
			 goal_left, 
			 goal_right]
	points = [penalty_spots, semi_circle]
	for line in lines:
		ax.plot(*line, color = color)
	for point in points:
		ax.scatter(*point, color = color, s = 3)


	# penalty spots
	arc = np.linspace(-0.923, 0.923, 20)
	left_x = 11 + 9.15 * np.cos(arc)
	left_y = 34 + 9.15 * np.sin(arc)
	right_x = 105-left_x
	ax.plot(left_x, left_y, color = color)
	ax.plot(right_x, left_y, color = color)

	# centre circle
	arc = np.linspace(-3.14, 3.15, 100)
	x = 52.5 + 9.15 * np.cos(arc)
	y = 34 + 9.15 * np.sin(arc)
	ax.plot(x, y, color = color)





def centred_text(ax, gridx, gridy, vals):
	for i, row in enumerate(vals):
		x = (gridx[0][i]+gridx[0][i+1])/2
		for j, val in enumerate(row):
			y = (gridy[j][0]+gridy[j+1][0])/2
			ax.text(x, y, f"{val:.2f}", ha='center', va="center", fontdict = {'family' : 'normal', 'weight' : 'light', 'size'   : 6})
			print(gridx[0][i], gridy[j][0], str(val))

def filter(df, column, value):
	return df[df[column] == value]

if __name__ == "__main__":
	os.chdir("C:/Users/Steph/ball/datasets")
	features = pd.read_csv("features.csv", index_col=0)
	# print(features.head())
	# print(features.shape)

	# features.columns
	# features.to_csv("features_1000.csv")


	shots = filter(features, 'type_name-0', "shot")
	goals = filter(shots, 'result_name-0', "success")

	gridx, gridy = [0, 5.5, 11.25, 16.5, 25, 40, 105], [0, 14, 25, 34, 43, 54, 68]
	gridx, gridy = np.meshgrid(gridx, gridy)

	grid_shots, _, _ = np.histogram2d(shots['start_x-0'], shots['start_y-0'], bins=[gridx[0], gridy[:,0]])
	grid_goals, _, _ = np.histogram2d(goals['start_x-0'], goals['start_y-0'], bins=[gridx[0], gridy[:,0]])
	grid_shot_success = np.divide(grid_goals, grid_shots, out = np.zeros_like(grid_goals), where=grid_shots!=0)



	fig, ax = plt.subplots()
	ax.pcolormesh(gridx, gridy, grid_shot_success.T, cmap="YlGn")

	pitch(ax)
	centred_text(ax, gridx, gridy, grid_shot_success)
	plt.show() 
