#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {

    // declare variables
    double m, k, x, x_prev, v, t_max, dt, t, a;
    vector<double> t_list, x_list, v_list;

    // mass, spring constant, initial position and velocity
    m = 1;
    k = 1;
    x = 0;
    v = 1;
    

    // simulation time and timestep
    t_max = 100;
    dt = 0.1;
    x_prev = x - dt * v;

    // Verlet integration
    for (t = 0; t <= t_max; t = t + dt) {

        // append current state to trajectories
        t_list.push_back(t);
        x_list.push_back(x);
        v_list.push_back(v);

        // calculate new position and velocity using the previous state
        double x_old = x;
        a = -k * x / m;
        double x_new = 2 * x - x_prev + dt * dt * a;
        v = (x_new - x_old) / dt; // update velocity from old/current state
        x_prev = x_old;
        x = x_new; // update current position

    }

    // Write the trajectories to the same file that the Python plot script reads.
    // ios::trunc ensures that each new run replaces the previous run's data.
    const string output_path = "C:/Users/benok/OneDrive - University of Cambridge/1B coursework/mars lander/lander/trajectories.txt";
    ofstream fout(output_path, ios::out | ios::trunc);
    if (fout) { // file opened successfully
        for (int i = 0; i < t_list.size(); i = i + 1) {
            fout << t_list[i] << ' ' << x_list[i] << ' ' << v_list[i] << endl;
        }
    }
    else { // file did not open successfully
        cout << "Could not open trajectory file for writing" << endl;
    }

    /* The file can be loaded and visualised in Python as follows:

    import numpy as np
    import matplotlib.pyplot as plt
    results = np.loadtxt('trajectories.txt')
    plt.figure(1)
    plt.clf()
    plt.xlabel('time (s)')
    plt.grid()
    plt.plot(results[:, 0], results[:, 1], label='x (m)')
    plt.plot(results[:, 0], results[:, 2], label='v (m/s)')
    plt.legend()
    plt.show()

    */
}
