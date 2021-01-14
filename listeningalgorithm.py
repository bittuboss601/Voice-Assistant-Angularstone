def listening_algorithm(to,from_):
    counts = []
    to = to.split(' ')
    for i in range(len(from_)):
        count = 0
        var = from_[i].split(' ')
        n = min(len(to),len(var))
        for j in range(n):
            if var[j] in to[j]:
                count += 1
        counts.append(count)
    maxm_ = max(counts)
    for i in range(len(counts)):
        if maxm_ == counts[i]:
            return from_[i]