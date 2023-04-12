def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def median(arr):
    n = len(arr)

    if n % 2 == 0:
        return (arr[n//2 - 1] + arr[n//2]) / 2
    else:
        return arr[n//2]


sport_salaries = list(map(int, input().split()))
future_club_salaries = list(map(int, input().split()))

merged_salaries = sport_salaries + future_club_salaries
merge_sort(merged_salaries)

median_salary = median(merged_salaries)

print(
    f"O salário sugerido por Juba na primeira negociação será de {median_salary:.2f} mil reais.")
