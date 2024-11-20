import numpy as np

def calculate_error_with_covariance(N, FWHMs):
    """
    Calculate the error on the mean using the covariance matrix.
    
    Parameters:
        N (int): Number of observations.
        FWHMs (list or numpy array): List of FWHM values for each sample distribution.
        
    Returns:
        float: The error on the mean.
    """
    # Convert FWHM to standard deviation
    variances = (np.array(FWHMs) / 2.3548) ** 2  # Variance for each sample
    
    # Create the covariance matrix (diagonal matrix in this case)
    covariance_matrix = np.diag(variances)
    
    # Create a vector of ones (N-dimensional)
    ones_vector = np.ones(N)
    
    # Calculate the error on the mean using the covariance matrix
    error_on_mean_squared = (1 / N**2) * ones_vector.T @ covariance_matrix @ ones_vector
    error_on_mean = np.sqrt(error_on_mean_squared)
    
    return error_on_mean

# Example usage
N = 5  # Number of observations
FWHMs = [10, 10, 10, 10, 10]  # FWHM values for each sample distribution

error_on_mean = calculate_error_with_covariance(N, FWHMs)
print(f"Error on the mean: {error_on_mean}")
