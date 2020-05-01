import os

input_file = '/home/tecsar/matias/jetson-inference/results/INT8.csv'

totals = []
posts = []
networks = []
pres = []
valids = []
with open(input_file, 'r') as infile:
    lineCount = 0
    for line in infile:
        splitLine = line.split(',')
        if (splitLine[0]=='Total') and (float(splitLine[-2]) > 2.0) and (lineCount >= 10) and (lineCount <=110):
            valids.append(lineCount)

        if (splitLine[0]=='Total'):
            totals.append(tuple([float(splitLine[2]), float(splitLine[5])]))
            lineCount += 1
        elif (splitLine[0]=='Post-Process'):
            posts.append(tuple([float(splitLine[2]), float(splitLine[5])]))
        elif (splitLine[0]=='Network'):
            networks.append(tuple([float(splitLine[2]), float(splitLine[5])]))
        elif (splitLine[0]=='Pre-Process'):
            pres.append(tuple([float(splitLine[2]), float(splitLine[5])]))
        else:
            print('NON VALID ENTRY')

        

cpu_totals = [totals[x][0] for x in valids]
gpu_totals = [totals[x][1] for x in valids]

cpu_posts = [posts[x][0] for x in valids]
gpu_posts = [posts[x][1] for x in valids]

cpu_networks = [networks[x][0] for x in valids]
gpu_networks = [networks[x][1] for x in valids]

cpu_pres = [pres[x][0] for x in valids]
gpu_pres = [pres[x][1] for x in valids]

print(input_file.split('/')[-1])
print("Valid Frames: " + str(len(valids)) + "\n")
#TOTALS
print('Total:\tCPU: ' + str(sum(cpu_totals)/len(cpu_totals)) + '\tGPU: ' + str(sum(gpu_totals)/len(gpu_totals)) )
#POST
print('Post:\tCPU: ' + str(sum(cpu_posts)/len(cpu_posts)) + '\tGPU: ' + str(sum(gpu_posts)/len(gpu_posts)) )
#NETWORK
print('Net:\tCPU: ' + str(sum(cpu_networks)/len(cpu_networks)) + '\tGPU: ' + str(sum(gpu_networks)/len(gpu_networks)) )
#PRE
print('Pre:\tCPU: ' + str(sum(cpu_pres)/len(cpu_pres)) + '\tGPU: ' + str(sum(gpu_pres)/len(gpu_pres)) )
