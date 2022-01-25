import numpy as np

# this mimics the return of updateAdditionalFields()
def getListOfRandomNumbers(size):
    return np.random.normal(1,1,size)

# we do not have the mean values and variances

# number of Stochastic fields
nSF = 100000

# fields for which mean and variance are needed
nFields = 7
meanFields = np.zeros(nFields);
varianceFields = np.zeros(nFields);
sumOfSquaredDifferences = np.zeros(nFields)


for i in range(nSF):
    oldMeans = meanFields
    increments = getListOfRandomNumbers(nFields)
    meanFields = oldMeans + (increments - oldMeans)/(i+1) 
    sumOfSquaredDifferences = sumOfSquaredDifferences + (increments - oldMeans)*(increments - meanFields)
    varianceFields = sumOfSquaredDifferences/(i+1)

# mean
print(meanFields)
#vairance
print(varianceFields)
# std
print(np.sqrt(varianceFields))
