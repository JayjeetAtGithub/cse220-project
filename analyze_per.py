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
        with open(f"results/skylake_aes/result_openroad_skylake_aes.log.{num}") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip().split(":")
                result["stage"].append(line[0])
                result["time (s)"].append(float(line[1]))

    df = pd.DataFrame(result).groupby("stage").mean() 
    dd = df["time (s)"].to_dict()

    sum = 0
    for k, v in dd.items():
        sum += float(v)
    
    print(sum)
    for k, v in dd.items():
        val = (float(v) / sum) * 100
        print(k, ": ",  val)

