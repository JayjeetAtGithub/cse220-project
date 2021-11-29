import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == "__main__":

    result = {
        "stage": [],
        "time (s)": []
    }
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        with open(f"result_openroad/result_openroad.log.{num}") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip().split(":")
                result["stage"].append(line[0])
                result["time (s)"].append(float(line[1]))

    df = pd.DataFrame(result)
    print(df)
    sns_plot = sns.barplot(x="stage", y="time (s)", ci="sd", data=df)
    fig = sns_plot.get_figure()
    plt.title("Time spent in different design flow stages")
    fig.savefig("plot_1_timing.png")
