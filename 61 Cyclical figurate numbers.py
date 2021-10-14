figurate_numbers = [dict(), dict(), dict(), dict(), dict(), dict()]
for n in range(
    19, 141
):  # 19 & 141 manually calculated as first 4-digit octfigurateonal and last 4-digit triangular number
    new_figurates = [
        str(n * (n + 1) // 2),
        str(n ** 2),
        str(n * (3 * n - 1) // 2),
        str(n * (2 * n - 1)),
        str(n * (5 * n - 3) // 2),
        str(n * (3 * n - 2)),
    ]
    for figurates in range(len(new_figurates)):
        if len(new_figurates[figurates]) == 4:
            if new_figurates[figurates][:2] not in figurate_numbers[figurates]:
                figurate_numbers[figurates][new_figurates[figurates][:2]] = set()
                figurate_numbers[figurates][new_figurates[figurates][:2]].add(
                    new_figurates[figurates][2:]
                )
            else:
                figurate_numbers[figurates][new_figurates[figurates][:2]].add(
                    new_figurates[figurates][2:]
                )


def solve(figurate_numbers):
    ret = []

    def recursion(figurates_left, tempret, suffix, master_suffix):
        nonlocal ret
        new_figurates_left, new_temp_ret = set(figurates_left), list(tempret)

        if (
            not new_figurates_left
            and suffix in figurate_numbers[5]
            and master_suffix in figurate_numbers[5][suffix]
        ):
            new_temp_ret.append(suffix)
            ret = new_temp_ret
            return

        for new_figurate in new_figurates_left:
            if suffix in figurate_numbers[new_figurate]:
                new_figurates_left.remove(new_figurate)
                new_temp_ret.append(suffix)
                for new_suffix in figurate_numbers[new_figurate][suffix]:
                    recursion(
                        new_figurates_left, new_temp_ret, new_suffix, master_suffix
                    )
                new_figurates_left.add(new_figurate)
                new_temp_ret.remove(suffix)

    for suffixes in figurate_numbers[5].values():
        for suffix in suffixes:
            master_suffix = suffix
            recursion(set(range(5)), [], suffix, master_suffix)
    return ret


answer = solve(figurate_numbers)
for i in range(len(answer)):
    answer[i] = int(answer[i] + answer[i])
print(sum(answer))
# sum of suffix *1 and suffix*100 for every suffix is equivalent b/c cyclical
