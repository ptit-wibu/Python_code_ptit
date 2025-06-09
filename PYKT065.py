'''

import sys

# Các số nguyên tố nhỏ hơn hoặc bằng 50
ALL_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

#quy hoạch động bitmask luôn
def count_not_divisible(limit, N):
    """
    Đếm số lượng các số từ 1 đến 'limit' KHÔNG chia hết cho bất kỳ số nào trong [2, N].
    Sử dụng nguyên lý bao hàm-loại trừ.
    """
    if limit == 0:
        return 0

    # Lọc ra các số nguyên tố cần xét
    primes_to_check = [p for p in ALL_PRIMES if p <= N]

    # Số lượng số "xấu" (chia hết cho ít nhất 1 số nguyên tố)
    count_of_bad_numbers = 0

    # k là số lượng các số nguyên tố cần xét
    k = len(primes_to_check)

    # Duyệt qua tất cả các tập con không rỗng của primes_to_check bằng bitmask
    # Vòng lặp từ 1 đến 2^k - 1
    for i in range(1, 1 << k):
        product = 1
        subset_size = 0

        for j in range(k):
            # Kiểm tra xem bit thứ j có được bật trong i không
            if (i >> j) & 1:
                # Nếu có, thêm số nguyên tố thứ j vào tích
                product *= primes_to_check[j]
                subset_size += 1

        # Nếu tích vượt quá giới hạn, các tích lớn hơn cũng vậy, bỏ qua
        if product > limit:
            continue

        # Áp dụng nguyên lý bao hàm - loại trừ
        term = limit // product
        if subset_size % 2 == 1:  # Tập con có số phần tử lẻ -> cộng vào
            count_of_bad_numbers += term
        else:  # Tập con có số phần tử chẵn -> trừ đi
            count_of_bad_numbers -= term

    # Số lượng số "tốt" = tổng số - số lượng số "xấu"
    return limit - count_of_bad_numbers


def solve():
    """Hàm chính để đọc input và xử lý các test case."""
    while True:
        line = sys.stdin.readline().strip()
        if line == '-1':
            break

        try:
            L, R = map(int, line.split())
            N = int(sys.stdin.readline())

            # Kết quả = (số tốt trong [1, R]) - (số tốt trong [1, L-1])
            ans = count_not_divisible(R, N) - count_not_divisible(L - 1, N)
            print(ans)

        except (IOError, ValueError):
            break


solve()
'''
'''
import sys

# Các số nguyên tố nhỏ hơn hoặc bằng 50
ALL_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def inclusion_exclusion_recursive(limit, primes, start_index, current_product):
    """
    Hàm đệ quy tính số lượng số chia hết cho ít nhất một số trong 'primes'
    bằng nguyên lý bao hàm - loại trừ, có áp dụng nhánh cận.
    """
    count = 0
    # Lặp qua các số nguyên tố còn lại để thêm vào tích
    for i in range(start_index, len(primes)):

        # Tính tích mới
        new_product = current_product * primes[i]

        # Nhánh cận (Pruning): Nếu tích mới đã lớn hơn giới hạn,
        # thì không cần xét nó và các tích lớn hơn nữa.
        if new_product > limit:
            break

        # Thêm số lượng các số chia hết cho tích mới
        count += limit // new_product

        # Trừ đi các phần tử bị đếm lặp (giao của tập hiện tại với các tập sau)
        # bằng cách gọi đệ quy cho các phần tử còn lại
        count -= inclusion_exclusion_recursive(limit, primes, i + 1, new_product)

    return count


def count_valid_numbers(limit, N):
    """
    Đếm số lượng các số từ 1 đến 'limit' KHÔNG chia hết cho bất kỳ số nào trong [2, N].
    """
    if limit == 0:
        return 0

    primes_to_check = [p for p in ALL_PRIMES if p <= N]

    # Đếm số lượng số "xấu" bằng hàm đệ quy đã tối ưu
    bad_numbers = inclusion_exclusion_recursive(limit, primes_to_check, 0, 1)

    # Số lượng số "tốt" = tổng số - số lượng số "xấu"
    return limit - bad_numbers


def solve():
    """Hàm chính để đọc input và xử lý các test case."""
    while True:
        line = sys.stdin.readline().strip()
        if not line or line == '-1':
            break

        try:
            L, R = map(int, line.split())
            N = int(sys.stdin.readline())

            ans = count_valid_numbers(R, N) - count_valid_numbers(L - 1, N)
            print(ans)

        except (IOError, ValueError):
            break


solve()
'''
import sys

# Các số nguyên tố nhỏ hơn hoặc bằng 50
ALL_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def count_divisible_in_range_recursive(L, R, primes, start_index, current_product):
    """
    Hàm đệ quy tính số lượng số trong [L, R] chia hết cho ít nhất một số trong 'primes'.
    Đây là phiên bản tối ưu, chỉ duyệt cây đệ quy một lần.
    """
    count = 0
    # Lặp qua các số nguyên tố còn lại để thêm vào tích
    for i in range(start_index, len(primes)):

        new_product = current_product * primes[i]

        # Nhánh cận: Nếu tích mới đã lớn hơn R, không cần xét nữa
        if new_product > R:
            break

        # Số lượng bội số của new_product trong đoạn [L, R]
        term = (R // new_product) - ((L - 1) // new_product)

        # Thêm số lượng này vào (theo nguyên lý bao hàm)
        count += term

        # Trừ đi các phần tử bị đếm lặp (giao của tập hiện tại với các tập sau)
        count -= count_divisible_in_range_recursive(L, R, primes, i + 1, new_product)

    return count


def solve():
    """Hàm chính để đọc input và xử lý các test case."""
    while True:
        line = sys.stdin.readline().strip()
        if not line or line == '-1':
            break

        try:
            L, R = map(int, line.split())
            N = int(sys.stdin.readline())

            # Lọc ra các số nguyên tố cần dùng
            primes_to_check = [p for p in ALL_PRIMES if p <= N]

            # Tổng số lượng số trong đoạn [L, R]
            total_numbers_in_range = R - L + 1

            # Tính số lượng số "xấu" (bị chia hết) trong đoạn [L, R] chỉ bằng một lần gọi
            bad_numbers_in_range = count_divisible_in_range_recursive(L, R, primes_to_check, 0, 1)

            # Kết quả là số "tốt"
            ans = total_numbers_in_range - bad_numbers_in_range
            print(ans)

        except (IOError, ValueError):
            break


solve()