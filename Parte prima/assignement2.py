import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate


class VoltageData:


    def __init__(self, times, voltages):
        t = np.array(times, dtype=np.float64)
        v = np.array(voltages, dtype=np.float64)
        self._data = np.column_stack([t,v])
        self.spline = interpolate.InterpolatedUnivariateSpline(self.timestamps, self.voltages, k=3)

    @property
    def timestamps(self):
        return self._data[:,0]

    @property
    def voltages(self):
        return self._data[:,1]
    @voltages.setter
    def voltages(self, new_values):
        self._data = np.column_stack([self.timestamps,new_values])


    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __iter__(self):
        return iter(self._data)

    def __str__(self):
        output_string = []
        row_fmt = '{:d}) {:.1f} {:.2f}'
        for i, entry in enumerate(self):
            output_string.append(row_fmt.format(i, entry[0], entry[1]))
        return '\n'.join(output_string)

    def plot(self, ax=None, fmt='bo--', **kwargs):
        if ax is not None:
            plt.sca(ax)
        else:
            plt.figure('Voltage vs Times')
        plt.plot(self.timestamps, self.voltages, fmt, **kwargs)
        plt.xlabel('Time [s]')
        plt.ylabel('Voltages [mV]')
        plt.grid(True)
        return plt.gca()

    def __call__(self, t): #call interpola
        spl = interpolate.InterpolatedUnivariateSpline(self.timestamps, self.voltages, k=3)
        return self.spline(t)


if __name__ == '__main__':
    t,v = np.loadtxt('sample_data_file.txt', unpack = True)
    v_data = VoltageData(t,v)
    assert len(v_data)==len(t)
    assert np.all(v_data.voltages == v)
    assert np.all(v_data.timestamps == t)
    assert v_data[3,1] == v[3] #voglio una matrice 2D
    assert v_data[-1, 0] == t[-1]
    assert np.all(v_data[1:5,1]==v[1:5])

    for i, entry in enumerate(v_data):
        assert entry[0] == t[i]
        assert entry[1] == v[i]
    print(v_data)
    plt.figure('My_figure')
    plt.plot(t, 2*v, 'r^', markersize=5, label='double voltage')
    v_data.plot(ax=plt.gca(), markersize=5, label = 'normal voltage')
    plt.legend()
    v_data.plot(fmt='ko', markersize=5, label = 'normal voltage')
    x_grid = np.linspace(min(t), max(t), 200)
    plt.plot(x_grid, v_data(x_grid), 'r-', label='spline')
    plt.legend()
    plt.show()
