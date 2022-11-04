# Program to calculate moving average
arr = [1, 2, 3, 7, 9]
window_size = 3
  
i = 0

moving_averages = []
  

while i < len(arr) - window_size + 1:

    window = arr[i : i + window_size]
  
    window_average = round(sum(window) / window_size, 2)
 
    moving_averages.append(window_average)
      
    i += 1
  
print(moving_averages)

def ChargingTime(interval, time):
    # Käydään läpi ennustearvot ja lasketaan 'time' pituinen liukuva keskiarvo
    # Keskiarvot taulukkoon jossa sarakkeet 'aloitusaika', 'lopetusaika' ja 'keskiarvo'
    # Keskiarvoista valitaan pienin
    # Return pienimmän keskiarvon aloitusaika

    # Calculates averages
    for i in range(len(arr) - time + 1):
        window = arr[i : i + time]
        window_avg = round(sum(window) / time, 3)
        avgs.append([arr[i], arr[i + time], window_avg])
    
    # Find min average and select the starting time to achieve that
    charging_time = min(avgs[2])

    return charging_time