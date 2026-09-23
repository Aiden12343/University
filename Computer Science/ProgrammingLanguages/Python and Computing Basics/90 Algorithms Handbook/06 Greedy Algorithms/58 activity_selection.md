# activity_selection

6 GREEDY ALGORITHMS
Make the locally best choice; only valid when proven.
activity_selection(intervals) FUNCTION
Return the largest set of non-overlapping (start, end) intervals.
REMEMBER Sort by END time; take an interval if it starts after the last chosen one ended. Finishing earliest leaves the
most room.
WHEN TO USE Maximise the NUMBER of meetings/jobs in one room/machine.
AVOID WHEN Intervals have weights/values (needs DP); sorting by start or length is WRONG.
REQUIRES List of (start_time, end_time) tuples.
TIME O(n log n). SPACE O(n).
USED FOR Room booking, CPU scheduling, interval scheduling.
def activity_selection(intervals):
chosen_intervals = []
finish_time_of_last_chosen = float("-inf")
for start_time, finish_time in sorted(intervals, key=lambda interval: interval[1]):
if start_time >= finish_time_of_last_chosen:
chosen_intervals.append((start_time, finish_time))
finish_time_of_last_chosen = finish_time
return chosen_intervals
INPUT meetings = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 11)] # (start_time, end_time)
activity_selection(meetings)
OUTPUT [(1, 4), (5, 7), (8, 11)]
IN PRODUCTION No standard routine: sorted() plus one loop is the production form. Solvers (OR-Tools) only matter for weighted or
constrained scheduling.
CS Algorithms Toolkit Greedy algorithms
58
