This is known problem: counting double chars in a long string  
Simple test for python program performed by pytest. 
For test was taken string with 1.000.000 chars.
Exploring different methods, including external component writen on Rust

============================= test session starts =============================
platform win32 -- Python 3.8.8, pytest-6.2.3, py-1.10.0, pluggy-0.13.1
benchmark: 3.4.1 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)

benchmark: 9 tests
|Name (time in ms)        |          Min         |        Max         |        Mean         |     StdDev         |     Median         |        IQR          |  Outliers|       OPS       |     Rounds|  Iterations|
|-------------------------|----------------------|--------------------|---------------------|--------------------|--------------------|---------------------|----------|-----------------|-----------|------------|
|test_rust_once           |       1.6983 (1.0)   |     2.4567 (1.0)   |      1.7207 (1.0)   |     0.0682 (1.0)   |     1.7042 (1.0)   |     0.0093 (1.0)    |     28;81|  581.1637 (1.0) |        566|           1|
|test_rust_pure           |       2.9971 (1.76)  |    37.8855 (15.42) |      3.3435 (1.94)  |     2.1859 (32.06) |     3.0571 (1.79)  |     0.0743 (7.99)   |      6;39|  299.0917 (0.51)|        314|           1|
|test_python_numpy        |       3.9310 (2.31)  |     9.0128 (3.67)  |      4.7457 (2.76)  |     0.7910 (11.60) |     4.4156 (2.59)  |     0.4313 (46.38)  |     33;37|  210.7180 (0.36)|        233|           1|
|test_regexp              |      65.1514 (38.36) |   195.7722 (79.69) |     91.5741 (53.22) |    31.7572 (465.77)|    85.2610 (50.03) |    15.6949 (>1000.0)|       1;2|   10.9201 (0.02)|         15|           1|
|test_pure_python         |     169.2898 (99.68) |   198.6297 (80.85) |    181.4316 (105.44)|    11.6145 (170.34)|   178.1684 (104.55)|    20.0032 (>1000.0)|       2;0|    5.5117 (0.01)|          6|           1|
|test_python_itertools    |     171.6756 (101.09)|   182.0148 (74.09) |    175.5716 (102.04)|     4.1640 (61.07) |   174.8385 (102.60)|     5.8766 (631.89) |       1;0|    5.6957 (0.01)|          6|           1|
|test_python_iter         |     173.0237 (101.88)|   202.1614 (82.29) |    184.7984 (107.40)|    12.1339 (177.96)|   186.7508 (109.59)|    18.7359 (>1000.0)|       1;0|    5.4113 (0.01)|          5|           1|
|test_python_comprehension|     175.8658 (103.55)|   259.0720 (105.46)|   206.2824 (119.88) |   31.8052 (466.47) |  201.3125 (118.13) |   43.3945 (>1000.0) |      1;0 |   4.8477 (0.01) |          6|           1|
|test_python_classic      |     276.4368 (162.77)|   708.0133 (288.20)|   390.9426 (227.20) |  182.1755 (>1000.0)|  300.7672 (176.49) |  180.2910 (>1000.0) |      1;0 |   2.5579 (0.00) |          5|           1|

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
============================= test session ends ===============================