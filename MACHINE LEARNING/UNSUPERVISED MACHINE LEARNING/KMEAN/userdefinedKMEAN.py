import copy
from email.base64mime import header_length
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
df = pd.DataFrame({
    'x':[12,20,28,18,29,33,24,45,45,52,51,52,55,53,55,61,64,69,72],
    'y':[39,36,30,52,54,46,55,59,63,70,66,63,58,23,14,8,19,7,24]

    # 'x':[185,170,168,179,182,188,180,180,183,180,180,177],
    # 'y':[72,56,60,68,72,77,71,70,84,88,67,76]
})

print("Step 1:installation - K initial  'means' (centriods) are genrated at randomly");

print("-------------------")
print("dataset for training")
print("-------------------")
print(df)
print("-------------------")

np.random.seed(200)
k=3

#centriodds[i] = [x,y]

centroids={
    i+1 :[np.random.randint(0,80),np.random.randint(0,80)]
    for i in range(k)
}

print("-------------------")
print("Random centroid genrated")
print(centroids)
print("-------------------")

#plotting of X and Y dataframe
fig =plt.figure(figsize=(5,5))
plt.scatter(df['x'],df['y'],color='k')

#plotting of random centriods
colmap = {1:'r',2:'g',3:'b'}
for i in centroids.keys():
    plt.scatter(*centroids[i],color=colmap[i])

print("MArvellous: Dataset with random centriod ")
plt.xlim(0,80)
plt.ylim(0,80)
plt.show()

#Assignments -k clusters are created by associating each observation with the nearest centroid

def assignments(df,centroids):

    for i in centroids.keys():
        # sqrt(x2-x1)^2 - (y2-y1)^2
        df['distance_from_{}'.format(i)]=(

            np.sqrt(
                    (df['x'] - centroids[i][0])**2 + (df['y'] - centroids[i][1])**2
            )
        )

        centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]

    df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
    df['closest'] = df['closest'].map(lambda x:int(x.lstrip('distance_from_')))
    df['color'] = df['closest'].map(lambda x:colmap[x])

    return df

print("Assignments 2-k clusters are created by associating each observation with the nearest centroid")
    
print("before assignment dataset")
print(df)
df = assignments(df,centroids)

print("first centriod = red")
print("second centroid = grreen")
print("third centroid=blue")

print("after assignment dataset")
print(df)

fig =plt.figure(figsize=(5,5))
plt.scatter(df['x'],df['y'],color=df['color'],alpha=0.5,edgecolors='k')

for i in centroids.keys():
    plt.scatter(*centroids[i],color=colmap[i])

plt.xlim(0,80)
plt.ylim(0,80)
plt.title("MArvellous: Dataset with clustring & random gentrated ")
plt.show()

#-------------

old_cenntroid =copy.deepcopy(centroids)
print("Step 3: the centroid of clusters becomes the new mean Assignment and update are repeted iteratively until convergence")

def update(k):
    print("old values of centroids")
    print(k)

    for i in centroids.keys():
        centroids[i][0] = np.mean(df[df['closest']== i]['x'])
        centroids[i][1] = np.mean(df[df['closest']== i]['y'])

    print("new values of centtroid")
    print(k)
    return k

centroids =update(centroids)


fig =plt.figure(figsize=(5,5))
ax =plt.axes()
plt.scatter(df['x'],df['y'],color=df['color'],alpha=0.5,edgecolors='k')

for i in centroids.keys():
    plt.scatter(*centroids[i],color=colmap[i])

plt.xlim(0,80)
plt.ylim(0,80)

for i in old_cenntroid.keys():
    old_x = old_cenntroid[i][0]
    old_y = old_cenntroid [i][1]

    dx = (centroids[i][0]- old_cenntroid[i][0])*0.75
    dy = (centroids[i][1]- old_cenntroid[i][1])*0.75

    ax.arrow(old_x,old_y,dx,dy,head_width=2,head_length=3,fc=colmap[i],ec=colmap[i])

plt.title("dataset with  clustring  and updated centroids")
plt.show()

#repeat assignment test 

    
print("before assignment dataset")
print(df)
df = assignments(df,centroids)

print("after assignment dataset")
print(df)

fig =plt.figure(figsize=(5,5))
plt.scatter(df['x'],df['y'],color=df['color'],alpha=0.5,edgecolors='k')

#plot result
for i in centroids.keys():
    plt.scatter(*centroids[i],color=colmap[i])

plt.xlim(0,80)
plt.ylim(0,80)
plt.title("MArvellous: Dataset with clustring & updating centroids ")
plt.show()

#continue until all assigned categories dont chnage any one
while True:
    closest_centroids = df['closest'].copy(deep=True)

    centroids =update (centroids)
    print("before assignment dataset")
    print(df)

    df = assignments(df,centroids)
    print("after assignment dataset")
    print(df)

    if closest_centroids.equals(df['closest']):
        break

print("final values of centroids")
print(centroids)


fig =plt.figure(figsize=(5,5))
plt.scatter(df['x'],df['y'],color=df['color'],alpha=0.5,edgecolors='k')

for i in centroids.keys():
    plt.scatter(*centroids[i],color=colmap[i])

plt.xlim(0,80)
plt.ylim(0,80)
plt.title("MArvellous: Final dataset with set centriods ")
plt.show()

