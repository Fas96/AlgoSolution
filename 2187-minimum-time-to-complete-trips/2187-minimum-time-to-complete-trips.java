class Solution {
    public long minimumTime(int[] time, int totalTrips) {
      long lowestTimeFrame = 1;
        long totalNumberOfTripsWeCanMake = Arrays.stream(time).min().getAsInt() * (long) totalTrips;

        while (lowestTimeFrame < totalNumberOfTripsWeCanMake) {
            final long midFrame = (lowestTimeFrame + totalNumberOfTripsWeCanMake) / 2;
            if (canCompleteTrips(time, midFrame,totalTrips)) totalNumberOfTripsWeCanMake = midFrame;
            else lowestTimeFrame = midFrame + 1;
        }

        return lowestTimeFrame;
    }

    private boolean canCompleteTrips(int[] time, long m,int totalTrips) {
        return Arrays.stream(time).asLongStream().reduce(0L, (subtotal, t) -> subtotal + m / t)>= totalTrips;
    }
}