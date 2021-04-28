ERROR_EXCEPTION = 1
ERROR_WRONG_SETTINGS = 2
ERROR_PYTHON_VERSION = 3
ERROR_MODULES_MISSING = 4
ERROR_QT_VERSION = 5

# # class MySupress:
# #     def __init__(self, *exceprions):
# #         self.exp = exceprions
# #
# #     def __enter__(self):
# #         return self
# #
# #     def __exit__(self, exc_type, exc_val, exc_tb):
# #         if exc_val is None:
# #             return True
#
# from contextlib import contextmanager
# import time
# import sys
#
# @contextmanager
# def timeit():
#     start = time.perf_counter()
#     try:
#         yield
#     finally:
#         stop = time.perf_counter()
#         elapsed = stop - start
#     print(elapsed)
#
# with timeit():
#     s = 0
#     for i in range(10000):
#         for j in range(1000):
#             s += i + j
#
#
# @contextmanager
# def supress(*exc):
#     try:
#         yield
#     except:
#         t, v, tb = sys.exc_info()
#         if not isinstance(v, exc):
#             raise Exception
#
#
# data = None
# with supress(FileNotFoundError, FileExistsError):
#     with open('form_style.py') as f:
#         data = f.read()
#     print('ok')