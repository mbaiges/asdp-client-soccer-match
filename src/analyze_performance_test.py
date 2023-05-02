import sys
import json
import numpy as np
import os
import matplotlib.pyplot as plt
import scipy.stats as st

OUTPUT_PATH = "tmp"

################
## UTILS
################

def usage():
    return f"Usage: {sys.argv[0]} " + "{perf_filename}"

def plot_hist(data):
    iqr = np.subtract(*np.percentile(data, [75, 25]))
    bin_width = 2 * iqr * len(data) ** (-1/3)
    num_bins = int((data.max() - data.min()) / bin_width)

    plt.title("Message processing time histogram")
    plt.xlabel("Processing time (ms)")
    plt.ylabel("Probability")

    # Probabilities histogram
    weights = np.ones_like(data) / data.shape[0]
    plt.hist(data, bins=num_bins, weights=weights)
    plt.xlim(0.0,1.34)
    plt.ylim(0.0,0.25)

    # # Compare to a normal curve
    # params = st.norm.fit(data)
    # x = np.linspace(0, max(data), 100)
    # y = st.norm.pdf(x, *params)
    # y = y * bin_width
    # plt.plot(x, y, 'r-')

    plt.show()

def get_distribution_type(values):
  # convert values to a numpy array
  values = np.array(values)

  # define a list of possible distributions
  distributions = [st.norm, st.expon, st.poisson, st.binom, st.uniform]

  # initialize the best distribution and the best parameters
  best_distribution = None
  best_params = None
  best_score = -np.inf

  # loop through each distribution
  for distribution in distributions:
    # try to fit the distribution to the data
    try:
      # get the parameters of the distribution
      params = distribution.fit(values)

      # calculate the log-likelihood of the data given the distribution
      log_likelihood = np.sum(distribution.logpdf(values, *params))

      # compare the log-likelihood with the best score
      if log_likelihood > best_score:
        # update the best distribution, parameters and score
        best_distribution = distribution
        best_params = params
        best_score = log_likelihood

    except:
      # ignore any errors in fitting
      pass

  # return the name of the best distribution and its parameters
  return best_distribution.name, best_params, best_score

def read_json_file(file_p, file_name):
    if os.path.exists(file_p) and os.path.isdir(file_p):
        if os.path.exists(os.path.join(file_p, file_name)) and os.path.isfile(os.path.join(file_p, file_name)):
            with open(os.path.join(file_p, file_name), "r") as file:
                try:
                    data = json.load(file)
                    return data
                except json.JSONDecodeError:
                    return None
        else:
            with open(os.path.join(file_p, file_name), "w") as file:
                return None
    else:
        os.makedirs(file_p, exist_ok=True)
        with open(os.path.join(file_p, file_name), "w") as file:
            return None

def save_json_file(file_p, file_name, data):
    if os.path.exists(file_p) and os.path.isdir(file_p):
        with open(os.path.join(file_p, file_name), "w") as file:
            json.dump(data, file)
            print("File saved")
    else:
        os.makedirs(file_p, exist_ok=True)
        with open(os.path.join(file_p, file_name), "w") as file:
            json.dump(data, file)
            print("Directory and file saved")

def analyze_with_new(output_filename, processing_times):
    if output_filename is None:
        print(f"Error: filename needed")
        exit(1)

    saved_proc_times = read_json_file(OUTPUT_PATH, output_filename)
    if saved_proc_times is None:
        saved_proc_times = []
    if processing_times is not None:
        saved_proc_times.extend(processing_times)
        save_json_file(OUTPUT_PATH, output_filename, saved_proc_times)

    processing_times_arr = np.array(saved_proc_times)
    processing_time_avg = processing_times_arr.mean() if len(saved_proc_times) > 0 else None
    print(f'Average processing time: {processing_time_avg:.03f}')

    # Guess distribution type
    dist_name, _, _ = get_distribution_type(saved_proc_times)
    print(f"Most likely distribution: {dist_name}")

    # Plot
    print(f"Plotting {len(saved_proc_times)} values.")
    plot_hist(processing_times_arr)

def analyze(output_filename):
    analyze_with_new(output_filename, None)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: missing arguments")
        print(usage())
        exit(1)

    perf_filename = sys.argv[1]
    analyze(perf_filename)