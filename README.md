# Junction 2022 Hackathon project

Our algorithm optimizes energy usage and reduces energy consumption peaks.

The app uses API from Fingrid (Finnish national electricity transmission grid operator) to forecast energy consumption and production. By analyzing that data algorithm finds best possible time period to use energy. It is the time period when production level is highest compared over consumption.

The algorithm uses forecast provided by Fingrid on electricity consumption as a basis. By analyzing that data algorithm forecasts best possible time period to use energy. Also based on that data, the application tries to avoid electricity consumption peaks and equalize electricity consumption. Possibly, the application could also reduce electricity consumption due to the optimized charging time. In theory, the demand would level off, in which case the price of electricity would not fluctuate at all, but would remain constant.

For example, the use of electricity is high, especially in the evenings. The algorithm considers the best time to charge the batteries during the day, when the demand stabilizes in the evening, and then the price of electricity stays under control. The application also looks at the best time to regulate the operation of rechargeable devices. An example of this could be that the store's soft drinks refrigerator which would turn off the cooling in the morning when there are no customers and lower it towards the evening when there are customers. This would be a small saving but in big scale it makes huge difference!

The main idea of algorithm can be used either on a basic household level or even on a society level.

The code was written in 36 hours. 
