pred = "/Users/heyibo/Desktop/Assertion/FSE2024/Artifact/Artifact-FocalMethodStudy/Results/rq2/IR-b1-atlas.txt"
ground = "/Users/heyibo/Desktop/Assertion/FSE2024/Artifact/ATLAS+/Testing/benchmark-1-atlas/assertLines.txt"

predictions = []
with open(pred,"r",encoding="utf-8") as f:
    predictions = f.readlines()

groundtruth = []
with open(ground,"r",encoding="utf-8") as f:
    groundtruth = f.readlines()

cor = 0
for i in range(len(predictions)):
    if(predictions[i].strip() == groundtruth[i].strip()):
        cor += 1

print(cor)