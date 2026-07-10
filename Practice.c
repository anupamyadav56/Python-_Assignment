#include <stdio.h>
#include <stdlib.h>

// Function to compare integers for qsort
int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

// Function to calculate minimum boosters
int min_boosters(int num_devices, int distances[], int F) {
    // Sort device distances
    qsort(distances, num_devices, sizeof(int), compare);

    int boosters = 0;
    int current_reach = 0;
    int i = 0;

    while (i < num_devices) {
        // If next device is within reach, move forward
        if (distances[i] <= current_reach + F) {
            current_reach = distances[i];
            i++;
        } else {
            // Place a booster to extend reach
            boosters++;
            current_reach += F;
        }
    }

    // Final check: if last device not covered
    if (current_reach < distances[num_devices - 1]) {
        boosters++;
    }

    return boosters;
}

int main() {
    int num_devices;
    scanf("%d", &num_devices);

    int distances[num_devices];
    for (int i = 0; i < num_devices; i++) {
        scanf("%d", &distances[i]);
    }

    int F;
    scanf("%d", &F);

    int result = min_boosters(num_devices, distances, F);
    printf("%d\n", result);

    return 0;
}