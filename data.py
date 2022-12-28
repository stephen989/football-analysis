os.chdir("C:/Users/Steph/ball/datasets")
features = pd.read_csv("features.csv", nrows = 100000, index_col=0)
actions = pd.read_csv("actions.csv", nrows = 100000, index_col=0)

actions_corners = filter(actions, "type_name", "corner_crossed")
corner_is = list(actions_corners.index)

mask = ((actions["type_name"] == "corner_crossed")|(actions["type_name"].shift(1) == "corner_crossed")|(actions["type_name"].shift(2) == "corner_crossed"))
sum(mask)
ca = actions[mask]
l = [actions["type_name"].shift(i) == "corner_crossed" for i in range(5)]
l[0]
len(a)

print(features.head())
print(features.shape)

# features.columns
# features.to_csv("features_1000.csv")

corners = filter(features, 'type_name-0', 'corner_crossed')
features['type_name-0'].unique()
corners['type_name-1'].unique()

take_on = filter(corners, 'type_name-1', 'take_on')


shots = filter(features, 'type_name-0', "shot")
goals = filter(shots, 'result_name-0', "success")

plt.scatter(corners['start_x-0'], corners['start_y-0'])
plt.show()
grid_shots, _, _ = np.histogram2d(shots['start_x-0'], shots['start_y-0'], bins=[gridx[0], gridy[:,0]])
grid_goals, _, _ = np.histogram2d(goals['start_x-0'], goals['start_y-0'], bins=[gridx[0], gridy[:,0]])
grid_shot_success = np.divide(grid_goals, grid_shots, out = np.zeros_like(grid_goals), where=grid_shots!=0)



fig, ax = plt.subplots()
graphing.pitch(ax)
ax.pcolormesh(gridx, gridy, grid_shot_success.T, cmap="YlGn")
plt.show()




plt.clf()
plt.grid(True)
plt.pcolormesh(gridx, gridy, grid_shot_success.T, cmap="YlGn")
plt.plot(*pitch, color="black")
plt.plot(*box, color = "black")
#plt.scatter(shots['start_x-0'], shots['start_y-0'], edgecolors = "orange", marker='o', facecolors='none')
#plt.scatter(goals['start_x-0'], goals['start_y-0'], edgecolors = "red", marker='o', facecolors='none')
plt.show()
gridx
grid
grid_shot_success.shape

for i, row in enumerate(grid_shot_success):
	x = (gridx[0][i]+gridx[0][i+1])/2
	for j, val in enumerate(row):
		y = (gridy[j][0]+gridy[j+1][0])/2
		plt.text(x, y, f"{val:.2f}", ha='center', va="center")
		print(gridx[0][i], gridy[j][0], str(val))
plt.show()
help(plt.text)

grid_goals/(grid_shots)





