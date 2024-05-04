package HW.HW7;

import java.util.Arrays;
import java.util.PriorityQueue;

public class Solution {

    public int minMeetingRooms(int[][] intervals) {
        if (intervals == null || intervals.length == 0) {
            return 0;
        }

        // Sort the intervals by start time
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        // Use a min heap to track the minimum end time of merged intervals
        PriorityQueue<Integer> heap = new PriorityQueue<>();

        // Start with the first meeting, put it in a meeting room
        heap.offer(intervals[0][1]);

        for (int i = 1; i < intervals.length; i++) {
            // If the current meeting starts after the room at the min end time gets free,
            // then reuse the room
            if (intervals[i][0] >= heap.peek()) {
                heap.poll();
            }

            // Add the current meeting into the heap
            heap.offer(intervals[i][1]);
        }

        // The size of the heap tells us the minimum rooms required for all the
        // meetings.
        return heap.size();
    }

}
