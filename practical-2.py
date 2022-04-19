import statistics

List = [10, 50, 80, 70, 49, 23, 11, 4]

minimum = min(List)
maximum = max(List)
mean = statistics.mean(List)
standard_deviation = statistics.pstdev(List)
variance = statistics.variance(List)
print(minimum)
print(maximum)
print('%.2f'%mean)
print('%.2f'%standard_deviation)
print('%.2f'%variance)


