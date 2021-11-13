from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file

start = datetime.datetime(2021, 3, 1)
end = datetime.datetime(2021, 6, 10)

df = data.DataReader(name="AAPL", data_source="yahoo", start=start, end=end)
# df
def inc_dec(c, o):
    if (c > o):
        value = "increase"
    elif (o > c):
        value = "decrease"
    else:
        value = "equal"
    return value

df["Status"] = [inc_dec(c, o) for c, o in zip(df.Close, df.Open)]
df["middle"] = (df.Open + df.Close) / 2
df["height"] = abs(df.Close - df.Open)
df

p = figure(x_axis_type='datetime', width=1000, height=300)

p.title= 'Candlestick Chart'

p.grid.grid_line_alpha = 0.2

hours_12 = 12 * 60 * 60 * 1000

p.segment(df.index, df.High, df.index, df.Low, color="black")

p.rect(df.index[df.Status == "increase"], df.middle[df.Status == "increase"], hours_12,
       df.height[df.Status == "increase"],
       fill_color="#32CD32", line_color="black")
p.rect(df.index[df.Status == "decrease"], df.middle[df.Status == "decrease"], hours_12,
       df.height[df.Status == "decrease"], fill_color="red", line_color="black")
output_file("CS.html")
show(p)



