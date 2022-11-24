import time
import multiprocessing as mp
import seaborn


def read_matrix(file_name):
    M = []
    with open(file_name, "r") as matrix_file:
        for line in matrix_file.readlines():
            row = list(map(int, line.split(";")))
            M.append(row)
    return M


def print_dimensions(M):
    print("number of rows =", len(M))
    print("number of columns =", len(M[0]))


def scalar_product(a, b):
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


def get_row(M, i):
    return M[i]


def get_column(M, j):
    res = []
    for i in range(len(M)):
        res.append(M[i][j])
    return res


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = (func(*args, **kwargs), time.time() - start_time)
        return res
    return wrapper


@time_decorator
def matrix_product(A, B):
    m = len(A)
    n = len(B[0])
    res = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            res[i][j] = scalar_product(get_row(A, i),
                                        get_column(B, j))
    return res


def proc_row(x):
    A, B, i = x[0], x[1], x[2]
    res = []
    for j in range(len(B[0])):
        res.append(scalar_product(
                    get_row(A, i),
                    get_column(B, j))
                )
    return res


@time_decorator
def matrix_product_mp(A, B, n):
    p = mp.Pool(n)
    # rows of a resulting matrix will
    # be calculated separately
    data = [(A, B, i) for i in range(len(A))]
    res = p.map(proc_row, data)
    return res


if __name__ == "__main__":
    A = read_matrix("matrix_1.csv")
    print_dimensions(A)
    B = read_matrix("matrix_2.csv")
    print_dimensions(B)
    res = matrix_product(A, B)
    C = res[0]
    print(res[1])

    cpu_num = mp.cpu_count() - 1
    print("Number of CPU: ", cpu_num + 1)
    for n in range(1, 21):
        print(n, "processes")
        res = matrix_product_mp(A, B, n)
        C_mp = [0]
        print(res[1])

    print("Coincidence of matrices: ", C == C_mp)
