def binarySearch(data, left, right, search, result=[], r=False, l=False):
    if left > right:
        return -1
    else:
        mid = (left + right) // 2
        if data[mid] == search:
            result.append(mid)
            if data[mid + 1] == search:
                if not l:
                    result.extend(binarySearch(data, left + 1, right + 1, search, result=[], r=True))
            if data[mid - 1] == search:
                if not r:
                    result.extend(binarySearch(data, left - 1, right - 1, search, result=[], l=True))
            return sorted(result)
        elif data[mid] < search:
            return binarySearch(data, mid + 1, right, search)
        elif data[mid] > search:
            return binarySearch(data, left, mid - 1, search)



if __name__ == "__main__":
    try:
        data = [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 6, 7, 9, 9, 9, 9, 9, 10]
        left = 0
        right = len(data) - 1
        search = int(input("Insert the data you want to search (integers only): "))
        print(binarySearch(data, left, right, search))
    except Exception as error:
        print("Something's wrong, I can feel it. And here's what I've got:\n\t{}".format(error))