import json
import pandas as pd
from matplotlib import pyplot as plt
from datetime import date, timedelta, datetime

start_time = date.today()
end_time = start_time + timedelta(days=1)

start_time = str(datetime.strftime(start_time, "%Y-%m-%d"))
end_time = str(datetime.strftime(end_time, "%Y-%m-%d"))

#kulutus ennuste
#url_166 = "https://api.fingrid.fi/v1/variable/166/events/csv?start_time={start_time}T00%3A00%3A00Z&end_time=2022-11-05T00%3A00%3A00Z"

url_166 = "https://api.fingrid.fi/v1/variable/166/events/csv?start_time=" + start_time + "T00%3A00%3A00Z&end_time=" + end_time + "T00%3A00%3A00Z"
#tuulivoima tuotanto ennuste
#url_245 = "https://api.fingrid.fi/v1/variable/245/events/csv?start_time="{start_time}"T00%3A00%3A00Z&end_time=2022-11-05T00%3A00%3A00Z"
#sähkötuotanto ennuste
#url_241 = "https://api.fingrid.fi/v1/variable/241/events/csv?start_time={start_time}T00%3A00%3A00Z&end_time=2022-11-05T00%3A00%3A00Z"


def GetDataAPI(url):
    df_kulutus = pd.read_csv(url)

    df_kulutus.columns = ["start_time","end_time","value"]

    # Convert value to pd datetime
    df_kulutus["start_time"] = pd.to_datetime(df_kulutus["start_time"]).dt.tz_localize(None)
    df_kulutus["end_time"] = pd.to_datetime(df_kulutus["end_time"]).dt.tz_localize(None)
    
    # Start time of interval
    start_date = pd.to_datetime("today")

    # Rajataan aikavälin mukaan
    df_kulutus_filt = df_kulutus[df_kulutus["start_time"] > start_date]

    # Valitaan vain kolme saraketta

    return df_kulutus_filt.values.tolist(), df_kulutus

def varFromJSON():
    # open file object
    file = open("./Data/data.json")

    # load data from file
    data = json.load(file)

    # get specific data from JSON response
    charging_time = data["minute"] # duration
    time_window = data["time"] # interval

    # create list for items    
    data_list = []

    # add items to list
    data_list.append(charging_time)
    data_list.append(time_window)

    return data_list

def ChargingTime(interval, duration, arr):
    """
    Params:
    interval = int
    how many data points to take account to find best rolling average

    duration = int
    how many data points take count to calculating average

    arr = [[start, end, value], [start, end, value],...]
    list of lists containing starting time ending time and value
    """
    
    avgs = []
    duration = round(duration / 5)
    interval = round(interval / 5)
        # Calculates averages
    for i in range(len(arr) - duration + 1):
        t1 = arr[i][0]
        t2 = arr[i][1]

        # Check if duration difference is bigger than interval
        if (pd.Timedelta(t2-t1).seconds / 60.0) > interval:
            break
        else:
            window = arr[i : i + duration]
            sum = 0
            for j in window:
                sum = sum + j[2]

            window_avg = round(sum / duration, 3)
                
            if (len(arr) - 1) > i + duration:
                avgs.append([arr[i][0], arr[i + duration][1], window_avg])

    # Find min average and select the starting duration to achieve that
    min_avg = [float('inf'), "", ""]
    for k in avgs:
        
        if min_avg[0] > k[2]:
            min_avg[0] = k[2]
            min_avg[1] = k[0]
            min_avg[2] = k[1]

    return min_avg

def FindChargingTime(list,df, kesto, intervalli):

    output = ChargingTime(intervalli, kesto, list)
    
    plt.rcParams["figure.figsize"] = [8, 4]
    plt.rcParams["figure.autolayout"] = True
    plt.rcParams["figure.dpi"] = 150

    plt.plot(df["start_time"], df["value"])
    plt.scatter(output[1], output[0], c="red")
    plt.scatter(output[2], output[0], c="red")

    x_values = [output[1], output[2]]
    y_values = [output[0], output[0]]

    plt.plot(x_values, y_values, c="red", linestyle="--", label="Charging time")

    plt.ylabel("Kulutusennuste")
    plt.legend()
    plt.savefig("outputs/fig.png")
    plt.show()

    return output

data, df = GetDataAPI(url_166)

result = FindChargingTime(data,df, varFromJSON()[0], varFromJSON()[1])
res = pd.DataFrame(result)
res.to_csv("outputs/result.csv", header=True)
print(result[1])
