def solution(sequence):
    dp_pm = [sequence[0]]
    dp_mp = [-sequence[0]]

    for i in range(1, len(sequence)):
        pm_add = -sequence[i] if i%2 == 1 else sequence[i]
        mp_add = sequence[i] if i%2 == 1 else -sequence[i]

        dp_pm.append(max(dp_pm[i-1], 0) + pm_add)
        dp_mp.append(max(dp_mp[i-1], 0) + mp_add)

    answer = max(max(dp_pm), max(dp_mp))
    return answer