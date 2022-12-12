def splitAssignmentIntoRanges(pair_assignments: str) -> list:
    return pair_assignments.split(",")

def areFullyContainedRanges(ranges: list) -> bool:
    splitted_ranges = [aRange.split("-") for aRange in ranges]
    return isRangeContainedInto(splitted_ranges[0], splitted_ranges[1]) or isRangeContainedInto(splitted_ranges[1], splitted_ranges[0])

def isRangeContainedInto(test_range: list, container_range: list) -> bool:
    container = range(int(container_range[0]), int(container_range[1])+1)
    return int(test_range[0]) in container and int(test_range[1]) in container

print(areFullyContainedRanges(["1-5", "0-6"]))


