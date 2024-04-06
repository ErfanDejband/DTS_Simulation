import numpy as np

def simulate(start=0, stop=30, step_size=0.15, H_start=None, H_stop=None, num_points=2000, spacial_res=1.5, env_temp=22, H_temperature=None):
    """
    Simulate DTS data.

    Parameters:
        start (float): Starting position of the DTS data.
        stop (float): Ending position of the DTS data.
        step_size (float): Step size between data points.
        H_start (float or None): Starting temperature value.
        H_stop (float or None): Ending temperature value.
        num_points (int): Number of points for the z array.
        spacial_res (float): Spatial resolution. If provided, calculates new constants and AAA value accordingly.
        env_temp (float): Environmental temperature. Default is 22.
        H_temperature (float): Heating temperature.

    Returns:
        actual_T (numpy.ndarray): Actual temperature array.
        DDTS (numpy.ndarray): Sum of DTS_T along the axis.
    """
    # Create z array
    Tuner = Tuner = (num_points - 1) * step_size/(stop - start)   # 10
    z = np.linspace(start, stop, num_points)

    # Calculate constants
    Constance1 = 0.14693333333333336 # adjust this if you simulator is not same as your experimental data
    Constance2 = 2.715 # adjust this if you simulator is not same as your experimental data
    
    if spacial_res is not None:
        # Calculate new constants based on spatial resolution
        New_sysconfig_spacial_res = spacial_res
        New_Constance2 = (New_sysconfig_spacial_res * Constance2) / 2
        New_Constance1 = Constance1 * (Constance2 / New_Constance2)
    else:
        New_sysconfig_spacial_res = None
        New_Constance2 = None
        New_Constance1 = None

    # Calculate actual temperature
    actual_T = np.full(z.shape, env_temp)
    if H_start is not None and H_stop is not None:
        if H_start < start or H_stop > stop:
            raise ValueError("Heating temperature range is outside the specified simulation range.")
        elif H_temperature is None:
            raise ValueError("Heating temperature is not provided.")
        else:
            # Convert H_start and H_stop to indices based on z
            H_start_idx = np.abs(z - H_start).argmin()
            H_stop_idx = np.abs(z - H_stop).argmin()
        
        # Update actual_T within the specified range
        actual_T[H_start_idx:H_stop_idx] = H_temperature

    # Calculate the Gaussian function for all values of z
    # refer to https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2013WR014979?utm_sq=gqzx3u0l8q
    Halo_sigma = spacial_res / Constance2 
    sigma = step_size / Halo_sigma
    X, MU = np.meshgrid(z, z)
    DTS_T = gaussian(X, MU, sigma) * actual_T * Constance1  * spacial_res / Tuner
    DDTS = np.sum(DTS_T, axis=1)

    return z,actual_T, DDTS

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))